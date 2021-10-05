# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

PlayerChoice = input("Rock, Paper, or Scissors?")
if PlayerChoice == "rock" or PlayerChoice == "Rock" or PlayerChoice == "r" or PlayerChoice == "R":
    PlayerChoice = "Rock"
elif PlayerChoice == "paper" or PlayerChoice == "Paper" or PlayerChoice == "p" or PlayerChoice == "P":
    PlayerChoice = "Paper"
elif PlayerChoice == "scissors" or PlayerChoice == "Scissors" or PlayerChoice == "s" or PlayerChoice == "S":
    PlayerChoice = "Scissors"
if PlayerChoice != "Rock" and PlayerChoice != "Paper" and PlayerChoice != "Scissors":
    print("invalid input, relaunch the program and try again")
else:
    print("You chose " + PlayerChoice)
    print("The computer is choosing now...")
    ComputerChoice = random.choice(["Rock", "Paper", "Scissors"])
    print("The Computer Chose " + ComputerChoice)

    if PlayerChoice == ComputerChoice:
        Result = "Tie"
    elif PlayerChoice == "Rock":
        if ComputerChoice == "Scissors":
            Result = "Human"
        else:
            Result = "Computer"
    elif PlayerChoice == "Paper":
        if ComputerChoice == "Rock":
            Result = "Human"
        else:
            Result = "Computer"
    elif PlayerChoice == "Scissors":
        if ComputerChoice == "Paper":
            Result = "Human"
        else:
            Result = "Computer"

    if Result == "Tie":
        print("Tie! No winners.")
    elif Result == "Human":
        print("Congratulations, you win!")
    elif Result == "Computer":
        print("You lost to the computer.")