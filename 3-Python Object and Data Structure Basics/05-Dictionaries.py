#Store Objects
#Key Value pairing
# {'key1':'value1','key2':'value2'}

my_dictionary = {'key1':'value1','key2':'value2'}
print(my_dictionary)
print(my_dictionary['key1'])

prices_lookup = {'apple':2.99, 'oranges':1.99,'banana':0.99}
print(prices_lookup['oranges'])

mega_dictionary = my_dictionary = {'k1':123,'k2':[1,2,3],'k3':{'insideKey1':345,'insideKey2':'Simple'}}
print(mega_dictionary['k3']['insideKey1'])
print(mega_dictionary['k2'][1])

mega_dictionary['k4'] = 500
mega_dictionary['k3']['insideKey2'] = mega_dictionary['k3']['insideKey2'].upper()
print(mega_dictionary)
print('----')
print(mega_dictionary.items())
print(mega_dictionary.values())
print(mega_dictionary.keys())
