import os
import imaplib
import getpass
os.system('cls')

# Connect to server
M = imaplib.IMAP4_SSL('imap.gmail.com')

# Get Email Password from User
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')

print(M.login(email,password))

# Review all labels
# print(M.list())

# Connect to the inbox
print(M.select("INBOX"))

typ ,data = M.search(None,'SUBJECT "Red Cat"')
print(typ)
print(data) #The data will be a list of unique ids.

