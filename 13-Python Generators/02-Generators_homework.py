import os
import random
os.system('cls')

print('------------PROBLEM 1-------------')
def square_gen(n):

    for num in range(n):
        yield num**2

for x in square_gen(10):
    print(x)

print('\n------------PROBLEM 2-------------')
def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
    pass

for num in rand_num(1,10,12):
    print(num)

print('\n------------PROBLEM 3-------------')
s = 'Hello'
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

