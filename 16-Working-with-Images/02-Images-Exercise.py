from PIL import Image
import os
os.system('cls')

path = 'C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\16-Working-with-Images\\'

mask = Image.open(path+'mask.png')
mask = mask.resize((1025,559))
mask.putalpha(125)

matrix = Image.open(path+'word_matrix.png')
matrix.paste(im=mask, box=(0,0), mask=mask)


matrix.save(path+"message.png")