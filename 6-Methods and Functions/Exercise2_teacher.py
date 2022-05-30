import os
from pyparsing import Or
os.system('cls')

#  WARMUP SECTION

# LESSER OF TWO EVENS: Write a function that returns the lesser
#  of two given numbers if both numbers are even, but returns the
#  greater if one or both numbers are odd

def lesser_of_two(num1,num2):
    if (num1 % 2 == 0) and (num2 % 2 == 0):
        return min(num1,num2)
    else:
        return max(num1,num2)

lesser_of_two(9,5)

print('------------------------------')

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(str1):
    words = str1.split()

    return words[0][0] == words[1][0]

print(animal_crackers('Aguila Cat'))

print('------------------------------')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
#  or if one of the integers is 20. If not, return False
def makes_twenty(num1, num2):
    return (num1 + num2 == 20) or (num1 == 20) or (num2 == 20)

print(makes_twenty(5,5))

print('------------------------------')

# LEVEL 1

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'

print(old_macdonald('macdonald'))

print('------------------------------')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(str):
    return ' '.join(str.split()[::-1])

print(master_yoda('I am home'))
print(master_yoda('Benjamin Vison Leon'))

print('------------------------------')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(num):
    return ((abs(100 - num) <= 10) or (abs(200 - num) <= 10))

print(almost_there(111))

print('------------------------------')

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(0, len(nums)-1):
      
        #nicer looking alternative in commented code
        #if nums[i] == 3 and nums[i+1] == 3:
    
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False

numlist = [2,1,3,2,1,7,8,9,3,3,3,1,2,4,3,0]
print(numlist)
print(has_33(numlist))

print('------------------------------')

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(str):
    result = ''
    for char in str:
        result += char * 3
    return result

print(paper_doll('Hello'))

print('------------------------------')

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum
# (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) > 21 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

print(blackjack(9,11,9))

print('------------------------------')

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


print(summer_69([4, 5, 6, 7, 8, 9]))

print('------------------------------')

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('a')
