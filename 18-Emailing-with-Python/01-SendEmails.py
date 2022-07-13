import os
import smtplib
import getpass
os.system('cls')

# Connect to server
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())
print(smtp_object.starttls()) # Only when using 587

# Get Email Password from User
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')

# Connect with credentials
print(smtp_object.login(email,password))

from_address= email
to_address = email
subject = input("Enter Subject: ")
message = input("Enter Body: ")
msg = "Subject: "+subject+'\n'+message

# Send Email
print(smtp_object.sendmail(from_address,to_address,msg))

# Close Session
smtp_object.quit()

