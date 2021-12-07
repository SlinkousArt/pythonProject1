import json
from os import path
import random


RPSItems = {"Rock": ["Scissors", "Lizard"],
            "Paper": ["Rock", "Spock"],
            "Scissors": ["Paper", "Lizard"],
            "Lizard": ["Paper", "Spock"],
            "Spock": ["Rock", "Scissors"]
            }
Messages = {
    "Tie": "The game resulted in a tie",
    "Human": "You win!",
    "Computer": "You lost to the computer",
    "Invalid": "Invalid input, try again"
}
ValidChoices = ['Rock', 'Paper', 'Scissors']


def game():
    global wins, ties, losses, ChoiceMessage, ResultMessage
    playerChoice = 'test'
    compChoice = random.choice(ValidChoices)
    if playerChoice in compChoice:
        result = 'Tie'
        ties += 1
    elif compChoice in RPSItems[playerChoice]:
        result = 'Human'
        wins += 1
    else:
        result = 'Computer'
        losses += 1
    ChoiceMessage = ('You chose', playerChoice, "\nThe computer chose", compChoice)
    ResultMessage = (Messages[result])

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
wins = userStats['wins']
ties = userStats['ties']
losses = userStats['losses']

game()

userStats['wins'] = wins
userStats['ties'] = ties
userStats['losses'] = losses

write(toWrite=globalStats)
