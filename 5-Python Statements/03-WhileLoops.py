import os
os.system("cls")

num = 0
while num <= 5:
    print(f'The current value of num is {num}')
    num += 1
else:
    print('X is not less than 5')

#break
mystring = 'SamMy'
for letter in mystring:
    if letter == 'M':
        break
    else:
        print(letter)

#continue
mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    else:
        print(letter)

#pass
x = [1,2,3]
for item in x:
    pass #placeholder / filler