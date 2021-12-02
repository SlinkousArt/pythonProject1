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

with open('stats.json') as infile:
    globalStats = json.load(infile)


username = input('input your username\n')
what = input('what would you like to check?\n')

userStats = globalStats[username]

print(userStats[what])
