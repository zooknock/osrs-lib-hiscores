# osrs-lib-hiscores

A lightweight, typed Python client for scraping OSRS Hiscores data.

[![Latest Release](https://img.shields.io/github/v/release/zooknock/osrs-lib-hiscores)](https://github.com/zooknock/osrs-lib-hiscores/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue)](https://www.python.org/downloads/)


## Overview

**osrs-lib-hiscores** provides a simple, typed interface to the OSRS hiscores. Fetch individual player profiles with all their skills and activities, or retrieve ranked leaderboards across all account types.

## Installation

```
pip install git+ssh://git@github.com/zooknock/osrs-lib-hiscores.git
```

## Quick Start

``` python
from osrs_lib_hiscores import AccountType, Activity, HiscoreClient, Skill

client = HiscoreClient()

# Fetch a player's full profile
player = client.get(AccountType.ULTIMATE_IRONMAN, "Wooooo91")
print(player.skills[Skill.OVERALL])  # PlayerSkill(id=0, name='Overall', rank=1, level=2376, xp=4149988891)
print(player.activities[Activity.ABYSSAL_SIRE])  # PlayerActivity(id=20, name='Abyssal Sire', rank=242, score=100)

# Fetch skill leaderboard (25 entries per page)
top_overall = client.get(AccountType.ULTIMATE_IRONMAN, Skill.OVERALL, page=1)
for entry in top_overall:
    print(f"{entry.rank}. {entry.player} - {entry.xp:,} xp")

# Fetch activity leaderboard
top_sire = client.get(AccountType.NORMAL, Activity.ABYSSAL_SIRE, page=1)
for entry in top_sire:
    print(f"{entry.rank}. {entry.player} - {entry.score:,} kc")
```

## Usage Examples

### Get Player Data

``` python
from osrs_lib_hiscores import AccountType, HiscoreClient, Skill, Activity

client = HiscoreClient()
player = client.get(AccountType.NORMAL, "woox")

# Find top skills by rank
for skill in sorted(player.skills.values(), key=lambda s: s.rank)[:5]:
    print(f"{skill.name:<15} lvl {skill.level:<3} rank {skill.rank:,}")

# Find specific activity
clue_elite = player.activities[Activity.CLUE_SCROLLS_ELITE]
print(f"{clue_elite.name} - rank {clue_elite.rank:,}, {clue_elite.score:,} complete")
```

### Browse Leaderboards

``` python
# Third page of Woodcutting for Hardcore Ironmen
page_3_wc = client.get(AccountType.HARDCORE_IRONMAN, Skill.WOODCUTTING, page=3)

# Top 10 Chambers of Xeric completions
cox_leaders = client.get(AccountType.HARDCORE_IRONMAN, Activity.CHAMBERS_OF_XERIC, page=1)
for entry in cox_leaders[:10]:
    print(f"{entry.rank}. {entry.player} - {entry.score:,}")
```

### Explore Enums

``` python
from osrs_lib_hiscores import Skill, Activity, AccountType

# All 25 skills
for skill in Skill:
    print(f"{skill.id}: {skill.label}")

# All 91 activities
for activity in Activity:
    print(f"{activity.id}: {activity.label}")

# All supported account types
for account_type in AccountType:
    print(account_type.label)
```

## API Reference

### HiscoreClient

``` python
client = HiscoreClient(timeout=10, delay=2.0, max_retries=5)
```

#### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `timeout` | `int` | `10` | Request timeout in seconds. |
| `delay` | `float` | `2.0` | Backoff delay multiplier for retries. |
| `max_retries` | `int` | `5` | Maximum retry attempts for rate-limited or failed requests. |

#### Methods

The client provides a single unified `get()` method with overloaded signatures:

``` python
# Fetch a player profile (returns Player)
player = client.get(AccountType.NORMAL, "username")

# Fetch skill leaderboard (returns list[HiscoreSkill])
rankings = client.get(AccountType.NORMAL, Skill.OVERALL, page=1)

# Fetch activity leaderboard (returns list[HiscoreActivity])
rankings = client.get(AccountType.NORMAL, Activity.CHAMBERS_OF_XERIC, page=1)
```

### Data Models

| Model | Attributes | Description |
|-------|-----------|-------------|
| **`Player`** | `player` (str), `skills` (dict), `activities` (dict) | A player's complete profile with all skills and activities. |
| **`PlayerSkill`** | `id`, `name`, `rank`, `level`, `xp` | A player's single skill record. |
| **`PlayerActivity`** | `id`, `name`, `rank`, `score` | A player's single activity record (boss KC, clue count, etc). |
| **`HiscoreSkill`** | `rank`, `player`, `level`, `xp` | A single entry on a skill leaderboard. |
| **`HiscoreActivity`** | `rank`, `player`, `score` | A single entry on an activity leaderboard. |

### Enums

**`AccountType`** – NORMAL, IRONMAN, HARDCORE_IRONMAN, ULTIMATE_IRONMAN, DEADMAN, SEASONAL

**`Skill`** – 25 skills: OVERALL, ATTACK, DEFENCE, STRENGTH, HITPOINTS, RANGED, PRAYER, MAGIC, COOKING, WOODCUTTING, FLETCHING, FISHING, FIREMAKING, CRAFTING, SMITHING, MINING, etc.

**`Activity`** – 91 activities: LEAGUE_POINTS, BOUNTY_HUNTER, PVP_ARENA, CHAMBERS_OF_XERIC, THEATRE_OF_BLOOD, TOMBS_OF_AMASCUT, ABYSSAL_SIRE, ALCHEMICAL_HYDRA, etc.

All enums support iteration and have `.id` and `.label` attributes:

``` python
print(Skill.WOODCUTTING.id)      # 15
print(Skill.WOODCUTTING.label)   # "Woodcutting"
```

## Error Handling

All methods raise `requests.RequestException` or `Exception` with descriptive messages on failure. The client handles automatic retries for rate limits (HTTP 429) and server errors (5xx status codes).

``` python
try:
    player = client.get(AccountType.NORMAL, "NonexistentPlayer")
except Exception as e:
    print(e)  # HTTP 404: Not Found
```

### Common Errors

- **HTTP 404** – Player not found
- **HTTP 429** – Rate limited; the client automatically retries with exponential backoff
- **Network timeout** – Connection failed or took too long; adjust `timeout` parameter if needed
- **Malformed JSON** – API returned unexpected data format

### Debugging

If leaderboard scraping returns empty results, the HTML table structure may have changed. Check the `min_cells` threshold in the `_parse_hiscore_table()` method, print the raw HTML and inspect ````<td>```` cell counts to see if an adjustment is needed.

## Contributing

Contributions welcome! Please ensure all tests pass:

``` bash
task check
```

## License

TBD
