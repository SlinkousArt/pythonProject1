
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

# Where the player chooses

PlayerChoice = input("Rock, Paper, or Scissors?")
# friendlyness
if PlayerChoice == "rock" or PlayerChoice == "Rock" or PlayerChoice == "r" or PlayerChoice == "R":
    PlayerChoice = "Rock"
elif PlayerChoice == "paper" or PlayerChoice == "Paper" or PlayerChoice == "p" or PlayerChoice == "P":
    PlayerChoice = "Paper"
elif PlayerChoice == "scissors" or PlayerChoice == "Scissors" or PlayerChoice == "s" or PlayerChoice == "S":
    PlayerChoice = "Scissors"
if PlayerChoice != "Rock" and PlayerChoice != "Paper" and PlayerChoice != "Scissors":
