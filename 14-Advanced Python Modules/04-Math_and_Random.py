import os
os.system('cls')
import math
from math import pi
import random

value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(4.5))
print(round(4.6))
print(round(5.5)) # It will round to even numbers

print(pi)

print(math.sin(10))

print('====== RANDOM ======')

random.seed(101)
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

mylist = list(range(0,20))
print(mylist)
print(random.choice(mylist))

# SAMPLE WITH REPLACEMENT
print(random.choices(population=mylist,k=10))

# SAMPLE WITHOUT REPLACEMENT
print(random.sample(population=mylist,k=10))

print(random.uniform(a=0,b=100))

print(random.gauss(mu=0,sigma=1))