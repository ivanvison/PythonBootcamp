import os
os.system('cls')

def user_choice():
    #VARIABLES
    
    #Initial
    choice = 'Wrong'
    acceptable_values = range(0,10)
    within_range = False

    #TWO CONDITIONS TO CHECK
    # DIGIT OR WITHIN RANGE == FALSE
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")

        #DIGIT CHECK
        if choice.isdigit() == False:
            print("Sorry, wrong value")

        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_values:
                within_range = True
            else:
                print('Out of acceptable range (0-10)')
                within_range = False

    return int(choice)

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

display(row1,row2,row3)

position_index = user_choice()
print(position_index)