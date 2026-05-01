#rock paper scissors game
import sys
import random
from enum import Enum

def play_rps():
    game_count=0
    player_wins=0
    comp_wins = 0

# print(RPS(2))
# print(RPS.ROCK)#RPS.ROCK
# print(RPS['ROCK'])#RPS.ROCK
# print(RPS.ROCK.value)#1
# sys.exit()
    def rps():
        nonlocal player_wins
        nonlocal comp_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerChoice=input('\nEnter...\n1 for rock\n2 for paper or \n3 for scissors:\n\n')
        if playerChoice not in ["1","2","3"]:
            print('You must chose a number between 1 and 3')
            return rps()
        player = int(playerChoice)

        compChoice = random.choice("123")
        comp = int(compChoice)

        
        print('\nyou chose '+str(RPS(player)).replace('RPS.','')+'.')
        print('computer chose '+ str(RPS(comp)).replace('RPS.','') +'.\n')
        
        def decide_winner(player,comp):
            nonlocal player_wins
            nonlocal comp_wins
            if player == 1 and comp ==3:
                player_wins+=1
                return '🥳 You win!'
            elif player == 2 and comp ==1:
                player_wins+=1
                return '🥳 You win!'
            elif player == 3 and comp ==2:
                player_wins+=1
                return '🥳 You win!'
            elif player == comp:
                return '😲 Its a tie!'
            else:
                comp_wins+=1
                return '🐍 You lose!'
        game_result = decide_winner(player,comp)
        print(game_result)

        nonlocal game_count 
        game_count+=1

        print('\nGame count:'+str(game_count))
        print('\nPlayer wins:'+str(player_wins))
        print('\ncomputer wins:'+str(comp_wins))
        print('\nplay again?')
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
    return rps
play =play_rps()
play()