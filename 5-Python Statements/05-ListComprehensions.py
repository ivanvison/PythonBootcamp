#Unique way of creating a list
#Example: using a for loop along with .append to create a list
import os
os.system('cls')

mystring = 'Hello'
mylist = []

#method 1
for letter in mystring:
    mylist.append(letter)

print(mylist)

#Method 2
mylist = [letter for letter in mystring]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)

mylist = [num**2 for num in range(0,11) if num % 2 == 0]
print(mylist)

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

#Nested loops
mylist = []

for x in [2,4,6]:
    for y in [1,2,3,4,5]:
        mylist.append(x*y)

print(mylist)

