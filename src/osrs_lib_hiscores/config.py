from urllib.parse import quote

from .enums import AccountType


class APIConfig:
    """Utilities for constructing hiscore and profile URLs."""

    BASE_URL = "https://secure.runescape.com"
    USER_ENDPOINT = "index_lite.json"

    ACCOUNT_TYPE_PATHS: dict[AccountType, str] = {
        AccountType.NORMAL: "/m=hiscore_oldschool/",
        AccountType.IRONMAN: "/m=hiscore_oldschool_ironman/",
        AccountType.HARDCORE_IRONMAN: "/m=hiscore_oldschool_hardcore_ironman/",
        AccountType.ULTIMATE_IRONMAN: "/m=hiscore_oldschool_ultimate/",
        AccountType.DEADMAN: "/m=hiscore_oldschool_deadman/",
        AccountType.SEASONAL: "/m=hiscore_oldschool_seasonal/",
    }

    def __new__(cls) -> None:
        """Prevent instantiation of this utility class."""
        raise TypeError("APIConfig is a utility class and cannot be instantiated")

    @staticmethod
    def build_hiscore_url(account_type: AccountType, endpoint: str) -> str:
        """Build a full hiscore URL for the given account type and endpoint."""
        return f"{APIConfig.BASE_URL}{APIConfig.ACCOUNT_TYPE_PATHS[account_type]}{endpoint}"

    @staticmethod
    def build_user_page_url(account_type: AccountType, username: str) -> str:
        """Build the official JSON profile URL for a player username."""
        return APIConfig.build_hiscore_url(
            account_type, f"{APIConfig.USER_ENDPOINT}?player={quote(username, safe='')}"
        )

    @staticmethod
    def build_skill_page_url(
        account_type: AccountType, table_id: int, page: int
    ) -> str:
        """Build a skill hiscore page URL for a specific table and page number."""
        if page < 1:
            raise ValueError("page must be >= 1")
        return APIConfig.build_hiscore_url(
            account_type, f"overall?table={table_id}&page={page}"
        )

    @staticmethod
    def build_activity_page_url(
        account_type: AccountType, table_id: int, page: int
    ) -> str:
        """Build an activity hiscore page URL for a specific table and page number."""
        if page < 1:
            raise ValueError("page must be >= 1")
        return APIConfig.build_hiscore_url(
            account_type, f"overall?category_type=1&table={table_id}&page={page}"
        )
