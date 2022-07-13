import PyPDF2
import os
os.system('cls')

path = 'C:\\Users\\Ivan\\Desktop\\Python Path\\BootCamp\\CourseCode\\17-PDFs-and-Spreadsheets\\'

# Open the file
f = open(path+'Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extract_text()
# print(page_one_text)


# Write to PDF

pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.add_page(first_page)
pdf_output = open(path+'Some_BrandNew_Doc.pdf', 'rb')
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()