from ast import arg

def myfunc(a,b):
    #Returns 5% of the sum of a and b
    return sum((a,b))*0.05

print(myfunc(40,60))

#WTF
def myfunc(*args):
    #Returns 5% of the sum of all received values
    return sum(args)*0.05

print(myfunc(40,60,200,20,15,50))

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My Fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('No fruit!')

myfunc(fruit='apple',car='Audi',coffee='black')

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange', food='eggs', amimal='dog')
