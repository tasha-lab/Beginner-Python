#rock paper scissors game
import sys
import random
from enum import Enum

def play_rps(name = 'PlayerOne'):
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

        playerChoice=input(f"\n{name} Enter...\n1 for rock\n2 for paper or \n3 for scissors:\n\n")
        if playerChoice not in ["1","2","3"]:
            print(f" {name}'Please chose a number between 1 and 3'")
            return rps()
        player = int(playerChoice)

        compChoice = random.choice("123")
        comp = int(compChoice)

        
        print(f"\n{name} you chose {str(RPS(player)).replace('RPS.','').title()}.")
        print(f"computer chose {str(RPS(comp)).replace('RPS.','').title()}.\n")
        
        def decide_winner(player,comp):
            nonlocal player_wins
            nonlocal comp_wins
            if player == 1 and comp ==3:
                player_wins+=1
                return f'{name},🥳 You win!'
            elif player == 2 and comp ==1:
                player_wins+=1
                return f'{name}🥳 You win!'
            elif player == 3 and comp ==2:
                player_wins+=1
                return f'{name}🥳 You win!'
            elif player == comp:
                return '😲 Its a tie!'
            else:
                comp_wins+=1
                return f'🐍 Comp wins!\n Try again {name}!!'
        game_result = decide_winner(player,comp)
        print(game_result)

        nonlocal game_count 
        game_count+=1

        print(f"\nGame count:{game_count}")
        print(f"\n{name} wins:{player_wins}")
        print(f"\ncomputer wins:{comp_wins}")
        print(f'\nplay again,{name}?')
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
            sys.exit(f"Bye {name}👋")
    return rps


#make the game a module
if __name__ == "__main__":
    import argparse #commandline option and argumen tparsing library

    parser = argparse.ArgumentParser(
        description='provides a personalized game experience'
    )
    parser.add_argument(
        '-n','--name',metavar='name',
        required=True,help='The name of the person to playing the game'
    )
    
    args = parser.parse_args()
    rock_paper_scissors =play_rps(args.name)
    rock_paper_scissors()