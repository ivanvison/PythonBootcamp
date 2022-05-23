#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
equation = ((((5**2)*9)/2)-12.5)+.25
print(equation)

#What is the value of the expression 4 * (6 + 5) = 44
print(4 * (6 + 5))
#What is the value of the expression 4 * 6 + 5 = 29
print(4 * 6 + 5)

#What is the value of the expression 4 + 6 * 5 = 34
print(4 + 6 * 5)

#What is the type of the result of the expression 3 + 1.5 + 4?
equation = 3 + 1.5 + 4
print(type(equation))

#What would you use to find a number’s square root, as well as its square?
#math.sqrt(0)   or 100 ** 0.5
#number**2

#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'Hello'
print(s[1])

#Reverse the string 'hello' using slicing:
print(s[4])

#Given the string hello, give two methods of producing the letter 'o' using indexing.
#method 1
print(s[-1])

#method 2
print()

#LISTS
#Build this list [0,0,0] two separate ways.
list = [0,0,0]
print(list)

list_two = [0]*3
print(list_two)

#Reassign 'hello' in this nested list to say 'goodbye' instead: list3 = [1,2,[3,4,'hello']]
list3 = [1,2,[3,4,'hello']]
print(list3)
list3[2][2] = 'goodbye'
print(list3)

#Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#DICTIONARIES
#Using keys and indexing, grab the 'hello' from the following dictionaries: d = {'simple_key':'hello'}
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#Tuplets
tuplet1 = (0,1,2,3,4)

#Use a set to find the unique values of the list below: list5 = [1,2,2,33,4,4,11,22,3,3,2]
list5 = [1,2,2,33,4,4,11,22,3,3,2]
list5.sort
print(set(list5))

#Booleans
print(3.0 == 3)