#def, indentation
#snake casing
#parenthesis
#colon
#optional Multi-line string to describe function
import os
os.system('cls')

def say_hello(name='Default'):
    print(f'Hello {name}')

say_hello()

def request_name():
    name = input("What's your name?: ")
    return name

def hello_name():
    print(f'Hello {request_name()}')

hello_name()

def add_function(num1,num2):
    return num1 + num2

result = add_function(5,6)
print(result)
