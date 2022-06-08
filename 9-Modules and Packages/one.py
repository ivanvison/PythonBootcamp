def func():
    print("Func() in one.py")

print("Top level in One.py")

if __name__ == '__main__':
    print('one.py is being run directly!')
else:
    print('One.py has been imported')

