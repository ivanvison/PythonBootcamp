#Iteration
from multiprocessing.sharedctypes import Value


my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    print(num)
    print('Hello')

for num in my_list:
    #Check for even
    if num% 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in my_list:
    list_sum += num

print(list_sum)

#STRING
mystring = 'Hello World'

for letter in mystring:
    print(letter.upper())

#TUpple
tup = (1,2,3)
for item in tup:
    print(item)

mylist = [(1,2,9), (3,4,0), (5,6,10), (7,8,0)]
for item in mylist:
    print(item)

#Tupple and packing
for (a,b,c) in mylist:
    print(a)
    print(b)

for (a,b,c) in mylist:
    print(c)

print('-----------')

#Dictionaries
dic = {'k1':1, 'k2':2, 'k3':3}
for item in dic.items():
    print(item)

for key,value in dic.items():
    print(value)

for value in dic.values():
    print(value)