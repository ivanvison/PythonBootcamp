import os
os.system('cls')
import time
import timeit
# Time Elapsed

# Current time
start_time = time.time()

def func_one(n):
    return [str(num) for num in range(n)]

func_one(100000)
end_time = time.time()
elapse_time = end_time - start_time
print('Elapse time: ', elapse_time)

#Current time
start_time = time.time()
def func_two(n):
    return list(map(str,range(n)))

func_two(100000)
end_time = time.time()
elapse_time = end_time - start_time
print('Elapse time: ', elapse_time)



# Timeit module

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt,setup,number=100000))


stmt2 = '''
func_two(100)
'''
setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt2,setup2,number=100000))