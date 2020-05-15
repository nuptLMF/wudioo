import pymongo


MONGODB_URI = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_NAME = 'weibo'
client = pymongo.MongoClient(MONGODB_URI,MONGODB_PORT)
db = client[MONGODB_NAME]
results = db['weibos'].find()
print('+++')
print(type(results))
print(results)
print(results.count())

#查找账号
news = db['weibos'].find_one({'name':'今天不睡觉行不行'})
news1 = db['weibos'].find_one({'user':1642351362})


print('*'*18)
print(news)
print(type(news))
print('*'*18)
print(news1)