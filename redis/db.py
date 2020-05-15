import redis
import random

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = 'lvmingfu123'

class redis_client(object):
	def __init__(self,type, website, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
		self.db_client = redis.StrictRedis(host = host, port = port ,db =7, password = REDIS_PASSWORD)
		self.type = type
		self.url_ = url_
		self.website = website
	def name(self):

		return '{type}:{website}{url_}'.format(type = self.type,website = self.website,url_ = self.url_)

	def set(self,username,value):

		return self.db_client.hset(self.name(),username,value)

	def get(self,username):

		return self.db_client.hget(self.name(),username)

	def delete(self,username):

		return self.db_client.hdel(self.name(),username)

	def count(self):
		
		return self.db_client.hlen(self.name())

	def random(self):

		return random.choice(self.db.hvals(self.name()))

	def usernames(self):

		return self.db_client.hkeys(self.name())

	def all(self):

		return self.db.hgetall(self.name())

if __name__ == '__main__':
	conn = redis_client('accounts','weibo')
	result = conn.set('hello','sss231')
	result1 = conn.get('hello')
	print(result)
	print(result1)
	