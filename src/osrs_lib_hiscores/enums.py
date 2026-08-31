from enum import Enum


class AccountType(Enum):
    """Account types supported for hiscore/profile lookups."""

    NORMAL = "Normal"
    IRONMAN = "Ironman"
    HARDCORE_IRONMAN = "Hardcore Ironman"
    ULTIMATE_IRONMAN = "Ultimate Ironman"
    DEADMAN = "Deadman"
    SEASONAL = "Seasonal"

    def __init__(self, label: str) -> None:
        """Store label for the account type."""
        self.label = label


class Skill(Enum):
    """Skills with numeric IDs and display labels."""

    OVERALL = (0, "Overall")
    ATTACK = (1, "Attack")
    DEFENCE = (2, "Defence")
    STRENGTH = (3, "Strength")
    HITPOINTS = (4, "Hitpoints")
    RANGED = (5, "Ranged")
    PRAYER = (6, "Prayer")
    MAGIC = (7, "Magic")
    COOKING = (8, "Cooking")
    WOODCUTTING = (9, "Woodcutting")
    FLETCHING = (10, "Fletching")
    FISHING = (11, "Fishing")
    FIREMAKING = (12, "Firemaking")
    CRAFTING = (13, "Crafting")
    SMITHING = (14, "Smithing")
    MINING = (15, "Mining")
    HERBLORE = (16, "Herblore")
    AGILITY = (17, "Agility")
    THIEVING = (18, "Thieving")
    SLAYER = (19, "Slayer")
    FARMING = (20, "Farming")
    RUNECRAFT = (21, "Runecraft")
    HUNTER = (22, "Hunter")
    CONSTRUCTION = (23, "Construction")
    SAILING = (24, "Sailing")

    def __init__(self, id: int, label: str) -> None:
        """Store the ID and label for the skill."""
        self.id = id
        self.label = label


