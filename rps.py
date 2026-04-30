#rock paper scissors game
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
# print(RPS(2))
# print(RPS.ROCK)#RPS.ROCK
# print(RPS['ROCK'])#RPS.ROCK
# print(RPS.ROCK.value)#1
# sys.exit()
def rps():
    playerChoice=input('\nEnter...\n1 for rock\n2 for paper or \n3 for scissors:\n\n')
    if playerChoice not in ["1","2","3"]:
        print('You must chose a number between 1 and 3')
        return rps()
    player = int(playerChoice)

    compChoice = random.choice("123")
    comp = int(compChoice)

    
    print('\nyou chose '+str(RPS(player)).replace('RPS.','')+'.')
    print('computer chose '+ str(RPS(comp)).replace('RPS.','') +'.\n')
    

    if player == 1 and comp ==3:
        print('🥳 You win!')
    elif player == 2 and comp ==1:
        print('🥳 You win!')
    elif player == 3 and comp ==2:
        print('🥳 You win!')
    elif player == comp:
        print('😲 Its a tie!')
    else:
        print('🐍 You lose!')
    print('\n play again?')
    while True:
        playAgain =input(' \nY for yes\nQ for quit\n')
        if playAgain.lower() not in ['y','q']:
            continue
        else:
            break

    
    if playAgain.lower()=='y':
        return rps()
    else:
        print('\n🥳🥳\nThank you for playing')
        sys.exit("Bye 👋")
rps()
