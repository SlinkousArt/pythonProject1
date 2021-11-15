# by fishiest

# Import string and random module
import string
import random
timesPrint = 0
# Randomly choose a letter from all the ascii_letters
while True:
    randomLetterOne = random.choice(string.ascii_letters).lower()
    randomLetterTwo = random.choice(string.ascii_letters).lower()
    randomLetterThree = random.choice(string.ascii_letters).lower()
    randomLetterFour = random.choice(string.ascii_letters).lower()
    randomLetterFive = random.choice(string.ascii_letters).lower()
    randomLetterSix = random.choice(string.ascii_letters).lower()
    whatPrint = (randomLetterOne + randomLetterTwo + randomLetterThree + randomLetterFour + randomLetterFive + randomLetterSix)
    print(whatPrint)
    timesPrint += 1
    if whatPrint == "amogus":
        print("You did it in", timesPrint, "attempts!")
        break
