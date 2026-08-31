# Example output of HCIM leaderboards for Woodcutting and COX.
#
# Top 5 Woodcutting for HCIM:
#      1  RPV                   lvl 99   xp 200,000,000
#      2  Turbo Blade           lvl 99   xp 200,000,000
#      3  Mikki                 lvl 99   xp 200,000,000
#      4  ZebraDontGo           lvl 99   xp 200,000,000
#      5  Lydia Kenney          lvl 99   xp 200,000,000
#
# Top 10 Chambers of Xeric for HCIM:
#      1  Visibly Lit           score 4,731
#      2  Tekton Vasa           score 2,964
#      3  HC T Swift            score 2,680
#      4  Miwi                  score 2,500
#      5  Zuropean              score 2,432
#      6  AriSlash              score 2,424
#      7  Tick Lag              score 2,378
#      8  apina                 score 2,341
#      9  Hard ROCKET           score 2,262
#     10  Never Deadge          score 2,196

from osrs_lib_hiscores import AccountType, Activity, HiscoreClient, Skill

client = HiscoreClient()

print("3rd page Woodcutting for HCIM, limited to top 5:")
for row in client.get(AccountType.HARDCORE_IRONMAN, Skill.WOODCUTTING, 3)[:5]:
    print(f"{row.rank:>6}  {row.player:<20}  lvl {row.level:<3}  xp {row.xp:,}")

print()

print("Top 10 Chambers of Xeric for HCIM:")
for row in client.get(AccountType.HARDCORE_IRONMAN, Activity.CHAMBERS_OF_XERIC)[:10]:
    print(f"{row.rank:>6}  {row.player:<20}  score {row.score:,}")
