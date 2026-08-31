# Example output for player 'woox'
#
# Player: woox

# Skill structure:
# PlayerSkill(id=0, name='Overall', rank=77169, level=2340, xp=508119231)
# PlayerSkill(id=1, name='Attack', rank=61190, level=99, xp=26062012)
# PlayerSkill(id=2, name='Defence', rank=36063, level=99, xp=25478462)

# Activity structure:
# PlayerActivity(id=20, name='Abyssal Sire', rank=242272, score=100)
# PlayerActivity(id=21, name='Alchemical Hydra', rank=226604, score=176)
# PlayerActivity(id=22, name='Amoxliatl', rank=201413, score=26)

# Amoxliatl data:
#   id   : 22
#   name : Amoxliatl
#   rank : 201,413
#   kc   : 26

# Top skills by rank:
#   Agility         lvl 99  rank 16,033 xp 15,176,911
#   Runecraft       lvl 99  rank 30,817 xp 14,386,618
#   Defence         lvl 99  rank 36,063 xp 25,478,462
#   Construction    lvl 99  rank 36,135 xp 13,402,037
#   Hunter          lvl 99  rank 44,475 xp 15,556,190

# Clue scroll activities:
#   Clue Scrolls (all)     rank 643,590 kc 84
#   Clue Scrolls (easy)    rank 836,521 kc 6
#   Clue Scrolls (medium)  rank 773,713 kc 11
#   Clue Scrolls (hard)    rank 863,326 kc 10
#   Clue Scrolls (elite)   rank 125,316 kc 48
#   Clue Scrolls (master)  rank 222,179 kc 9

from osrs_lib_hiscores import AccountType, Activity, HiscoreClient

client = HiscoreClient()
player = client.get(AccountType.NORMAL, "woox")

print(f"Player: {player.player}")

print()
print("Skill structure:")
for skill in list(player.skills.values())[:3]:
    print(skill)

print()
print("Activity structure:")
for activity in list(player.activities.values())[20:23]:
    print(activity)

print()
print("Amoxliatl data:")
activity = player.activities[Activity.AMOXLIATL]
print("  id   :", activity.id)
print("  name :", activity.name)
print("  rank :", f"{activity.rank:,}")
print("  kc   :", activity.score)

print()
print("Top skills by rank:")
for skill in sorted(player.skills.values(), key=lambda s: s.rank)[:5]:
    print(
        f"  {skill.name:<15} lvl {skill.level:<3} rank {skill.rank:,} xp {skill.xp:,}"
    )


clue_activities = {
    Activity.CLUE_SCROLLS_ALL.label,
    Activity.CLUE_SCROLLS_BEGINNER.label,
    Activity.CLUE_SCROLLS_EASY.label,
    Activity.CLUE_SCROLLS_MEDIUM.label,
    Activity.CLUE_SCROLLS_HARD.label,
    Activity.CLUE_SCROLLS_ELITE.label,
    Activity.CLUE_SCROLLS_MASTER.label,
}

print()
print("Clue scroll activities:")
for activity in player.activities.values():
    if activity.name in clue_activities and activity.score > 0:
        print(f"  {activity.name:<22} rank {activity.rank:,} kc {activity.score:,}")
