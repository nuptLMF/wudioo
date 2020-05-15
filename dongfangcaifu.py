import requests
from lxml import etree
from bs4 import BeautifulSoup
from urllib.parse import urlencode 
import re
import json


headers = {
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
			"Host":"22.push2.eastmoney.com",
			"Referer":"http://quote.eastmoney.com/center/gridlist.html"
}

def turn_pages(base_url,page):

	url = base_url+"cb=jQuery1124014808540857572172_1561848272609&pn={}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1561848272624".format(page)
	try:
		response = requests.get(url,headers = headers)
		response.encoding = 'utf-8'
		data = re.findall('diff":\[(.*?)\]',response.text)[0]
		dd = re.findall('\{(.*?)\}',data)
		print(type(dd))
		print(dd)



	except requests.ConnectionError:
		return None


def parse_east(html):
	pass

def main():
	base_url = 'http://70.push2.eastmoney.com/api/qt/clist/get?'
	for page in range(1,5):
		json = turn_pages(base_url,page)
		parse_east(json)


if __name__ =='__main__':
	main()