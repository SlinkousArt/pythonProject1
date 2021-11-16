import random
import os
from autocorrect import Speller
from time import sleep

spell = Speller()

# class RPSItem:
#     def __init__(self, wins):
#         self.wins = wins
#
#
# Rock = RPSItem(["Scissors"])
# Paper = RPSItem(["Rock"])
# Scissors = RPSItem(["Paper"])
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


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


ValidChoices = ['Rock', 'Paper', 'Scissors']
# ValidChoices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


def game():
    global wins, ties, losses
    playerChoice = "Error"
    while playerChoice not in ValidChoices:
        print('Choose one of the below:\n', ', '.join(ValidChoices))
        playerChoice = spell(input('')).capitalize()
        if playerChoice not in ValidChoices:
            print('Invalid choice, try again')
            sleep(1)
        clear()
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
    print('You chose', playerChoice, "\nThe computer chose", compChoice)
    print(Messages[result])


wins = ties = losses = 0
playing = True
while playing:
    game()
    playAgain = "z"
    while playAgain not in ["y", "n"]:
        print('Play Again?')
        playAgain = (input().lower() + 'z')[0]
        if playAgain not in ["y", "n"]:
            print(Messages["Invalid"])
    if playAgain in "y":
        playing = True
    else:
        playing = False
    clear()


print('Final Scores:\nWins:', wins, "\nLosses:", losses, 'Ties:', ties)
