import random


class RPSItem:
    def __init__(self, wins):
        self.wins = wins


Rock = RPSItem(["Scissors"])
Paper = RPSItem(["Rock"])
Scissors = RPSItem(["Paper"])

playerChoice = input('rock paper or scissors')
compChoice = random.choice(["Rock", "Paper", "Scissors"])

if playerChoice is compChoice:
    result = 'Tie'
elif compChoice in

print('You chose', playerChoice, "\nThe computer chose", compChoice)
