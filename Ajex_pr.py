import requests
import pymongo
from urllib.parse import urlencode 
from lxml import etree
'''
FIRT BLOOD
'''
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}
Cookie = {"PSTM":"1566317672",
		"BIDUPSID":"C272AD8808694BBC37A8742D03919C28",
		"BAIDUID":"598742F0282C7AC3423A7FD96F9B6C12:FG=1",
		"BDORZ":"B490B5EBF6F3CD402E515D22BCDA1598",
		"Hm_lvt_da3258e243c3132f66f0f3c247b48473":"1568363649,1568368516",
		"Hm_lpvt_da3258e243c3132f66f0f3c247b48473":"1568368516",
		"delPer":"0",
		"PSINO":"5",
		"H_PS_PSSID":"1448_21126_29073_29523_29521_29720_29568_29221",
}

def get_pages(keywords,page):
	base_url = 'https://zhaopin.baidu.com/api/qzasync?'
	params = {
		'query':keywords,
		'city':'%E5%8D%97%E4%BA%AC',
		'is_adq':'1',
		'pcmod':'1',
		'token':'==QmR/qpa+NqWhVmYymbZqZcrhWZbhFbrVWbkRZatlGa',
		'pn':int(page)*20,
		'rn':'20',
		}

	url = base_url+urlencode(params)
	print(url)
	try:
		response = requests.get(url,headers = headers)
		if response.content:
			return response.json()
	except requests.ConnectionError:
		return None


def parse_item(json):
	if json:
		items = json.get('data').get('disp_data')
		for item in items:
			job = {}
			job['name'] = item.get('name')
			job['city'] = item.get('city')
			job['salary'] = item.get('ori_salary')
			job['time'] = item.get('lastmod')
			print(job)


def main():
	for page in range(1,6):
		ja = get_pages('大客户经理',page)
		parse_item(ja)

if __name__=='__main__':
	main()