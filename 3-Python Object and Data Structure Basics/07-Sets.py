#Unordered collections of unique elements

myset = set()

myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset)

mylist = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
print(mylist)
print(set(mylist))

print(set('Mississippi'))
