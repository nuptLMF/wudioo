import requests
import time
from lxml import etree
import re

def response_(url):
	res = requests.get(url)
	res.raise_for_status()
	res.encoding = 'utf-8'
	return res.text

def parse_iqiyi(html):
	cate = []
	Html = etree.HTML(html)
	video_name = Html.xpath('//*[@id="block-D"]/div//text()')
	print(video_name)

	Category = Html.xpath('//*[@id="block-C"]//text()')
#	web = Html.xpath('//*[@id="nav_sec_K3"]/div[6]/div[2]/div[1]//text()')
	for i in Category:
		codes = re.findall('[\u4e00-\u9fa5]+',i)
		if codes:
			cate.append(codes[0])
	print(cate)
	for i in range(1,len(cate)):
		web_name = Html.xpath('//*[@id="block-C"]/div[1]/div[1]/div[3]/div[6]/div[2]/a/text()')[0]
		web_url = Html.xpath('//*[@id="block-C"]/div[1]/div[1]/div[3]/div[6]/div[2]/a/@href')
	print(web_name)
	print(web_url)

def main():
	urls = 'https://list.iqiyi.com/www/3/70-------------4-1-1-iqiyi-1-.html'
#	code_num =['70','72','74','73','77','71','28119','310','28137','28138']
#	for i in code_num:
#		url = 'https://list.iqiyi.com/www/3/{}-------------4-1-1-iqiyi-1-.html'.format(i)
	html = response_(urls)
	parse_iqiyi(html)

if __name__=='__main__':
	main()