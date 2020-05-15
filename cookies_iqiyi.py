from selenium import webdriver
import urllib.parse
import requests
import json
import time

browser = webdriver.Chrome()
browser.get('https://www.iqiyi.com')
cookies = browser.get_cookies()
print(cookies)
	#国内1
	#香港28997
	#美国2
	#欧洲3
	#韩国4
	#日本308
	#泰国1115
	#印度28999
	#area=[1,28997,2,3,4,308,1115,28999]
"https://pcw-api.iqiyi.com/search/video/videolists?access_play_control_platform=14&channel_id=1&data_type=1&from=pcw_list&is_album_finished=&is_purchase=&key=&market_release_date_level=&mode=24&pageNum={}&pageSize=48&site=iqiyi&source_type=&three_category_id={};must&without_qipu=1"	#其他5
#cookies = [{'domain': 'list.iqiyi.com', 'expiry': 1897621046, 'httpOnly': False, 'name': '__uuid', 'path': '/www/3', 'secure': False, 'value': 'a2747bc6-7685-b609-c210-4040cfbb4531'}, {'domain': '.iqiyi.com', 'expiry': 4420501044, 'httpOnly': False, 'name': 'QC005', 'path': '/', 'secure': False, 'value': '866eabbae4325ae58cdb4df2520f3988'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC007', 'path': '/', 'secure': False, 'value': 'DIRECT'}, {'domain': '.iqiyi.com', 'expiry': 4420501044, 'httpOnly': False, 'name': 'QC173', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.iqiyi.com', 'expiry': 1613797046, 'httpOnly': False, 'name': 'QC008', 'path': '/', 'secure': False, 'value': '1582261046.1582261046.1582261046.1'}, {'domain': '.iqiyi.com', 'expiry': 1613797044, 'httpOnly': False, 'name': 'Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e', 'path': '/', 'secure': False, 'value': '1582261045'}, {'domain': '.iqiyi.com', 'expiry': 1613797046, 'httpOnly': False, 'name': 'QC006', 'path': '/', 'secure': False, 'value': 'siygxaz4odx4tsnoiuewp8w0'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e', 'path': '/', 'secure': False, 'value': '1582261045'}, {'domain': '.iqiyi.com', 'expiry': 1582520245, 'httpOnly': False, 'name': 'QC175', 'path': '/', 'secure': False, 'value': '%7B%22upd%22%3Atrue%2C%22ct%22%3A%22%22%7D'}, {'domain': '.iqiyi.com', 'expiry': 1613365046.458142, 'httpOnly': False, 'name': 'T00404', 'path': '/', 'secure': False, 'value': 'f0773dd452ccd42c796536255131ce08'}, {'domain': '.iqiyi.com', 'expiry': 1613365046.458175, 'httpOnly': False, 'name': 'IMS', 'path': '/', 'secure': False, 'value': 'IggQABj__L_yBSokCiA3MTBkZTRjNGEwY2E4ZDYzMmE5ODY5MzkwZjY3Y2ZmOBAA'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'nu', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.iqiyi.com', 'httpOnly': False, 'name': 'QC010', 'path': '/', 'secure': False, 'value': '246375040'}, {'domain': '.iqiyi.com', 'expiry': 1924905600, 'httpOnly': False, 'name': '__dfp', 'path': '/', 'secure': False, 'value': 'a0eb5d872e91714229a1c52b7cd39b5a5c437a2d54442544563717c02d210c6b16@1583557045992@1582261046992'}]
cookie = {}
for i in cookies:
	cookie[i["name"]]=i["value"]
ss = urllib.parse.urlencode(cookie)
print(ss)
for num in range(1,16):
	print("第{}页".format(num))
	time.sleep(3)
	try:
		url = 'https://pcw-api.iqiyi.com/search/video/videolists?access_play_control_platform=14&channel_id=3&data_type=1&from=pcw_list&is_album_finished=&is_purchase=&key=&market_release_date_level=&mode=4&pageNum={}&pageSize=48&site=iqiyi&source_type=1&three_category_id=70;must&without_qipu=1'.format(num)
		res = requests.get(url,cookies = cookie)
		k = json.loads(res.text)
		for a in k["data"]["list"]:
			print(a["name"])
	except:
		print("出现错误！！！")
#		print(cookie)
