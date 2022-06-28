import os
os.system('cls')

def cool():

    def super_cool():
        return 'I am very cool!!'

    return super_cool

some_func = cool()
print(some_func())


def new_decorator(original_func):

    def wrap_func():
        print('Code before the original function')

        original_func()

        print('Code after the original function')

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!!")

print(func_needs_decorator())

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!!")