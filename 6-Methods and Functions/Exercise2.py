import os
from pyparsing import Or
os.system('cls')

# WARMUP SECTION

#LESSER OF TWO EVENS: Write a function that returns the lesser
# of two given numbers if both numbers are even, but returns the
# greater if one or both numbers are odd

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

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(str1):
    words = str1.split()

    if words[0][0] == words[1][0]:
        return True
    else:
        return False

print(animal_crackers('Aguila Cat'))

print('------------------------------')

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
# or if one of the integers is 20. If not, return False
def makes_twenty(num1, num2):
    if (num1 + num2 == 20) or (num1 == 20) or (num2 == 20):
        return True
    else:
        return False

print(makes_twenty(5,5))

print('------------------------------')

#LEVEL 1

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    temp = list(name)
    temp[0] = temp[0].upper()
    temp[3] = temp[3].upper()
    name = "".join(temp)
    return name

print(old_macdonald('macdonald'))

print('------------------------------')

#MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(str):
    temp = str.split()
    temp.reverse()
    temp = " ".join(temp)
    return temp

print(master_yoda('I am home'))
print(master_yoda('Benjamin Vison Leon'))

print('------------------------------')

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(num):
    if (num >=90 and num <= 110) or (num >=190 and num <= 210):
        return True
    else:
        return False

print(almost_there(111))