import pdfplumber
import pandas as pd
import xlwt
import os

path = 'E:\\pdf_to_excel\\华西线132\\台区96点数据.8.21日'

def PDF_reader(path):
	#PDF中表格数据读取并清洗多余字符，取出数据
	try:
		with pdfplumber.open(path) as pdf:
			#获取第一页的数据pages【0】
			first_page = pdf.pages[0]
			new_sheet = []
			#提取第一页中的第一个表格
			datasheet = first_page.extract_tables()[0]
			#表格的总行数
			length = len(datasheet)
			for i in range(length):
				datasheet_01 = []
				for data in datasheet[i]:
					#将每行数据清洗
					datasheet_01.append(data.replace('\n',''))
				new_sheet.append(datasheet_01)
				#将清洗后的表格数据以列表形式返回
		return new_sheet
	except:
		return 0
		

def EXCEL_write(file_path,datas):
	#EXCEL数据写入，file_path输出文件夹路径，datas输出文件中的数据，行写入
	f = xlwt.Workbook()#初始化表格
	sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet1作为写入sheet
	#将数据写入第 i 行，第 j 列
	i = 0
	for data in datas:
		for j in range(len(data)):
			sheet1.write(i,j,data[j])
		i = i + 1
	f.save(file_path)

def main():
	file_paths = []
	path = 'E:\\pdf_to_excel\\华西线132\\台区96点数据.8.21日'#PDF所在的文件夹路径
	file_names = os.listdir(path)#遍历文件夹中的所有文件名称
	x = 0
	for file_name in file_names:
		path1 = path +'\\'+file_name#源文件的路径
		path2 = 'E:\\pdf_to_excel转化后\\台区96点数据.8.21日'+'\\'+file_name[:-3]+'xls'#输出文件的路径
		datas = PDF_reader(path1)
		if datas:
			EXCEL_write(path2,datas)
		print('文件'+path1+'转化完成')
		x = x +1
		print('转化完成{}个'.format(x))

if __name__=='__main__':
	main()