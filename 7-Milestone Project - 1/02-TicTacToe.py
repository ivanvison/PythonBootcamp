#2 players should be able to play the game
# numpad
#7 8 9
#4 5 6
#1 2 3
# clear output

import random
import os
os.system('cls')

# Step 1: Write a function that can print out a board. Set up your board as a list,
# where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

def display_board(board):
    print('\n\n')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'.
# Think about using while loops to continually ask until you get a correct answer.
# IV Note: My Addition, ask the name to provide personalization
def player_input():
    player1_name = ''
    player2_name = ''
    marks = ''

    print('Hello Players!!! How should I call you?')
    
    while player1_name == '':
        player1_name = input('Player 1, please enter a name: ')

    while player2_name == '':
        player2_name = input('Player 2, please enter a name: ') 

    while marks == '':
        player1_mark = input(f'{player1_name}, please enter your mark (X or O): ')
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

# PERSONAL ADDITION - Flip a coin to determine who will start
# (This is a personal addition to the test. Not originally in the requirements)
# Please note that Step 5 had a similar request than this.
def flip_coin(player1_name,player2_name):
    print("\nLet's flip a coin to see who will start!" )
    coin = ['H','T']
    coin_result = ''
    p1_choice = 'wrong'

    while p1_choice == 'wrong':
        p1_choice = input(f'{player1_name}, please select Heads (H) or Tails (T): ')
        
        if p1_choice != 'H' and p1_choice != 'T':
            print("This side of the coin doesn't exists!. Please choose Heads (H) or Tails (T)")
            p1_choice == 'wrong'

    coin_result = random.choice(coin)
    print(f"Result of the coin: {coin_result}")

    if coin_result == p1_choice:
        print(f'Congrats {player1_name}!! You will start the game!')
        starter = 'P1'
    else:
        print(f'Congrats {player2_name}!! You will start the game!')
        starter = 'P2'

    return starter


# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.



# Step 4: Write a function that takes in a board and a mark (X or O) and then checks
# to see if that mark has won.


# Step 5: Write a function that uses the random module to randomly decide which player goes first.
# You may want to lookup random.randint() Return a string of which player went first.


# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.


# Step 7: Write a function that checks if the board is full and returns a boolean value.
# True if full, False otherwise.


# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses
# the function from step 6 to check if it's a free position. If it is, then return the position for later use.


# Step 9: Write a function that asks the player if they want to play again and returns a boolean
# True if they do want to play again.

# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

print('Welcome to Tic Tac Toe!')

board = ['#','X','X','X','O','O','O','O','O','O']
display_board(board)
player1_name,player1_mark,player2_name,player2_mark = player_input()
starter = flip_coin(player1_name,player2_name)
