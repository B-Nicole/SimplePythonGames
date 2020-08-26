'''
This is where the user will choose what game they want to play through the bot
'''
import os

def chooseAGameToPlay():
    print('Welcome! Choose a game:\n')
    choice = int(input('[1] Rock Paper Sizzors / [2] BlackJack / [3] Guess A Number / [0] EXIT'))

    if choice == 0:
        print("Exiting")
        exit()
    elif choice == 1:
        os.system(" python RockPaperSizzors.py")
    elif choice == 2:
        os.system(" python BlackJack.py")
    elif choice == 3:
        os.system(" python GuessANumber.py")
    else:
        print("Error invalid input....Exiting")
        exit()

