import os
os.system('cls')
from collections import Counter
from collections import defaultdict
from collections import namedtuple

# SPECIALIZED CONTAINER TYPE

my_list = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3]
print(Counter(my_list))

string_list = ['a','a','b','b',10,10,10,10,10]
print(Counter(string_list))

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print(Counter(sentence.lower().split()))

letters = 'aaaaaaaaaaaaabbbbbbbbbbccccccccdddddddddd'
c = Counter(letters)
print(c)
print(c.most_common(3))
print(list(c))

print('---')

d = {'a':10}
print(d)
print(d['a'])

# Assign default value
d = defaultdict(lambda: 0)
print(d['Wrong'])

print('---')

mytuple = (10,20,30)
print(mytuple)

Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age=5,breed='Husky',name='Sam')
print(sammy)
print(type(sammy))
print(sammy.breed)