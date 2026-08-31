from osrs_lib_hiscores.models import (
    HiscoreActivity,
    HiscoreEntry,
    HiscoreSkill,
    Player,
    PlayerActivity,
    PlayerEntry,
    PlayerSkill,
)


def test_hiscore_entry() -> None:
    entry = HiscoreEntry(rank=1, player="Zooknock")
    assert entry.rank == 1
    assert entry.player == "Zooknock"


def test_hiscore_activity() -> None:
    activity = HiscoreActivity(rank=2, player="Zooknock", score=99)
    assert activity.rank == 2
    assert activity.player == "Zooknock"
    assert activity.score == 99


def test_hiscore_skill() -> None:
    skill = HiscoreSkill(rank=3, player="Zooknock", level=99, xp=13_034_431)
    assert skill.rank == 3
    assert skill.player == "Zooknock"
    assert skill.level == 99
    assert skill.xp == 13_034_431


def test_player_entry() -> None:
    entry = PlayerEntry(id=42, name="Zooknock", rank=7)
    assert entry.id == 42
    assert entry.name == "Zooknock"
    assert entry.rank == 7


def test_player_activity() -> None:
    activity = PlayerActivity(id=1, name="Zooknock", rank=8, score=123)
    assert activity.score == 123


def test_player_skill() -> None:
    skill = PlayerSkill(id=1, name="Zooknock", rank=9, level=99, xp=200_000_000)
    assert skill.level == 99
    assert skill.xp == 200_000_000


def test_player() -> None:
    player = Player(
        player="Zooknock",
        skills={},
        activities={},
    )
    assert player.player == "Zooknock"
    assert player.skills == {}
    assert player.activities == {}
