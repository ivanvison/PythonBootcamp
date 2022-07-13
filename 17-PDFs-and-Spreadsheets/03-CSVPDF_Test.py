from types import NoneType
import PyPDF2
import csv
import os
import re
os.system('cls')

path = 'C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\17-PDFs-and-Spreadsheets\\Exercise_Files\\'

# Task One: Use Python to extract the Google Drive link from the .csv file.
# (Hint: Its along the diagonal from top left to bottom right).
csv_file = open(path+'find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(csv_file)

# reformat it into a python object list of lists
data_lines = list(csv_data)

link = []
i = 0

for line in data_lines[1:]:
    link.append(data_lines[i][i])
    i += 1

link = ''.join(link)
print(link)


'''
link_str = ''

for row_num, data in enumerate(data_lines):
    link_str += data[row_num]

print(link_str)
'''

# Task Two: Download the PDF from the Google Drive link (we already downloaded it for you
# just in case you can't download from Google Drive) and find the phone number that is in the document.
# Note: There are different ways of formatting a phone number!
f = open(path+'Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
phone_pattern = r'\d{3}[\s.-]?\d{3}[\s.-]?\d{4}'
results = []

for page in range(pdf_reader.numPages):
    current_page = pdf_reader.getPage(page)
    text = current_page.extractText()
    phone = re.search(phone_pattern,text)
    print(f'{page + 1} - {phone}')

    if type(phone) != NoneType:
        result_page = page
        break

print(f'\nPhone is: {phone.group()}')
print(f'Located in page: {result_page}')


   