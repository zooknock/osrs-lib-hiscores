import pytest

from osrs_lib_hiscores.config import APIConfig
from osrs_lib_hiscores.enums import AccountType, Activity, Skill


def test_api_config_cannot_instantiate() -> None:
    with pytest.raises(TypeError):
        APIConfig()  # type: ignore[misc]


def test_build_user_page_url_encodes_username() -> None:
    url = APIConfig.build_user_page_url(AccountType.NORMAL, "Zooknock 123")
    assert "player=Zooknock%20123" in url


def test_build_skill_page_url_rejects_invalid_page() -> None:
    with pytest.raises(ValueError):
        APIConfig.build_skill_page_url(AccountType.NORMAL, Skill.ATTACK.id, 0)


def test_build_activity_page_url_rejects_invalid_page() -> None:
    with pytest.raises(ValueError):
        APIConfig.build_activity_page_url(AccountType.NORMAL, Activity.ZULRAH.id, 0)
