# Original TIC TAC TOE test, applied some edits. 

import random
import os
os.system('cls')

# Display board
def display_board(board):
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])


# Function that handles player's names and marks
def player_input():
    player1_name = ''
    player2_name = ''
    marks = ''

    print('Hello Players!!! How should I call you?')
    
    while player1_name == '':
        player1_name = input('Player 1, please enter a name: ').upper()

    while player2_name == '':
        player2_name = input('Player 2, please enter a name: ').upper()

    while marks == '':
        player1_mark = input(f'{player1_name}, please enter your mark (X or O): ').upper()
        if player1_mark != 'X' and player1_mark != 'O':
            print('Wrong Mark. Please choose the right mark -> X or O.')
        else:
            if player1_mark == 'X':
                player2_mark = 'O'
                marks = 'Done'
            else:
                player2_mark = 'X'
                marks = 'Done'

    return (player1_name,player1_mark,player2_name,player2_mark)

# Flip a coin to determine who goes first. 
def flip_coin(player1_name,player2_name):
    print("\nLet's flip a coin to see who will start!" )
    coin = ['H','T']
    coin_result = ''
    p1_choice = 'wrong'

    while p1_choice == 'wrong':
        p1_choice = input(f'{player1_name}, please select Heads (H) or Tails (T): ').upper()
        
        if p1_choice != 'H' and p1_choice != 'T':
            print("This side of the coin doesn't exists!. Please choose Heads (H) or Tails (T)")
            p1_choice = 'wrong'

    coin_result = random.choice(coin)
    print(f"Result of the coin: {coin_result}")

    if coin_result == p1_choice:
        print(f'Congrats {player1_name}!! You will start the game!')
        starter = 'P1'
    else:
        print(f'Congrats {player2_name}!! You will start the game!')
        starter = 'P2'

    return starter


# Place Marker function takes name, mark and the board to allow the user enter a position and update the board
def place_marker(player_name, player_mark,board):
    position = 0

    while position == 0:
        position = int(input(f"\n{player_name}, please enter a position to place your '{player_mark}' from 1-9: "))
        if position not in range(1,10):
            print("Please select a correct number (1-9)")
            position = 0
        elif board[position] != ' ':
            print("Please select another position (1-9)")
            position = 0
        elif board[position] == ' ':
            board[position] = player_mark
            return board


# Win Check will go through the board looking for a winner or a tie. 
def win_check(board, p1_mark, p2_mark,game_plays):
    if (board[1] == board[2] == board[3] == p1_mark): 
        result = 'P1'
    elif (board[4] == board[5] == board[6] == p1_mark):
        result = 'P1'
    elif (board[7] == board[8] == board[9] == p1_mark):
        result = 'P1'
    elif (board[1] == board[4] == board[7] == p1_mark):
        result = 'P1'
    elif (board[2] == board[5] == board[8] == p1_mark):
        result = 'P1'
    elif (board[3] == board[6] == board[9] == p1_mark):
        result = 'P1'
    elif (board[1] == board[5] == board[9] == p1_mark):
        result = 'P1'
    elif (board[3] == board[5] == board[7] == p1_mark):
        result = 'P1'
    elif (board[1] == board[2] == board[3] == p2_mark):
        result = 'P2'
    elif (board[4] == board[5] == board[6] == p2_mark):
        result = 'P2'
    elif (board[7] == board[8] == board[9] == p2_mark):
        result = 'P2'
    elif (board[1] == board[4] == board[7] == p2_mark):
        result = 'P2'
    elif (board[2] == board[5] == board[8] == p2_mark):
        result = 'P2'
    elif (board[3] == board[6] == board[9] == p2_mark):
        result = 'P2'
    elif (board[1] == board[5] == board[9] == p2_mark):
        result = 'P2'
    elif (board[3] == board[5] == board[7] == p2_mark):
        result = 'P2'
    else:
        result = ''
    
    if result == '' and game_plays == 9:
        print("\nThis is a TIE!")
        result = 'None'
    elif result != '':
        print(f"\nWinner is {result}")

    return result

# Replay function asks users if they want to continue playing or not.
def replay():
    choice = ''
    
    while choice == '':
        choice = input(f'Would you like to play again? (Y) Yes / (N) No: ').upper()
    
        if choice != 'Y' and choice != 'N':
            print("Please select a correct option - (Y) Yes / (N) No")
            choice = ''
        elif choice == 'Y':
            print('\n\n')
            return True
        else:
            print(f'\n\nThank you for playing!!! Come back soon!!')
            return False        

# Main code. Putting everything together.
print('Welcome to Tic Tac Toe!')
game_on = True

# While runs while players want to keep on playing. 
while game_on == True:
    winner = ''
    game_plays = 0
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    player1_name,player1_mark,player2_name,player2_mark = player_input()
    next_play = flip_coin(player1_name,player2_name)

    # Loop in charge of handling next player, counting plays, checking for a winner and replays
    while winner == '':
        if next_play == 'P1':
            board = place_marker(player1_name, player1_mark,board)
            next_play = 'P2'
        elif next_play == 'P2':
            board = place_marker(player2_name, player2_mark,board)
            next_play = 'P1'

        game_plays += 1
        display_board(board)
        winner = win_check(board,player1_mark,player2_mark,game_plays)

    game_on = replay()





