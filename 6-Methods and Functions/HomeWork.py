# Please note that all of these solutions were written by me. Teacher's solutions I reviewed them in the original code and compared.
# @ homework_teacher.py

from cmath import pi
import os
os.system('cls')

def vol(rad):
    return (4/3)*pi*(rad**3)

print(vol(2))

print('---')

def ran_check(num,low,high):
    if num >= low and num <= high:
        print(f'{num} is in the range between {low} and {high}')
    else:
        print(f'{num} is NOT in the range between {low} and {high}')

ran_check(5,2,7)

print('---')

def up_low(str):
    temp = list(str)
    upper = 0
    lower = 0

    for letter in temp:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        else:
            pass
    
    print(f'No. of Upper case characters: {upper}')
    print(f'No. of Lower case characters: {lower}')

str = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(str)

print('---')

def unique_list(sample_list):
    return list(set(sample_list))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

print('---')

def multiply(numbers):
    total = 1
    
    for i in numbers:
        print(i*i)
        total = (total*i)
    
    return total

print(multiply([1,2,3,-4]))

print('---')

def palindrome(str):
#    newstr = str.split()
#    newstr.reverse()
#    newstr = "".join(newstr)
    newstr = str[::-1]

    if str == newstr:
        return True
    else:
        return False

print(palindrome('racecar racecar'))

print('---')