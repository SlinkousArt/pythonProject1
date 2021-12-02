import json
from os import path


if path.exists('stats.json') is False:
    x = {
        "slinkous": {
            "wins": 0,
            "ties": 0,
            "losses": 0
        }
    }
    with open('stats.json', "w", encoding='utf-8') as f:
        json.dump(x, f, ensure_ascii=False, indent=4)


username = input('input your username\n')
with open('stats.json', 'r', encoding='utf-8') as infile:
    globalStats = json.load(infile)

userStats = globalStats[username]
stat = input('choose what to change')
new = int(input('input the stat to change'))
userStats[stat] = new

with open('stats.json', 'w', encoding='utf-8') as f:
    json.dump(globalStats, f, ensure_ascii=False, indent=4)
