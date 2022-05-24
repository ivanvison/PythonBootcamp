import os
os.system('cls')

mylist = [1,2,3,4]
for num in range(3,10,2):
    print(num)

print(list(range(3,10,2)))

#ennumerate
index_count = 0
for letter in 'abcde':
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1

print('---')
word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)

#ZIP
mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']
for item in zip(mylist1,mylist2):
    print(item)

#IN
print('x' in ['x','y'])
print('a' in 'a world')

d = {'mykey':245}
'mykey' in {'mykey':245}
345 in d.keys()

min(mylist)
max(mylist)

#Import function
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,10000))

#INPUTS
result = int(input('Enter a number: '))
if result >= 0:
    result *= 2
    print(f'Your number times 2 is equals to {result}')
else:
    print('Please enter a number greater or equals to 0')
