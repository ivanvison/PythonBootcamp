import os
os.system('cls')
import re

print("--------- |PART 1| ---------")

text = "The agent's phone number is 408-555-6589. Call soon!"
print('phone' in text)

pattern = 'phone'
print(re.search(pattern,text))
print(re.search('gugu',text))

match = re.search(pattern,text)
print(match.span())
print(match.start())
print(match.end())

text2 = 'My phone once, my phone twice'
print(re.search('phone',text2))
matches = re.findall('phone',text2)
print(matches)
for match in re.finditer('phone',text2):
    print(match)


print("\n--------- |PART 2| ---------")
text3 = "The agent's phone number is 408-555-6589. Call soon!"
phone = re.search(r'\d\d\d-\d\d\d-\d{4}',text3)
print(phone)
print(phone.group())
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text3)
print(results.group())
print(results.group(1)) # Area code


print("\n--------- |PART 3| ---------")
print(re.search(r'cat|dog','The catttt is here'))

print(re.findall(r'.oo.','how much wood could a woodchuck chuck... According to the Poetry Foundation, a woodchuck would chuck “As much wood as a woodchuck could chuck, If a woodchuck could chuck wood.'))

print(re.findall(r'^\d|\d$', '6 is A nice number an also 2'))

phrase = 'There are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d ]+' # r'[^!.?]+'
clean = re.findall(pattern,phrase)
print(clean)
print(' '.join(clean))

text = 'Only find the hypen-word in this sentence. You do not know how long-ish these words are'
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern,text))

# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|erpillar)',text))