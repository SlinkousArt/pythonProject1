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
import time
import os
# import curses


# Curses setup
# curses.initscr()

# Random functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def tutorial():
    print('This is literally a game of rock paper scissors, played against the computer.')
    print('I\'m too lazy to explain rock paper scissors, go look it up')


# Main Function. Run this whenever the game is to be played.
def game():
    print('Game Started')


# intro
print('Welcome To Rock, Paper, Scissors')
time.sleep(1)
print('Coded by slinkous')
time.sleep(5)
clear()

# Start
playNow = input("Press Enter to Start")
clear()
game()
