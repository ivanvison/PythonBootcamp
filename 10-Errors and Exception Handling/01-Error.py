import os
os.system('cls')

def add(n1,n2):
    print(n1+n2)

def ask_for_int():
    
    while True:
        try:
            result = int(input("Please Provide a Number: "))
        except:
            print('Whoops! Not a number')
            continue
        else:
            print('Thank you')
            break
        finally:
            print('End of Try/Except/Finally')


number1 = 10
number2 = 5 #int(input("Please Provide a Number: "))

add(number1,number2)
print('Something Happened!')

try:
    # Attempt THIS CODE
    result = 10 + 10
except:
    print("Looks like you aren't adding correctly!")
else:
    print('Add went well')
    print(result)


try:
    f = open('testfile','w')
    f.write('Write a test line\n')
except TypeError:
    print('Error type!')
except OSError:
    print('OS Error type!')
except:
    print('General Error')
finally:
    print('Always Run')
    f.close()


ask_for_int()