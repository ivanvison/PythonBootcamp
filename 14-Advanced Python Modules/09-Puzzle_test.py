import os
os.system('cls')
import shutil
import re

def search(file,pattern):
    f = open(file,'r')
    text = f.read()

    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''


'''
zippath = 'C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\14-Advanced Python Modules'
shutil.unpack_archive(zippath+'\\unzip_me_for_instructions.zip',zippath+'','zip')

with open(zippath+'/extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)
'''
unzipped_path = 'C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\14-Advanced Python Modules\\extracted_content'
print(unzipped_path+'\n')

'''
TASK:
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-#### 
Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
'''

pattern = r'\d{3}-\d{3}-\d{4}'
results = []
file_names = ''
i = 0
# Iterate through folders
for folder, sub_folders, files in os.walk(unzipped_path):
    
    for f in files:     
        full_path = folder+'\\'+f

        results.append(search(full_path,pattern))

    for r in results:
        if r != '':
            print(r.group())