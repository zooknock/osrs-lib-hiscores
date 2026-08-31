from osrs_lib_hiscores import AccountType, Activity, HiscoreClient, Skill

# Initialise client
client = HiscoreClient()

# Get specific player data
player = client.get(AccountType.ULTIMATE_IRONMAN, "Wooooo91")
player_fishing = player.skills[Skill.FISHING]
player_sire = player.activities[Activity.ABYSSAL_SIRE]

# Get leaderboards data
hcim_slayer = client.get(AccountType.HARDCORE_IRONMAN, Skill.SLAYER, 1)
im_mediums = client.get(AccountType.IRONMAN, Activity.CLUE_SCROLLS_MEDIUM, 1)

# Access skill names
for skill in Skill:
    print(skill.label)

# Access activity names
for activity in Activity:
    print(activity.label)

# Access hiscore-supported account types
for accountType in AccountType:
    print(accountType.label)
