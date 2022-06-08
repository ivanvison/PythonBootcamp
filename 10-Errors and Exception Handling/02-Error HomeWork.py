import os
os.system('cls')

# PROBLEM 1

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Please provide a valid list of values")

# PROBLEM 2
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by 0")
finally:
    print('ALL DONE!')

# PROBLEM 3
def ask():
    
    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('An error occured. Please verify value.')
            continue
        else:
            print(f"Thank you, your squared number is: {result**2}")
            break
        
ask()