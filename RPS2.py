# importing
from time import sleep
import os
import random

options = {"Rock": ("Scissors"),
           "Paper": ("Rock"),
           "Scissors": ("Paper")}


# Random functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# intro
def intro():
    print('Welcome To Rock, Paper, Scissors')
    sleep(1)
    print('Coded by slinkous')
    sleep(2)
    clear()


# lets the player choose R, P, or S
def choose():
    global playerChoice
    playerChoice = input('Rock, Paper, or Scissors?')[0].lower()
    verify()


# verify that the choice is valid
def verify():
    if playerChoice not in ["r", "p", "s"]:
        print("Invalid Choice, retry")
        sleep(1)
        clear()
        choose()


# set the single character things to full words
def wordify():
    global playerChoice
    if playerChoice == "r":
        playerChoice = "Rock"
    if playerChoice == "p":
        playerChoice = "Paper"
    if playerChoice == "s":
        playerChoice = "Scissors"


# chooses for the computer
def comp_choose():
    global compChoice
    compChoice = random.choice(["Rock", "Paper", "Scissors"])


# reveal the choices
def reveal():
    print('You chose', playerChoice)
    sleep(1)
    print('The computer chose', compChoice)


# ok so this is the fun bit
def calculate():
    global result
    rock()
    paper()
    scissors()
    calc1()


def calc1():
    global result
    if compChoice == playerChoice:
        result = "Tie"
    elif compChoice in options[playerChoice]:
        result = "Human"
    else:
        result = "Computer"


def calc_score():
    global wins, losses, ties, result
    if result is "Tie":
        ties += 1
    elif result is "Human":
        wins += 1
    elif result is "Computer":
        losses += 1


def announce():
    if result is "Tie":
        print("The game resulted in a tie")
    elif result is "Human":
        print("Congratulations, you win")
    elif result is "Computer":
        print("You lost to the computer")
    else:
        print("There was an error TwT")
    # announce scores
    if doScoring is True:
        print("SCORE")
        score()


def score():
    print("Wins:", wins)
    print("Losses:", losses)
    print("Ties:", ties)


def wait():
    sleep(2)
    input("Press Enter to Continue")


def replayyn():
    global playAgain
    playAgain = input('Play Again?')[0].lower()
    checkyn()


# verify that the choice is valid
def checkyn():
    global playAgain
    if playAgain not in ["y", "n"]:
        print("Invalid option, type \"yes\" or \"no\"")
        sleep(1)
        clear()
        replayyn()


# Main Function. Run this whenever the game is to be played.
def game():
    print('Game Started')
    sleep(0.75)
    clear()
    choose()
    clear()
    wordify()
    comp_choose()
    reveal()
    calculate()
    calc_score()
    sleep(1)
    announce()
    wait()
    clear()


# random vars
playerChoice = "What's this OwO"
compChoice = "UwU"
result = "TwT"
winAgainst = tieAgainst = loseAgainst = "Error"
playAgain = "n"
playedAgain = False
doScoring = True
wins = losses = ties = 0

# clear screen, play intro
clear()
intro()

# Start the game
playNow = input("Press Enter to Start")
clear()
game()
replayyn()
while playAgain in "y":
    print('playAgain triggered')
    clear()
    game()
    replayyn()
    playedAgain = True
if playedAgain is True and doScoring is True:
    clear()
    sleep(1)
    print('Final Score:')
    score()
