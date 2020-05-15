import requests
import csv
from bs4 import BeautifulSoup
from lxml import etree


def get_pages(url):
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
	r = requests.get(url,headers = headers)
	r.encoding = 'utf-8'
	return r.text

def get_content_xpath(html):
	con = etree.HTML(html)
	title = con.xpath('//*[@id="td_4354432"]/h3//text()')
	print(title)

def get_content_beautifulsoup(html):
	soup = BeautifulSoup(html,'html.parser')
	con = soup.find('div',class_='t z')
	titles = con.find_all('h3')
	daoguo = []
	guochan = []
	for title in  titles:
		ti = title.find('a').string
		if '日本' in ti or '亚洲' in ti:
			daoguo.append(ti)
		elif '国产'  in ti or '國產' in ti:
			guochan.append(ti)

#		elif '國產' in ti:
#			guochan.append(ti)
	print(daoguo)
	print('*'*18)
	print(guochan)
	#print(titles)

def get_info_japan(html):
	pass

def main():
	url = 'http://e1.zxhgqgp.info/pw/thread.php?fid=3&page=1'
	q = get_pages(url)
#	print(q)
#	get_content_xpath(q)
	get_content_beautifulsoup(q)

if __name__ == '__main__':
	main()

