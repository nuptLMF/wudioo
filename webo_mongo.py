import pymongo
import re
import csv
import os
path = "D:\\BaiduYunDownload"

def get_conn():
	client = pymongo.MongoClient(host = 'localhost',port = 27017)
	db = client["weibo"]
	csv_datas = []
	count = 0
	for i in db["users"].find():
#		print(i["description"])
		if re.findall("[0-9a-zA-Z]+",i["description"]):
			print("描述:"+i["description"],"\n昵称："+i["name"],"\n粉丝数："+str(i["fans_count"]),"\n微博账号:"+str(i["id"]))
			csv_datas.append([i["name"],i["id"],i["description"],i["fans_count"]])
			count = count+1
	print(count)
	return csv_datas

def csv_write(datas):
	with open(path+"\\example.csv","w",newline = "",encoding = "UTF-8-sig") as f:
		writer =csv.writer(f)
		for data in datas:
			writer.writerow(data)

def main():
	x = get_conn()
	csv_write(x)

if __name__=="__main__":
	main()