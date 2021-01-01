#########################################################################################
#Print out remaining index values nested in a gme_board
def print_board_remaining():
    print('Remaining index positions:')
    print(f'\n {game_board[0]} | {game_board[1]} | {game_board[2]}\n-----------\n {game_board[3]} | {game_board[4]} | {game_board[5]}\n-----------\n {game_board[6]} | {game_board[7]} | {game_board[8]}\n')

#########################################################################################
#Takes users input if its correct returns it.
def user_mark_input():
    
    index_number_list=game_board
    index_number='missing'
    
    while index_number not in index_number_list or index_number=='X' or index_number=='O':
        
        if index_number not in index_number_list or index_number=='X' or index_number=='O':
            print_board_remaining()
            index_number=input('Please provide index number of your move: ')
            clear_output()
            
        if index_number not in index_number_list or index_number=='X' or index_number=='O':
            print('Wrong index number.')
    
    return int(index_number)

#########################################################################################
#Function that applies users input to a game_board. Needs turn +=1 in each playar move.
def applying_user_input():

    # IF Player X's turn, change index number in gameboard
    if turn%2==0:
        game_board[int(index_number)-1]=' '
        printed_board[int(index_number)-1]='X'
        
    # IF Player O's turn, change index number in gameboard to 'O'
    if turn%2==1:
        game_board[int(index_number)-1]=' '
        printed_board[int(index_number)-1]='O'
    
    return game_board

#########################################################################################
#Function that Prints Actuall Tic Tac Toe Game Board 
def print_board():
    i=-1
    for x in printed_board:
        i+=1
        if x.isdigit():
            printed_board[i]=' '
    clear_output()
    print(f'\n {printed_board[0]} | {printed_board[1]} | {printed_board[2]}\n-----------\n {printed_board[3]} | {printed_board[4]} | {printed_board[5]}\n-----------\n {printed_board[6]} | {printed_board[7]} | {printed_board[8]}\n')

#########################################################################################
#Function that decides who starts the game 'X' or 'O'. Needs turn +=1 in each 
def who_starts():
    turn=[0,1]
    random.shuffle(turn)
    if turn[0]==0:
        print("Player 'O' starts the game.")
    if turn[0]==1:
        print("Player 'X' starts the game.")
    return turn[0]

#########################################################################################
#Function that checks if won and who won 
def if_won():
    
    if printed_board[0]==printed_board[1]==printed_board[2]!=' ' or printed_board[3]==printed_board[4]==printed_board[5]!=' ' or printed_board[6]==printed_board[7]==printed_board[8]!=' ' or printed_board[0]==printed_board[3]==printed_board[6]!=' ' or printed_board[1]==printed_board[4]==printed_board[7]!=' ' or printed_board[2]==printed_board[5]==printed_board[8]!=' ' or printed_board[0]==printed_board[4]==printed_board[8]!=' ' or printed_board[2]==printed_board[4]==printed_board[6]!=' ':
        if turn%2==0:
            print(f'Player X won! Congratulations!')
        else:
            print(f'Player O won! Congratulations!')
        return True

    if ' ' not in printed_board:
        print(f'There is no winner this time! GG!')
        return True

    return False

#########################################################################################
#Checking if player wants to play another game
def wanna_play_check():
    xyz=''
    while xyz.lower() not in ['y','n']:
        
        if xyz.lower() not in ['y','n']:
            xyz=input('This the end of the game. Do you want to play one more time? Y or N: ')
            clear_output()

        if xyz.lower() not in ['y','n']:
            print('Wrong input.')
        else:
            if xyz.lower()=='y':
                return True
            else:
                return False

#########################################################################################
#Checking if players are ready to play
def are_you_ready():
    xyz=''
    while xyz.lower() not in ['y','"y"']:
        
        if xyz.lower() not in ['y','"y"']:
            xyz=input('Please decide who of you is "O" and who is "X".\nIf ready type "Y". Ready? ')
            clear_output()

        if xyz.lower() not in ['y','"y"']:
            print('\nWrong input or you are not ready yet. Type "Y" when ready.')

#########################################################################################
#Cleaning whole console
def clean_console():
        clear = lambda: os.system('cls')
        clear()

#########################################################################################
#########################################################################################
#TIC TAC TOE GAME

#########################################################################################
#Importing modules
from IPython.display import clear_output
import os
import random

#Cleanning console
clean_console()

#Intro to the game and first loop
wanna_play=True
print('\nYou are about to play Hot-seat Tic Tac Toe Game for 2 players.')

while wanna_play:

    #Checking if players are ready.
    are_you_ready()

    #Cleanning console
    clean_console()

    #Setting Variables
    won=False
    game_board=['1','2','3','4','5','6','7','8','9']
    printed_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

    # Drawing who starts the game.
    turn=who_starts()

    while won==False:

        #Changing player's turn
        turn+=1
        
        #Getting user's input.
        index_number=user_mark_input()

        #Applying user's iput.
        game_board=applying_user_input()
        
        #Cleanning console
        clean_console()

        #Printing out current game_board
        print_board()

        # Cheking if someone already won
        won=if_won()

    #Asking player if he wants to play one more time
    wanna_play=wanna_play_check()

    #Cleanning console
    clean_console()

print('Thanks for playing. It was a pleasure.')