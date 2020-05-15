from redis import StrictRedis
import random

redis = StrictRedis(host = 'localhost',db =7 ,port=6379,password = 'lvmingfu123')

#k = random.choice(redis.keys())
k = redis.hvals('cookies')
print(k)
