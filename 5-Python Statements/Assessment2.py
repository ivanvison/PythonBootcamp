import os
os.system('cls')

#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
# Method 1
words_list = st.split(' ')
print(words_list)
for word in words_list:
    temp = word
    if temp[0] == 's' or temp[0] == 'S':
        print(word)

#Method 2 - Instructor
for word in st.split():
    if word[0] == 's':
        print(word)


#Use range() to print all the even numbers from 0 to 10.
#Method 1
for num in range(0,11):
    if num % 2 == 0:
        print(num)

#Method 2 - Instructor
print(list(range(0,11,2)))


#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist = [num for num in range(1,51) if num % 3 == 0]
print(mylist)


#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
#Method 1
words_list = st.split(' ')
print(words_list)
for word in words_list:
    if len(word) % 2 == 0:
        print(f'{word} - This word is Even!')

#Method 2 - Instructor
for word in st.split():
    if len(word) % 2 ==0:
        print(f'{word} has an even lenght!')


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
#Included the numbers for personal purposes.
print('---')
for num in range(0,101):
    if (num % 3 == 0) and (num % 5 == 0):
        print(f'FizzBuzz - {num}')
    elif num % 3 == 0:
        print(f'Fizz - {num}')
    elif num % 5 == 0:
        print(f'Buzz - {num}')
    else:
        print(num) 

#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
mylist = [letter[0] for letter in st.split()]
print(mylist)