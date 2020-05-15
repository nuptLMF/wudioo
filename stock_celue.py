import pymongo

MONGO_URI = 'localhost'
MONGO_PORT = 27017
MONGO_DATABASE1 = 'stock_list'
MONGO_DATABASE2 = 'stock_info'

count =0
client = pymongo.MongoClient(host = MONGO_URI,port = MONGO_PORT)
db1 = client[MONGO_DATABASE1]
db2 = client[MONGO_DATABASE2]

for i in db1["gpqd"].find():
	price1 = db2[i]["spj"]-(db2[i]["zgj"]+db2[i]["zdj"])/2
	if price1>0:
		print(i)
		count= count+1

print("可能上涨股数:"+str(count))
#for i in count:
#	print(i)