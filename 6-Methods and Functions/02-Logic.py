import os
os.system('cls')

def even_check(number):
    return number % 2 == 0

#num = int(input('Insert a number: '))   
print(even_check(20))
#-----------------------------------------------
#Return true if any number is even inside a list

def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            print('It is even')
            return True
        else:
            pass
    return False

print(check_even_list([1,1,1]))
#-----------------------------------------------
#Return even numbers

def return_even_numbers(num_list):

    #palceholder
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

print(return_even_numbers([2,1,5,6,8,9,3,10]))