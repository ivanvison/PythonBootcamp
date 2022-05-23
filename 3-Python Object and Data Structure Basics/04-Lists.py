my_list = [1,2,3]
print(my_list)

my_other_list = ['STRING', 100, 23.2]
print(my_other_list)

print(len(my_other_list))

#Indexing Slicing and concatenate works the same as in string

my_master_list = my_list + my_other_list
print(my_master_list)

#List are mutable
my_master_list[0] = 'ONE ALL CAPS AND TEXT'
print(my_master_list)

#Methods, append
my_master_list.append('Appended')
print(my_master_list)

#remove items from the list
popped_items = []
popped_items.append(my_master_list.pop())
print(my_master_list)
popped_items.append(my_master_list.pop(0))
print(popped_items)
print(my_master_list)

new_list = ['a', 'x', 'b', 'z', 'e', 'm']
number_list = ['5', '9', '1', '2', '4', '8']

new_list.sort(reverse=True)
#new_list.reverse()
print(new_list)
number_list.sort()
print(number_list)