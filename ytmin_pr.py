import os
import re

path = "E:\\ymetin\\items"
ss = os.listdir("E:\\ymetin\\items")

for i in ss:
	if i[-3:] =='itm':
		try:
			with open(path+"\\"+i,"r") as f:
#				print(f.read())
				k = re.findall("[\u4e00-\u9fa5]+",f.read())
				if '阳光' in k[-1]:
					print(i,k) 
		except:
			print("打不开",i)
