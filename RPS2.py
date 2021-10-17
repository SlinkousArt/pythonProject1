# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import random

# Where the player chooses
# playerIn = input("Rock, Paper, or Scissors?")
# friendliness

# import time
# def functionThing(number):
#     for owo in range(number):
#         print(owo + 1)
#         # time.sleep(1)
#
# howMany = int(input("howMany"))
#
# functionThing(number=howMany)

# importing
from time import sleep
import os
import random
# import sys
# import curses


# Curses setup
# curses.initscr()

# Random functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Typewriter effect
# def typewrite(text):
#     for letter in text:
#         sys.stdout.write(letter)
#         sys.stdout.flush()
#         sleep(0.1)


# nope
def tutorial():
    print('This is literally a game of rock paper scissors, played against the computer.')
    print('I\'m too lazy to explain rock paper scissors, go look it up')


# intro
def intro():
    print('Welcome To Rock, Paper, Scissors')
    sleep(1)
    print('Coded by slinkous')
    sleep(2)
    clear()


# lets the player choose R, P, or S
def choose():
    choice = input('Rock, Paper, or Scissors?')
    global playerChoice
    playerChoice = choice[0].lower()
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
    print("0-0")
    global result
    if playerChoice == compChoice:
        result = "Tie"
#    else:
#        print('aaand this is the hard part. -_-')


def announce():
    if result is "Tie":
        print("The game resulted in a tie")
    elif result is "Human":
        print("Congratulations, you win")
    elif result is "Computer":
        print("You lost to the computer")
#    else:
#        print("There was an error TwT")
    # announce scores
    if doScoring is True:
        print("SCORE")
        print("Wins:", wins)
        print("Losses:", losses)
        print("Ties:", ties)


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
    announce()


# random vars
playerChoice = "What's this OwO"
compChoice = "UwU"
result = "TwT"
# Scoring, not yet implemented
doScoring = False

wins = losses = ties = 0

# clears the screen to start
clear()

# intro
intro()

# Start
playNow = input("Press Enter to Start")
clear()
game()
