from dataclasses import dataclass

from .enums import Activity, Skill


@dataclass
class HiscoreEntry:
    """Base columns for hiscore table data."""

    rank: int
    player: str


@dataclass
class HiscoreActivity(HiscoreEntry):
    """Hiscore activity row with a score value."""

    score: int


@dataclass
class HiscoreSkill(HiscoreEntry):
    """Hiscore skill row with level and XP values."""

    level: int
    xp: int


@dataclass
class PlayerEntry:
    """Base columns for player API data."""

    id: int
    name: str
    rank: int


@dataclass
class PlayerActivity(PlayerEntry):
    """Player activity entry with a score value."""

    score: int


@dataclass
class PlayerSkill(PlayerEntry):
    """Player skill entry with level and XP values."""

    level: int
    xp: int


@dataclass
class Player:
    """Full player API data containing skill and activity data."""

    player: str
    skills: dict[Skill, PlayerSkill]
    activities: dict[Activity, PlayerActivity]
