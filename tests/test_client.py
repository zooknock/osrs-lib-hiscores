from unittest.mock import Mock, patch

from osrs_lib_hiscores.client import HiscoreClient
from osrs_lib_hiscores.enums import AccountType, Activity, Skill
from osrs_lib_hiscores.models import HiscoreActivity, HiscoreSkill, Player


def test_get_dispatches_to_get_user() -> None:
    client = HiscoreClient()
    client.get = Mock(return_value=Player("Zooknock", {}, {}))

    result = client.get(AccountType.NORMAL, "Zooknock")

    assert isinstance(result, Player)
    client.get.assert_called_once_with(AccountType.NORMAL, "Zooknock")


def test_get_dispatches_to_skill_page() -> None:
    client = HiscoreClient()
    client._get_skill_page = Mock(return_value=[])

    result = client.get(AccountType.NORMAL, Skill.ATTACK, 1)

    assert result == []
    client._get_skill_page.assert_called_once_with(AccountType.NORMAL, Skill.ATTACK, 1)


def test_get_dispatches_to_activity_page() -> None:
    client = HiscoreClient()
    client._get_activity_page = Mock(return_value=[])

    result = client.get(AccountType.NORMAL, Activity.ZULRAH, 1)

    assert result == []
    client._get_activity_page.assert_called_once_with(AccountType.NORMAL, Activity.ZULRAH, 1)


@patch("osrs_lib_hiscores.client.requests.Session.get")
def test_get_user_parses_player(mock_get: Mock) -> None:
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {
        "name": "Zooknock",
        "skills": [{"id": 1, "name": "Attack", "rank": 10, "level": 99, "xp": 13}],
        "activities": [{"id": 90, "name": "Zulrah", "rank": 5, "score": 7}],
    }
    mock_get.return_value = response

    client = HiscoreClient()
    player = client.get(AccountType.NORMAL, "Zooknock")

    assert player.player == "Zooknock"
    assert player.skills[Skill.ATTACK].name == "Attack"
    assert player.activities[Activity.ZULRAH].name == "Zulrah"


@patch("osrs_lib_hiscores.client.requests.Session.get")
def test_get_skill_page_parses_html(mock_get: Mock) -> None:
    response = Mock()
    response.text = "<html><body>skill</body></html>"
    mock_get.return_value = response

    client = HiscoreClient()
    client._parse_skill_page = Mock(return_value=[])

    result = client.get(AccountType.NORMAL, Skill.ATTACK, 1)

    assert result == []
    client._parse_skill_page.assert_called_once_with("<html><body>skill</body></html>")


@patch("osrs_lib_hiscores.client.requests.Session.get")
def test_get_activity_page_parses_html(mock_get: Mock) -> None:
    response = Mock()
    response.text = "<html><body>activity</body></html>"
    mock_get.return_value = response

    client = HiscoreClient()
    client._parse_activity_page = Mock(return_value=[])

    result = client.get(AccountType.NORMAL, Activity.ZULRAH, 1)

    assert result == []
    client._parse_activity_page.assert_called_once_with("<html><body>activity</body></html>")


def test_parse_skill_page_empty_table_returns_empty_list() -> None:
    client = HiscoreClient()
    assert client._parse_skill_page("<html><body></body></html>") == []


def test_parse_activity_page_empty_table_returns_empty_list() -> None:
    client = HiscoreClient()
    assert client._parse_activity_page("<html><body></body></html>") == []


def test_parse_skill_page_parses_row() -> None:
    client = HiscoreClient()
    html = """
    <table>
      <tr class="personal-hiscores__row">
        <td></td><td>1</td><td><a>Zooknock</a></td><td>99</td><td>13,034,431</td>
      </tr>
    </table>
    """
    result = client._parse_skill_page(html)

    assert result == [HiscoreSkill(player="Zooknock", rank=1, level=99, xp=13_034_431)]


def test_parse_activity_page_parses_row() -> None:
    client = HiscoreClient()
    html = """
    <table>
      <tr class="personal-hiscores__row">
        <td>1</td><td><a>Zooknock</a></td><td>42</td>
      </tr>
    </table>
    """
    result = client._parse_activity_page(html)

    assert result == [HiscoreActivity(player="Zooknock", rank=1, score=42)]
