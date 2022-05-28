import os
os.system('cls')

def myfunc(*args):
    even_list = []
    
    for num in args:
        if num % 2 == 0:
            even_list.append(num)
    print(even_list)
    return even_list

myfunc(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

print('----------------------')

def myfunc(str): 
    out_str = []

    for i in range(len(str)):
        if i % 2 == 0:
            out_str.append(str[i].lower())
        else:
            out_str.append(str[i].upper())

    return "".join(out_str)

print(myfunc('AbCdEfGhI'))

print('----------------------')

