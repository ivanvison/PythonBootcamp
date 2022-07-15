import os
os.system('cls')

# Advanced Numbers
print(hex(12))
print(bin(256))
print(pow(3,4,3))
print(round(3.945435,2))

# Advanced Strings
print('--')
s = 'hello world'
print(s.upper())
print(s.count('o'))
print(s.find('o'))
print(s.islower())
print(s.isspace())

# Advanced Sets
print('--')
s = set()
s.add(1)
s.add(2)
print(s)
sc = s.copy()
sc.add(4)
print(sc)
print(s.difference(sc))
s.discard(2)
print(s)

# Advanced Dictionaries
print('--')
d = {'k1':1, 'k2':2}

print({x:x**2 for x in range(10)})
print({k:v**2 for k,v in zip(['a','b'],range(2))})


# Advanced Lists
print('--')
l = [1,2,3,4]
l.extend([6,7]) # Different to APPEND
print(l)

l.insert(2, 'inserted')
print(l)

# Advanced Objects Assessment Test