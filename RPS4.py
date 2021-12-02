import json
from os import path


def write(toWrite):
    with open('stats.json', 'w', encoding='utf-8') as f:
        json.dump(toWrite, f, ensure_ascii=False, indent=4)


username = input('input your username\n')
if path.exists('stats.json') is False:
    x = {
        username: {
            "wins": 0,
            "ties": 0,
            "losses": 0
        }
    }
    write(toWrite=x)


with open('stats.json', 'r', encoding='utf-8') as infile:
    globalStats = json.load(infile)

if username not in globalStats:
    globalStats[username] = {
        "wins": 0,
        "ties": 0,
        "losses": 0
    }
    write(toWrite=globalStats)

userStats = globalStats[username]
stat = input('choose what to change')
new = int(input('input the stat to change'))
userStats[stat] = new

write(toWrite=globalStats)