
import os
os.system('cls')

x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

#Local
# lambda num:num**2


#GLOBAL
name = 'This is a global String'
def greet():
    #ENGLOSING
    name = 'Sammy' #Comment to see the global behaviour 

    def hello():
        #LOCAL
        print('Hello ' + name)
    
    hello()

greet()

#DANGEROUS PATH! safer to retun the object and reassign 
x = 50
def func():
    global x
    print(f'X is {x}')

    #Local
    x = 'NEW'
    print(f'Changed X to {x}')

func()
print(x)