import csv
import os
os.system('cls')

path = 'C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\17-PDFs-and-Spreadsheets\\'

# Open the file
data = open(path+'example.csv', encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)

print(data_lines[2])
print(data_lines[2][0])
print(data_lines[3][1])
print(len(data_lines))

for line in data_lines[:5]:
    print(line)

all_emails = []

for line in data_lines[1:]:
    all_emails.append(line[3])

# print(all_emails)

full_names = []

for line in data_lines[1:]:
    full_names.append(line[1]+ ' ' +line[2])

# print(full_names)

file_to_output = open('to_save_file.csv',mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerow([['1','2','3'],['4','5','6'],['7','8','9']])
file_to_output.close()

f = open('to_save_file.csv',mode='a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1','1','1'])
f.close()

