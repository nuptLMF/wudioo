import os
import re
import pdfplumber
import docx

files = docx.Document()
path = "E:\pdf_to_excel\pdf文件"
file = os.listdir(path)[2]
filepath = path+'\\'+file
with pdfplumber.open(filepath) as pdf:
	for page in pdf.pages:
		content = page.extract_text()
		print(content)
		files.add_paragraph(content)
	files.save(path+'\\'+'abcd.docx') 


                                                                                                                