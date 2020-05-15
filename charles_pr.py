import requests
import time
import urllib 
i = 3
j=i-1

url = "https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_ksTS=1576766698750_2238&callback=jsonp2239&q=U%E7%9B%98&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20191219&ie=utf8&bcoffset=-9&ntoffset=-3&p4ppushleft=1%2C48&s={}".format(48*i,48*j)
headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
cookies= {
	"thw":"cn",
	"cna":"80bYFQc3BKOCaxLeEupwkfxe",
	"t":"e7e555af32aed0506d7121d0bdb1da6c",
	"lgc":"lvmingfu007",
	"tracknick":"lvmingfu007",
	"tg":"0",
	"uc3":"vT3=F8dbyuS%2f4PoC%2F%2B7w9dS%3d&iD2=VAKO5VBBlLos&lG2=VFC%2Fuz9Ayeyq2G%3D%3d&nK2=D9WZS0jKzY%2b3la4%3D",
	"uc4":"id4=0%40VHvCOxO7ZQ7ZBLGYAD9JBiPivRG%3d&nk4=0%40dfBWpEr7IjrX62VSHDY7C4TQ688CbG%3D%3D",
	"_cc_":"URm48SYIZQ%3D%3D",
	"enc":"ysn5wf98uJFKy0sjSmQ%2ffVH%2FLj9IxFY0HVG4y7Oqx9xaAIk6nyTiTKljEdr86OQhMVJ7vbRlqC%2frotKXPcgVnG%3D%3D",
	"hng":"CN%7CZH-CN%7CCNY%7C156",
	"_m_h5_tk":"370a7139e4e2bd1c8fc88efbeab86cbc_1576236257432",
	"_m_h5_tk_enc":"a52ddf4723cdf4e92cb52b38c7ab1f82",
	"mt":"ci=-1_0",
	"v":"0",
	"cookie2":"74e99232f10a317e799581619e346293",
	"_tb_token_":"ebe331755e8ad",
	"alitrackid":"www.taobao.com",
	"lastalitrackid":"www.taobao.com",
	"JSESSIONID":"C1DC4112E4661678D930BB4574AB6518",
	"uc1":"cookie14=uoTBM8AmW8H9VA%3D%3D",
	"isg":"bc4ufY5S_-K28QSWGbX0o8a6f4QWH_JoQ1wyDLJ3fTHsO8yvY7YoOZz99-dy4-pB",
	"l":"dboPgzVGQVvW5LJjBOfNCuI8A17OmirBzsPzW4_G2ICPOJCW5FLVwZlG5VyXCNgvhsaEz3J4RKmJBQynyYhqjxpsw3k_J_vE3dC..",
}


res= requests.get(url,cookies = cookies,headers = headers)

print(res.text)