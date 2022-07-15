import os
import imaplib
import getpass
import email
os.system('cls')

# Connect to server
M = imaplib.IMAP4_SSL('imap.gmail.com')

# Get Email Password from User
email_address = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')

print(M.login(email_address,password))

# Review all labels
# print(M.list())

# Connect to the inbox
print(M.select("INBOX"))


typ ,data = M.search(None,'SUBJECT "Red Cat"')
print(typ)
print(data) #The data will be a list of unique ids.
email_id = data[0]
result , email_data = M.fetch(email_id,'(RFC822)')
# print(email_data)

raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)

