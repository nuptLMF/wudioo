import requests
from lxml import etree
import re
from flask import Flask
import pymongo
import redis
#from pymongo.connection import Connection
#from datatime import datatime
'''def Download_page(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    res = requests.get(url,headers=headers)
    return res.text

#用Xpath提取数据
def Get_contents(html):
    HTML_Xpath = etree.HTML(html)
    results = HTML_Xpath.xpath('//div[contains(@class,"article")]/a[1]/div/span/text()')
#    result = etree.tostring(results,encoding = 'unicode')
    print(results)

#def extract_content():

    
def main():
	url = r'http://www.qiushibaike.com/text'
	html = Download_page(url)
	Get_contents(html)

if __name__ == '__main__':
	main()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run()

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'test'
client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
db = client[DB_NAME]
post = {"zhanghu":"mongo教程1",
    "decription":"mongo 是一个 nosql 数据库1",
    "url":"http://www.runoob.com",
    "tags":['mongodb1','database1','nosql1'],
    "linkes":1001
    }
'''
pool = redis.ConnectionPool(host='127.0.0.1',port='6379',db=0)
r=redis.Redis(connection_pool=pool)