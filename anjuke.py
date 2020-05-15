# -*- coding: utf-8 -*-
import requests
from lxml import etree
import re


def Request(url):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}  
    res = requests.get(url,headers = headers)
    return res.text


def Contents(html):
    item = {}
    htmls = etree.HTML(html)
    for i in range(1,61):
        titles = htmls.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[1]/a//text()'.format(str(i)))[0].replace(' ','').replace('\n','')
        rooms = htmls.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[2]/span[1]/text()'.format(str(i)))[0].replace(' ','').replace('\n','')
        mianji = htmls.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[2]/span[2]/text()'.format(str(i)))[0].replace(' ','').replace('\n','')
        floors = htmls.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[2]/span[3]/text()'.format(str(i)))[0].replace(' ','').replace('\n','')
        urls = htmls.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[1]/a/@href'.format(str(i)))[0]
        id_ = re.findall('view/(A\d+)',urls)[0]
        url_ = re.findall('(.*?){}'.format(id_),urls)[0]+id_
        try:
            niandai = htmls.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[2]/span[4]/text()'.format(str(i)))[0].replace(' ','').replace('\n','')
        except IndexError:
            niandai = '不祥'
        details2 = htmls.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[3]/span/text()'.format(str(i)))[0].replace(' ','').replace('\n','')
        xiaoqu = details2.split('\xa0\xa0')[0]
        dizhi = details2.split('\xa0\xa0')[1]
        price = htmls.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[3]/span[1]/strong/text()'.format(str(i)))[0]+'万'
        danjia = htmls.xpath('//*[@id="houselist-mod-new"]/li[37]/div[3]/span[2]/text()'.format(str(i)))[0]
#        print(i,'\n',titles,'\n',rooms,'\n',mianji,'\n',floors,'\n',niandai,'\n',xiaoqu,'\n',dizhi,'\n',price,'\n',danjia)
        item = {
            'id':id_,
            '标题':titles,
            '房间格局':rooms,
            '面积':mianji,
            '楼层':floors,
            '修建年代':niandai,
            '小区':xiaoqu,
            '地址':dizhi,
            '价格':price,
            '单价':danjia,
            '网址':url_,
            }
        yield item

def main():
    for i in range(1,51):
        url = 'https://nanjing.anjuke.com/sale/p{}/#filtersort'.format(1)
        r = Request(url)
        item = Contents(r)
        print("*"*10)
        print('第{}页'.format(i))
        print("*"*10)
        for a in item:
            print(a)

if __name__ =="__main__":
    main()