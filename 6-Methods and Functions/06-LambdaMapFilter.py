print('---LAMBDA---')
#Lambda
square = lambda num: num ** 2
print(square(5))
my_nums = [1,2,3,4,5,6]
print(list(map(lambda num:num**2,my_nums)))

print(list(filter(lambda num: num%2 == 0,my_nums)))

names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda x:x[0],names)))

print('\n\n---MAP---')
#Map
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print(item)
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer,names)))


#Filter
print('\n\n---FILTER---')
def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6]
print(list(filter(check_even, mynums)))