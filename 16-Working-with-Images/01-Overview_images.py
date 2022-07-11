from PIL import Image
import os
os.system('cls')

path = 'C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\16-Working-with-Images\\'

pencils = Image.open(path+'pencils.jpg')
print(pencils.size)
print(pencils.format_description)

# CROPPING IMAGES

x = 0
y = 0

w = 1950 / 3
y = 1330 / 10

pencils.crop((x,y,w,y))

x = 0 
y = 1100
w = 1950/3
h = 1300
pencils.crop((x,y,w,h))