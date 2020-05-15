import requests
from urllib.parse import urlencode

headers = {
	'Host':'zhaopin.baidu.com',
	'Referer':'https://zhaopin.baidu.com/?city=%E5%8D%97%E4%BA%AC',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}
cookie = 'BAIDUID=C272AD8808694BBC37A8742D03919C28:FG=1; BIDUPSID=C272AD8808694BBC37A8742D03919C28; PSTM=1559364502; delPer=0; PSINO=3; Hm_lvt_4b55f5db1b521481b884efb1078a89cc=1560938500; Hm_lpvt_4b55f5db1b521481b884efb1078a89cc=1560938500; BDRCVFR[SaXdSMkdNXD]=I67x6TjHwwYf0; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[tFA6N9pQGI3]=mk3SLVN4HKm; BCLID=11650752623254613795; BDSFRCVID=cE8OJeC624oe5TrwWG3ZUJ9S-pwMTt3TH6aoXgp5scBQkp1mD8AzEG0PDx8g0KA-S2-HogKKL2OTHm_F_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJIO_KPKtC83fP36qR6sMJ8thmT22-us56kj2hcH0KLKMhPGXb7K5p-1D-nPBjcgHC3hLh7sJfb1MRjVX4CW3j01WR6Bexb2QmvJQl5TtUJqSDnTDMRh-RKSyxryKMniBnr9-pnEXhQrh459XP68bTkA5bjZKxtq3mkjbIOFfDD5bKDmD603bDCV-frb-C62aKDs3hKyBhcqEIL4j-nqjq0X5nJxJhTPWJ5gs4J5BxbMhUbSj4QoW--Qjqb23qoW-n6LKInpMq5nhMJe257JDMPFqJ-Hexvy523i2IovQpnV_pQ3DRoWXPIqbN7P-p5Z5mAqKl0MLIOkbRO4-TFMj5OBDM5; __ag_cm_=1; ag_fid=WpEoJRQ6SkilLHyF; ZP_FR=aladdin-5463-zp_exact_new; Hm_lvt_da3258e243c3132f66f0f3c247b48473=1560937959,1560951475; Hm_lpvt_da3258e243c3132f66f0f3c247b48473=1560952407; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; pgv_pvi=8895107072; pgv_si=s7464550400; ZD_ENTRY=baidu; BDUSS=ENadERpUm1Ob3NEanFTNWVvQm5HWWw4ZVN5Z2cxLU1qNjRSZ3RJYksxZTkwVEZkSUFBQUFBJCQAAAAAAAAAAAEAAACDJLOeAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL1ECl29RApda'
cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}
param = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': 1
    }

base_url1 = 'https://zhaopin.baidu.com/api/qzasync?'
def token_url(page:int):

	params = {
		'query':'python',
		'city':'%E5%8D%97%E4%BA%AC',
		'is_adq':'1',
		'pcmod':'1',
		'token':'==AlTzqpH3apGWIcVWpZW6mlZa2kYdlZTWpamtWnjlGa',
		'pn':page*10,
		'rn':'10'
		}

	url = base_url1+urlencode(params)
	return url

count = 0
for i in range(20):
	try:
		r = requests.get(token_url(i),headers=headers,cookies = cookie_dict)
		r.encoding = 'utf-8'
		json = r.json()
		try:
			if json:
					items = json.get('data').get('disp_data')
					for item in items:
						job = {}
						job['name'] = item.get('name')
						job['city'] = item.get('city')
						job['salary'] = item.get('ori_salary')
						job['time'] = item.get('lastmod')
						print(job)
						count = count+1
		except AttributeError:
			print('*'*20)
			print('碰到一条广告出现错误')
			print('*'*20)
	except :
		print('此关键词爬取完毕')
		print('一共爬取信息{}条'.format(count-1))
		break
