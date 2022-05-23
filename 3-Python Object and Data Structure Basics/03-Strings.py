#'hello'
#"Hello"
#"I don't do that"
#Ordered sequences - indexing per character
#Reverse index: 0 -4 -3 -2 -1
#Slide: [start:stop:step]

print('Hello world')
print("I'm going on a run") #Note the ' mixed with "

print('Hello \nworld') #\n new line, \t tab

print(len('Hello World')) #Length

#Indexing and Slicing
mystring = "Hello World"
print(mystring)
print(mystring[0])
print(mystring[8])
print(mystring[-2])

mystring = 'abdcefghijk'
print(mystring[2:]) #this goes all the way to the end
print(mystring[:3]) #this shows UP TO - NOT INCLUDING - index 3
print(mystring[3:6]) #grabs a subsection

print(mystring[::2]) #step size of 2
print(mystring[1:7:3]) #step size of 2
print(mystring[::-1]) #Reverse trick

#String Properties and Methods
# String are immutability
name = "sam"
#name[0] = 'P' Error
last_letters = name[1:]
#String Concatenation
new_name = 'P' + last_letters
print(new_name)

#Mult of letters
print(new_name * 3)

#Methods
x = 'Hello World'
x = x.upper()
print(x)
new_x = x.split('L');
print(new_x)

#String Formatting for Printing
#.format()
print('This is a string {}'.format('INSERTED'))
print('The {2} {0} {1}'.format('brown', 'fox', 'quick'))
print('The {q} {b} {f}'.format(b='brown', f='fox', q='quick'))

#Float formatting
result = 100/777
print("The result was {r:1.3f}".format(r=result))

#f-strings
name = "Jose"
print(f'Hello, his name is {name}')