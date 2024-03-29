# Please note that all of these solutions were written by me. Teacher's solutions I reviewed them in the original code and compared.
# @ Exercise2_teacher.py

import os
from pyparsing import Or
os.system('cls')

#  WARMUP SECTION

# LESSER OF TWO EVENS: Write a function that returns the lesser
#  of two given numbers if both numbers are even, but returns the
#  greater if one or both numbers are odd

def lesser_of_two(num1,num2):
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        if num1 < num2:
            print(num1)
        else:
            print(num2)
    else:
        if num1 > num2:
            print(num1)
        else:
            print(num2)

lesser_of_two(9,5)

print('------------------------------')

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(str1):
    words = str1.split()

    if words[0][0] == words[1][0]:
        return True
    else:
        return False

print(animal_crackers('Aguila Cat'))

print('------------------------------')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
#  or if one of the integers is 20. If not, return False
def makes_twenty(num1, num2):
    if (num1 + num2 == 20) or (num1 == 20) or (num2 == 20):
        return True
    else:
        return False

print(makes_twenty(5,5))

print('------------------------------')

# LEVEL 1

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    temp = list(name)
    temp[0] = temp[0].upper()
    temp[3] = temp[3].upper()
    name = "".join(temp)
    return name

print(old_macdonald('macdonald'))

print('------------------------------')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(str):
    temp = str.split()
    temp.reverse()
    temp = " ".join(temp)
    return temp

print(master_yoda('I am home'))
print(master_yoda('Benjamin Vison Leon'))

print('------------------------------')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(num):
    if (num >=90 and num <= 110) or (num >=190 and num <= 210):
        return True
    else:
        return False

print(almost_there(111))

print('------------------------------')

# LEVEL 2

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(numlist):
    elements = len(numlist)
    # print(elements)
    count = 0
    for i in numlist:
        if (i == 3) and (count <= elements-1):
            if (numlist[count+1] == 3):
                return True
        count += 1 
    
    return False

numlist = [2,1,3,2,1,7,8,9,3,3,3,1,2,4,3,0]
print(numlist)
print(has_33(numlist))

print('------------------------------')

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(str):
    temp = list(str)
    print(temp)
    i = 0
    for letter in temp:
        temp[i] = 3*(letter)
        i += 1

    str = "".join(temp)
    return str

print(paper_doll('Hello'))

print('------------------------------')

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum
# (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    if (a <= 0 or a > 11) or (b <= 0 or b > 11) or (c <= 0 or c > 11):
        return 'Please check Numbers.'

    sum = a+b+c
    if (sum <= 21):
        return sum
    else:
        if (a == 11 or b == 11 or c == 11):
            sum = sum - 10
            if (sum <= 21):
                return sum                
        return 'BUST'

print(blackjack(9,11,9))

print('------------------------------')

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
def summer_69(arr):
    pass

print(summer_69([4, 5, 6, 7, 8, 9]))

