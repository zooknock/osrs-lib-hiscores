from osrs_lib_hiscores.enums import AccountType, Activity, Skill


def test_account_type_values() -> None:
    assert AccountType.NORMAL.value == "Normal"
    assert AccountType.IRONMAN.value == "Ironman"
    assert AccountType.HARDCORE_IRONMAN.value == "Hardcore Ironman"
    assert AccountType.ULTIMATE_IRONMAN.value == "Ultimate Ironman"
    assert AccountType.DEADMAN.value == "Deadman"
    assert AccountType.SEASONAL.value == "Seasonal"


def test_skill_ids_and_labels() -> None:
    assert Skill.OVERALL.id == 0
    assert Skill.OVERALL.label == "Overall"
    assert Skill.ATTACK.id == 1
    assert Skill.ATTACK.label == "Attack"
    assert Skill.SAILING.id == 24
    assert Skill.SAILING.label == "Sailing"


def test_activity_ids_and_labels() -> None:
    assert Activity.GRID_POINTS.id == 0
    assert Activity.GRID_POINTS.label == "Grid Points"
    assert Activity.ABYSSAL_SIRE.id == 20
    assert Activity.ABYSSAL_SIRE.label == "Abyssal Sire"
    assert Activity.ZULRAH.id == 90
    assert Activity.ZULRAH.label == "Zulrah"


def test_enum_members_are_unique() -> None:
    assert len(set(item.value for item in AccountType)) == len(AccountType)
    assert len(set(item.id for item in Skill)) == len(Skill)
    assert len(set(item.id for item in Activity)) == len(Activity)
