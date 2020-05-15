import os
import pandas as pd
path = 'E:\\pdf_to_excel\\华西线132\\台区96点数据.8.21日'
path2 = 'E:\\pdf_to_excel转化后\\台区96点数据.8.21日'
names = os.listdir(path)
file_paths = []
for file_name in names:
	file_path = path2+'\\'+file_name[:-3]+'xls'
	df = pd.DataFrame()
	df.to_excel(file_path)
	file_paths.append(file_path)
print(file_paths)

