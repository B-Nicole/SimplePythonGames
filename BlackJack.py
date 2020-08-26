import random

# --------- Global Variables ----------
winner = None
play = True
pick_again = False
PlayerTurn_isOver = False
playerHand = 0
num = 0

def pick_a_card():
 global playerHand
 global num
 num = random.randint(1, 11)
 print('You pulled a : ')
 print(num)
 playerHand = num + playerHand
 print('Your total is' )
 print(playerHand)
 check_if_over(playerHand)
 return

def prompt():
    global PlayerTurn_isOver
    global playerHand
    choice = input('Do you want to pick another card')
    if(choice == "Yes" or choice == "yes" or choice == "YES" or choice == "Y" or choice == "y"):
         draw_again()
    elif (choice == "No" or choice == "no" or choice == "NO" or choice == "N" or choice == "n"):
         PlayerTurn_isOver = True
         freeze(playerHand)
         stop()
    return

def draw_again(): #if the player wants to draw a card again
    pick_a_card()
    return

def check_if_over(n):
    global playerHand
    playerHand = n
    if (playerHand> 21):
        print("You loose")
        stop()
    elif (playerHand == 21):
        print("You Win!")
        stop()
    else:
        prompt()
    return
def freeze(n):
    global playerHand
    playerHand = n
    print('You stopped at')
    print(playerHand)
    return

def stop():
    print("The game is over.")
    return
def play_game(): # you pick two cards at the beginning of the game
    pick_a_card()
    return

#--------Play-------------
print("Welcome to blackJack")
play_game()