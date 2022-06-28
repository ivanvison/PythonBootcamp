import os
import shutil
import send2trash
os.system('cls')


f = open('practice.txt', 'w+')
f.write('This is a string')
f.close()

print(os.getcwd())

#for item in os.listdir():
#    print(item)

if 'practice.txt' in os.listdir():
    shutil.move('practice.txt','C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\15-Advanced Python Modules',)

send2trash.send2trash('C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\15-Advanced Python Modules\\practice.txt')

file_path = 'C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\15-Advanced Python Modules\\Example_Top_Level'
for folder, sub_folders, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print("Subfolders are")
    for sub_folder in sub_folders:
        print(f"\tSubfolder: {sub_folder}")

    print("The files are: ")
    for f in files:
        print(f'\tFile: {f}')

    print('\n')
