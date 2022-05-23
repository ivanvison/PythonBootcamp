f = open("test.txt","w+")
f.write("Hello this is a text file\nThis is the second line\nthis is the third line")
f = open("test.txt","r")
content = f.read()
print(content)
print('----------')
f = open("test.txt","a+")
f.write("\nAnd Another line")
f = open("test.txt","r")
content = f.read()
print(content)
print('----------')
f.seek(0) #Resets the cursor
lines = f.readlines()
print(lines)
f.close()

#This method theres no need to close the file
with open('test.txt',mode='r+') as my_new_file:
    contents = my_new_file.read()
    print("---")
    print(contents)





