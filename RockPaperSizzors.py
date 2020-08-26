'''
Created: August 21, 2020
Author: Brittany Hughes
Description: Creates a game of rock paper sizzors against the computer. There are three rounds in total
'''

import random

#----------Global Variables---------
listChoice = (['rock', 'paper', 'sizzors'])
Computer_Choice = ''
playerChoice = ''

round = 1
playerScore = 0
computerScore = 0

def Pick():
    global Computer_Choice
    global playerChoice
    global listChoice
    global round

    print(f'Round {round}')
    playerChoice = input('Choose from : Rock / Paper/ Sizzors')
    playerChoice = playerChoice.lower()
    if(playerChoice == 'rock' or playerChoice == 'paper' or playerChoice == 'sizzors'):
        pass
    else:
        print('ERROR INVALID INPUT')
        Pick()
    Computer_Choice = random.choice(listChoice)
    print(f'You chose {playerChoice}')
    print(f'The computer chose {Computer_Choice}')
    whoWon(playerChoice, Computer_Choice)
    return

def whoWon(humanChoice, AIchoice):
    global round
    global playerScore
    global computerScore

    if humanChoice == AIchoice:
        print('Tie')
    elif humanChoice == 'paper' and AIchoice == 'rock':
        playerScore = playerScore + 1
        print('YOU WIN')

    elif humanChoice == 'sizzors' and AIchoice == 'paper':
        playerScore = playerScore + 1
        print('YOU WIN')

    elif humanChoice == 'rock' and AIchoice == 'sizzors':
        playerScore = playerScore + 1
        print('YOU WIN')
    else:
        computerScore = computerScore + 1
        print('COMPUTER WINS')
    round = round + 1
    print(f'The score is Player:{playerScore} , Computer: {computerScore}')


def play(): #begin game with the player
    print('Welcome to rock paper sizzors! Human goes first')
    Pick()
    return

play()
while round < 4:
    Pick()