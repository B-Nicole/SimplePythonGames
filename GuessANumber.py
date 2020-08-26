'''
Author: Brittany Hughes
Date: August 22, 2020

A game where the computer gives the user a range of numbers to guess from
The user has 4 chances to guess the correct number
The computer will give hints if the user is too high or too low.
The user can have a hint. The hint given will be if the number is either even or odd
'''


import random
#________Global Variables__________
guess = 1
remainingNumberOfGuesses = 4
continuePlaying = True

def playGame():
    global rounds
    #have computer pick a number
    print('The computer has chosen the number.')
    gameLoop(computerNumber)

def guess():
    global guess, computerNumber
    if computerNumber % 2 == 0:
        print('The number is even')
        guess = 0
    else:
        print('The number is odd')
        guess = 0

def gameLoop(computerNumber):
    global score
    global remainingNumberOfGuesses
    global continuePlaying

    if remainingNumberOfGuesses <= 0:
        print(f'GAME OVER YOU LOOSE. The number was: {computerNumber}')
        continuePlaying = False
    if guess == 1:
        choice = input('Do you want to use a hint? y/n')
        choice = choice.lower()
        if choice == 'y':
            guess()

    playerGuess = int(input('Guess a number BETWEEN -1 and 101 (0- 100 inclusive)'))
    if playerGuess < computerNumber:
        remainingNumberOfGuesses -= 1
        print('TOO LOW')

        gameLoop()

    elif playerGuess > computerNumber:
        remainingNumberOfGuesses -=1
        print('TOO HIGH')
        gameLoop()
    else:
        score += 1
        print(f'YOU GUESSED THE NUMBER!')
        continuePlaying = False

def instructions():
    print('''
    A game where the computer gives you a range of numbers to guess from.
    The You have 4 chances to guess the correct number.
    The The computer will give hints if your guess is too high or too low.
    The You will be given one hint that can be used at any time.
    ''')
    prompt()

def prompt(): #TODO: This function will initilize the game
    print('Welcome to guess a number. Please choose an option')
    option = int(input('[1] Play Game / [2] Instructions / [3] Quit'))
    if option == 3:
        print('...EXITING')
        exit()
    elif option == 2:
        instructions()
    else:
        playGame()

prompt()
while continuePlaying == True:
    playGame()