from typing import Any, overload

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .config import AccountType, APIConfig
from .enums import Activity, Skill
from .models import HiscoreActivity, HiscoreSkill, Player, PlayerActivity, PlayerSkill


class HiscoreClient:
    """OSRS hiscore data scraper with automatic retries and rate-limit handling."""

    def __init__(
        self, timeout: int = 10, delay: float = 2.0, max_retries: int = 5
    ) -> None:
        """
        Initialize the client.

        Args:
            timeout: Request timeout in seconds (default: 10).
            delay: Backoff delay multiplier for retries (default: 2.0).
            max_retries: Maximum retry attempts (default: 5).
        """
        self.timeout = timeout
        self.session = requests.Session()

        retry = Retry(
            total=max_retries,
            backoff_factor=delay,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers["User-Agent"] = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )

    @overload
    def get(self, account_type: AccountType, target: str) -> Player: ...

    @overload
    def get(
        self, account_type: AccountType, target: Skill, page: int = 1
    ) -> list[HiscoreSkill]: ...

    @overload
    def get(
        self, account_type: AccountType, target: Activity, page: int = 1
    ) -> list[HiscoreActivity]: ...

    def get(
        self,
        account_type: AccountType,
        target: str | Activity | Skill,
        page: int = 1,
    ) -> Player | list[HiscoreSkill] | list[HiscoreActivity]:
        """
        Fetch a player profile or hiscore rankings.

        Args:
            account_type: The account type to query.
            target: A username for player lookup, or a Skill/Activity for ranking lookup.
            page: The hiscore page number to fetch; required when target is a Skill or Activity.

        Returns:
            A Player when target is a username, or a list of HiscoreSkill / HiscoreActivity
            entries when fetching rankings.

        Raises:
            TypeError: If page is not provided for skill/activity ranking lookups.
        """

        if isinstance(target, str):
            return self._get_user(account_type, target)

        if isinstance(target, Activity):
            return self._get_activity_page(account_type, target, page)
        if isinstance(target, Skill):
            return self._get_skill_page(account_type, target, page)

    def _get_user(self, account_type: AccountType, username: str) -> Player:
        """Fetch player profile from official API.

        Args:
            account_type: Account type (e.g. AccountType.MAIN, AccountType.ULTIMATE_IRONMAN).
            username: Player username.

        Returns:
            Player object with skills and activities.

        Raises:
            requests.RequestException: On network or HTTP errors.
        """
        url = APIConfig.build_user_page_url(account_type, username)
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return self._parse_player(response.json())

    def _get_skill_page(
        self, account_type: AccountType, entity: Skill, page: int
    ) -> list[HiscoreSkill]:
        """Fetch hiscore rankings for a specific skill, scraped from HTML hiscores.

        Args:
            account_type: Account type (e.g. AccountType.MAIN, AccountType.ULTIMATE_IRONMAN).
            entity: Skill to fetch rankings for (e.g. Skill.OVERALL, Skill.Woodcutting)
            page: Page number (1-indexed).

        Returns:
            List of HiscoreSkill objects.
        """
        html = self.session.get(
            APIConfig.build_skill_page_url(account_type, entity.id, page),
            timeout=self.timeout,
        ).text
        return self._parse_skill_page(html)

    def _get_activity_page(
        self, account_type: AccountType, entity: Activity, page: int
    ) -> list[HiscoreActivity]:
        """Fetch hiscore rankings for a specific activity, scraped from HTML hiscores.

        Args:
            account_type: Account type (e.g. AccountType.MAIN, AccountType.ULTIMATE_IRONMAN).
            entity: Activity to fetch rankings for (e.g. Activity.CALVARION, Activity.LMS_RANK)
            page: Page number (1-indexed).

        Returns:
            List of HiscoreActivity objects.
        """
        html = self.session.get(
            APIConfig.build_activity_page_url(account_type, entity.id, page),
            timeout=self.timeout,
        ).text
        return self._parse_activity_page(html)

    def _parse_player(self, data: dict[str, Any]) -> Player:
        """Convert JSON response to Player dataclass."""
        skills = {
            next(skill for skill in Skill if skill.id == s["id"]): PlayerSkill(
                id=s["id"],
                name=s["name"],
                rank=s["rank"],
                level=s["level"],
                xp=s["xp"],
            )
            for s in data.get("skills", [])
        }

        activities = {
            next(
                activity for activity in Activity if activity.id == a["id"]
            ): PlayerActivity(
                id=a["id"],
                name=a["name"],
                rank=a["rank"],
                score=a["score"],
            )
            for a in data.get("activities", [])
        }

        return Player(player=data["name"], skills=skills, activities=activities)

    def _parse_hiscore_table(
        self, html: str, column_config: dict[str, Any]
    ) -> list[dict[str, Any]]:
        """Parse hiscore HTML table with flexible column extraction for Skill and Activity pages."""
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table")
        if not table:
            return []
        rows = table.find_all("tr", class_="personal-hiscores__row")
        return [
            column_config["extractor"](cells)
            for row in rows
            if len(cells := row.find_all("td")) >= column_config["min_cells"]
        ]

    def _parse_activity_page(self, html: str) -> list[HiscoreActivity]:
        """Parse activity hiscore page."""
        config = {
            "min_cells": 3,
            "extractor": lambda cells: {
                "rank": int(cells[0].text.strip().replace(",", "")),
                "name": cells[1].find("a").text.strip(),
                "score": int(cells[2].text.strip().replace(",", "")),
            },
        }
        return [
            HiscoreActivity(player=r["name"], rank=r["rank"], score=r["score"])
            for r in self._parse_hiscore_table(html, config)
        ]

    def _parse_skill_page(self, html: str) -> list[HiscoreSkill]:
        """Parse skill hiscore page."""
        config = {
            "min_cells": 5,
            "extractor": lambda cells: {
                "rank": int(cells[1].text.strip().replace(",", "")),
                "name": cells[2].find("a").text.strip(),
                "level": int(cells[3].text.strip().replace(",", "")),
                "xp": int(cells[4].text.strip().replace(",", "")),
            },
        }
        return [
            HiscoreSkill(player=r["name"], rank=r["rank"], level=r["level"], xp=r["xp"])
            for r in self._parse_hiscore_table(html, config)
        ]
