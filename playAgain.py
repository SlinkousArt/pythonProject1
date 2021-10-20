def game():
    #this is where you put the game
    print('pretend you\'re playing the game')


game()

playAgain = input('type "Y" to play again')

while playAgain == 'Y' or playAgain == 'y':
    game()
    playAgain = input('type "Y" to play again')

