import pandas as pd
import numpy as np
import xlwt
import xlrd
import os
import re
path0 = "E:\pdf_to_excel转化后\数据处理(1)\pdf_to_excel转化后\目标文件\\abc.xls"
path = "E:\pdf_to_excel转化后\数据处理(1)\pdf_to_excel转化后\台区96点数据.7.26日"
path1 = "E:\pdf_to_excel转化后\数据处理(1)\台区-编号连接关系.xls"
path2 = path + '\\' + '电流图形数据0537068483.xls'
docs = os.listdir("E:\pdf_to_excel转化后\数据处理(1)\pdf_to_excel转化后\台区96点数据.7.26日")
number_list = []
for x in docs:
	number = re.findall("([A-Z]{0,1}[0-9]+).xls",x)[0]
	if not number in number_list:
		number_list.append(number)
ss = xlrd.open_workbook(path1)
m = ss.sheet_by_index(0)
dic = {}
for k in range(1,m.nrows):
	dic[m.row_values(k)[5]] = m.row_values(k)[1]

print(dic)

def EXCEL_read():
	new_sheet = []
	for j in number_list:
		doc_name1 = path + '\\' + '电流图形数据{}.xls'.format(j)
		doc_name2 = path + '\\' + '电压图形数据{}.xls'.format(j)
		doc_name3 = path + '\\' + '无功功率图形数据{}.xls'.format(j)
		doc_name4 = path + '\\' + '有功功率图形数据{}.xls'.format(j)
		for i in [doc_name1,doc_name2,doc_name3,doc_name4]:
			myfile = xlrd.open_workbook(i)
#			sheets = myfile.sheet_names()
			first_table = myfile.sheet_by_index(0)
			n = first_table.nrows
			for i in range(1,n):
				x = first_table.row_values(i)
				x.insert(0,str(j))
				x.insert(0,dic[str(j)])
				print(x)
				new_sheet.append(x)
	xlrd.open_workbook(path2)
	n = xlrd.open_workbook(path2).sheet_by_index(0)
	nn = n.row_values(0)
	nn.insert(0,'资产编号')
	nn.insert(0,'台区')
	new_sheet.insert(0,nn)
#	print(new_sheet)
	return new_sheet

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
	return i

def main():
	datas = EXCEL_read()
	count = EXCEL_write(path0,datas)

if __name__=='__main__':
	main()