class Activity(Enum):
    """Activities with numeric IDs and display labels."""

    GRID_POINTS = (0, "Grid Points")
    LEAGUE_POINTS = (1, "League Points")
    DEADMAN_POINTS = (2, "Deadman Points")
    BOUNTY_HUNTER_HUNTER = (3, "Bounty Hunter - Hunter")
    BOUNTY_HUNTER_ROGUE = (4, "Bounty Hunter - Rogue")
    BOUNTY_HUNTER_LEGACY_HUNTER = (5, "Bounty Hunter (Legacy) - Hunter")
    BOUNTY_HUNTER_LEGACY_ROGUE = (6, "Bounty Hunter (Legacy) - Rogue")
    CLUE_SCROLLS_ALL = (7, "Clue Scrolls (all)")
    CLUE_SCROLLS_BEGINNER = (8, "Clue Scrolls (beginner)")
    CLUE_SCROLLS_EASY = (9, "Clue Scrolls (easy)")
    CLUE_SCROLLS_MEDIUM = (10, "Clue Scrolls (medium)")
    CLUE_SCROLLS_HARD = (11, "Clue Scrolls (hard)")
    CLUE_SCROLLS_ELITE = (12, "Clue Scrolls (elite)")
    CLUE_SCROLLS_MASTER = (13, "Clue Scrolls (master)")
    LMS_RANK = (14, "LMS - Rank")
    PVP_ARENA_RANK = (15, "PvP Arena - Rank")
    SOUL_WARS_ZEAL = (16, "Soul Wars Zeal")
    RIFTS_CLOSED = (17, "Rifts closed")
    COLOSSEUM_GLORY = (18, "Colosseum Glory")
    COLLECTIONS_LOGGED = (19, "Collections Logged")
    ABYSSAL_SIRE = (20, "Abyssal Sire")
    ALCHEMICAL_HYDRA = (21, "Alchemical Hydra")
    AMOXLIATL = (22, "Amoxliatl")
    ARAXXOR = (23, "Araxxor")
    ARTIO = (24, "Artio")
    BARROWS_CHESTS = (25, "Barrows Chests")
    BRUTUS = (26, "Brutus")
    BRYOPHYTA = (27, "Bryophyta")
    CALLISTO = (28, "Callisto")
    CALVARION = (29, "Calvar'ion")
    CERBERUS = (30, "Cerberus")
    CHAMBERS_OF_XERIC = (31, "Chambers of Xeric")
    CHAMBERS_OF_XERIC_CHALLENGE_MODE = (32, "Chambers of Xeric: Challenge Mode")
    CHAOS_ELEMENTAL = (33, "Chaos Elemental")
    CHAOS_FANATIC = (34, "Chaos Fanatic")
    COMMANDER_ZILYANA = (35, "Commander Zilyana")
    CORPOREAL_BEAST = (36, "Corporeal Beast")
    CRAZY_ARCHAEOLOGIST = (37, "Crazy Archaeologist")
    DAGANNOTH_PRIME = (38, "Dagannoth Prime")
    DAGANNOTH_REX = (39, "Dagannoth Rex")
    DAGANNOTH_SUPREME = (40, "Dagannoth Supreme")
    DERANGED_ARCHAEOLOGIST = (41, "Deranged Archaeologist")
    DOOM_OF_MOKHAIOTL = (42, "Doom of Mokhaiotl")
    DUKE_SUCELLUS = (43, "Duke Sucellus")
    GENERAL_GRAARDOR = (44, "General Graardor")
    GIANT_MOLE = (45, "Giant Mole")
    GROTESQUE_GUARDIANS = (46, "Grotesque Guardians")
    HESPORI = (47, "Hespori")
    KALPHITE_QUEEN = (48, "Kalphite Queen")
    KING_BLACK_DRAGON = (49, "King Black Dragon")
    KRAKEN = (50, "Kraken")
    KREEARRA = (51, "Kree'Arra")
    KRIL_TSUTSAROTH = (52, "K'ril Tsutsaroth")
    LUNAR_CHESTS = (53, "Lunar Chests")
    MAD_ANGEL = (54, "Mad Angel")
    MAGGOT_KING = (55, "Maggot King")
    MIMIC = (56, "Mimic")
    NEX = (57, "Nex")
    NIGHTMARE = (58, "Nightmare")
    PHOSANIS_NIGHTMARE = (59, "Phosani's Nightmare")
    OBOR = (60, "Obor")
    PHANTOM_MUSPAH = (61, "Phantom Muspah")
    SARACHNIS = (62, "Sarachnis")
    SCORPIA = (63, "Scorpia")
    SCURRIUS = (64, "Scurrius")
    SHELLBANE_GRYPHON = (65, "Shellbane Gryphon")
    SKOTIZO = (66, "Skotizo")
    SOL_HEREDIT = (67, "Sol Heredit")
    SPINDEL = (68, "Spindel")
    TEMPOROSS = (69, "Tempoross")
    THE_GAUNTLET = (70, "The Gauntlet")
    THE_CORRUPTED_GAUNTLET = (71, "The Corrupted Gauntlet")
    THE_HUEYCOATL = (72, "The Hueycoatl")
    THE_LEVIATHAN = (73, "The Leviathan")
    THE_ROYAL_TITANS = (74, "The Royal Titans")
    THE_WHISPERER = (75, "The Whisperer")
    THEATRE_OF_BLOOD = (76, "Theatre of Blood")
    THEATRE_OF_BLOOD_HARD_MODE = (77, "Theatre of Blood: Hard Mode")
    THERMONUCLEAR_SMOKE_DEVIL = (78, "Thermonuclear Smoke Devil")
    TOMBS_OF_AMASCUT = (79, "Tombs of Amascut")
    TOMBS_OF_AMASCUT_EXPERT_MODE = (80, "Tombs of Amascut: Expert Mode")
    TZKAL_ZUK = (81, "TzKal-Zuk")
    TZTOK_JAD = (82, "TzTok-Jad")
    VARDORVIS = (83, "Vardorvis")
    VENENATIS = (84, "Venenatis")
    VETION = (85, "Vet'ion")
    VORKATH = (86, "Vorkath")
    WINTERTODT = (87, "Wintertodt")
    YAMA = (88, "Yama")
    ZALCANO = (89, "Zalcano")
    ZULRAH = (90, "Zulrah")

    def __init__(self, id: int, label: str) -> None:
        """Store the ID and label for the activity."""
        self.id = id
        self.label = label
