from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import requests
import redis
import json
import os
import pymongo
from lxml import etree

file_path="E:\practise_01\ceshi01\ceshi01.txt"

class JD_item(object):
	#初始化登陆账号：account和密码password，已经要搜索的关键字keywords
	def __init__(self,account,password,website = 'http://yes.youwinedu.com/#/login'):
		self.account = account
		self.password = password
		chromeOptions = webdriver.ChromeOptions()
		prefs = {"download.default_directory":"D:\\TT教案\\小学"}
		chromeOptions.add_experimental_option("prefs", prefs)
		self.browser = webdriver.Chrome(chrome_options=chromeOptions)
#		self.browser = webdriver.Chrome()

	def login(self):
		#初始化登陆，由于极验验证破解功能，这里需要进行手动滑块。
		self.browser.get('http://yes.youwinedu.com/#/login')
		self.browser.maximize_window()
		wait = WDW(self.browser,10)
		input = wait.until(EC.presence_of_element_located((By.ID,'login-name')))
		input.send_keys(self.account)
		input = wait.until(EC.presence_of_element_located((By.ID,'login-pass')))
		input.send_keys(self.password)
		input = self.browser.find_element_by_xpath('//*[@id="body"]/div[2]/div/div/div[1]/div[2]/form/ul[3]/input')
		input.send_keys("1234")
		time.sleep(2)
		button = self.browser.find_element_by_xpath('//*[@id="body"]/div[2]/div/div/div[1]/div[2]/form/ul[4]/button')
		button.click()
		time.sleep(3)
		self.browser.find_element_by_xpath('//*[@id="navbar"]/ul/li[7]/a').click()
		time.sleep(3)
		self.browser.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/div/div[1]/nav-side/ul/li[1]/a').click()
		time.sleep(3)
		s1 = Select(self.browser.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/div/div[2]/div[3]/select[1]'))
		s1.select_by_visible_text("初中")
		time.sleep(3)
		s2 = Select(self.browser.find_element_by_xpath('//*[@id="body"]/div[2]/div[2]/div/div[2]/div[3]/select[2]'))
		s2.select_by_visible_text("语文")
		time.sleep(5)

	def close(self):
		#关闭网页 
		self.browser.close()

	def next_page(self,number):
		wait = WDW(self.browser,10)
		input = wait.until(EC.presence_of_element_located((By.ID,'go_pg_num')))
		input.clear()
		input.send_keys(number)
		time.sleep(2)
		button = self.browser.find_element_by_xpath('//*[@id="mt_page"]/div/span')
		button.click()


	def response(self):
		#将目前浏览的网页源代码转换成html
		return etree.HTML(self.browser.page_source)


	def parse_item(self,num):
		#爬取的物品的名称，价格，物品的主页面网址
		res = self.response()
		name = os.listdir("D:\\TT教案\\语文")
		for i in range(1,11):
			items = res.xpath('//*[@id="body"]/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/div/div/div/div[1]/div[{}]/h3/a[1]/text()'.format(i))[0]
			if items in name:
				print("第{}页第{}个文件{}已存在".format(num,i,items))
			else:
				txt_write('第{}页第{}个文件{}未下载\n'.format(num,i,items))


def txt_read():
	with open(file_path,'rb') as f:
		a = f.read()
	return a

def txt_write(infos):
	with open(file_path,'a') as f:
		f.write(str(infos))

		

def main():
	jd_account = '15051883071' #----填入京东账号13776629330
	jd_pwd = '883071'   #----填入京东密码114065tt
#	item_word = 'adidas运动套装' #----填入你要搜索的物品名称
	JD = JD_item(jd_account,jd_pwd) 
	JD.login()
	cc = 0

	for j in range(177,355):
		try:
			JD.parse_item(j)
			JD.next_page(j)
			time.sleep(5)
		except:
			JD.close()
			txt_write(j)
			main()

if __name__=='__main__':
	main()