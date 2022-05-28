from doctest import Example
import os
from tabnanny import check
os.system('cls')
from random import shuffle

#example = [1,3,4,5,6,7,8,9]
##shuffle(example)
#print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number (0, 1 or 2): ")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("CORRECT!!!")
    else:
        print("Wrong Guess!")

    print(mylist)

#result = shuffle_list(example)
#print(result)

#INITIAL LIST
mylist = [' ','O',' ']

#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixedup_list,guess)


