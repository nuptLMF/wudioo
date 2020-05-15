import requests
import json
import re
import time
import pymongo

MONGO_URI = 'localhost'
MONGO_PORT = 27017
MONGO_DATABASE = 'stock_info'

client = pymongo.MongoClient(host = MONGO_URI,port = MONGO_PORT)
db = client[MONGO_DATABASE]
count = 0
stock_info_map = {
	"kpj":"f17",
	"zdf":"f3",
	"zde":"f4",
	"cjl":"f5",
	"cje":"f6",
	"spj":"f2",
	"hsl":"f8",
	"syl":"f9",
	"sjl":"f23",
	"zgj":"f15",
	"zdj":"f16",
	"gpdm":"f12",
	"gpmc":"f14",
}
for i in range(1,195):
	url = "http://22.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403375894672138908_1575724270341&pn={}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1575724270354".format(i)
	res = requests.get(url)
	j = re.findall("[(](.*?)[)]",res.text)[0]
	a = json.loads(j)
	stock_info = {}
	t = time.localtime(time.time())
	if t[2]<10:
		parse_time=str(t[0])+str(t[1])+'0'+str(t[2])
	else:
		parse_time=str(t[0])+str(t[1])+str(t[2])
	stock_info["sj"] = parse_time
	for k in range(20):
		try:
			b = a["data"]["diff"][k]
			for s,c in stock_info_map.items():
				stock_info[s] = b[c]
			count = count+1
#			print(b)
			print(stock_info)
#			db[stock_info['gpdm']].create_index([('id', pymongo.ASCENDING)])
			db[stock_info["gpdm"]].update_many({'sj': stock_info.get('sj')}, {'$set': stock_info}, True)
			print("存入数据成功")
		except:
			print("存入数据失败")


print("一共股票数量："+str(count))
#print(re.text)