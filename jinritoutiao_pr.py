import requests
from lxml import etree

def Request(url):
	headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"} 
	r = requests.get(url,headers=headers)
	return r.text

def parse_info(html):
	param = {
		"aid":24
		"app_name":"web_search"
		"offset":0
		"format":"json"
		"keyword":"街拍"
		"autoload":"true"
		"count":20
		"en_qc":1
		"cur_tab":1
		"from":"search_tab"
		"pd":"synthesis"
		"timestamp":1568213148932
	}
	h = etree.HTML(html)
