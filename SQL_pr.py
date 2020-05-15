import pymysql
import os
weibos={
    "id":"4400430442090388",
    "attitudes_count":"62101",
    "comments_count":"10002",
    "crawled_at":"2019-08-22 19:34",
    "created_at":"2019-08-01 00:00",
    "picture":"http://wx3.sinaimg.cn/large/4cd09971gy1g5jziu2nfpj21420qowiq.jpg",
    "pictures":"https://wx3.sinaimg.cn/orj360/4cd09971gy1g5jziu2nfpj21420qowiq.jpg", 
    "raw_text":"null",
    "reposts_count":"4167",
    "source":"nova 5i Pro",
    "text_":"今晚在这等我 <a href='/n/PANDORA潘多拉珠宝'>@PANDORA潘多拉珠宝</a> <a  href=\"https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E5%A4%A9%E7%8C%AB%E8%B6%85%E7%BA%A7%E5%93%81%E7%89%8C%E6%97%A5%23&luicode=10000011&lfid=1076031288739185\" data-hide=\"\"><span class=\"surl-text\">#天猫超级品牌日#</span></a><a  href=\"https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E7%88%B1%E4%B8%8D%E5%8F%AF%E6%8C%A1%23&extparam=%23%E7%88%B1%E4%B8%8D%E5%8F%AF%E6%8C%A1%23&luicode=10000011&lfid=1076031288739185\" data-hide=\"\"><span class=\"surl-text\">#爱不可挡#</span></a> <a data-url=\"http://t.cn/RfdaBGE\" href=\"https://m.weibo.cn/p/index?containerid=1002212002174%253A66f8f1707a4d407f89333f067a2eb68f____RfdaBGE&extparam=followtopweibo&luicode=10000011&lfid=1076031288739185\" data-hide=\"\"><span class='url-icon'><img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_taobao_default.png'></span><span class=\"surl-text\">PANDORA潘多拉官方旗舰店</span></a>",
    "thumbnail":"http://wx3.sinaimg.cn/thumbnail/4cd09971gy1g5jziu2nfpj21420qowiq.jpg",
    "user":"1288739185",
}
datas={
    "id" : "4402289965993918",
    "attitudes_count" : 57824,
    "comments_count" : 10455,
    "crawled_at" : "2019-08-25 19:54",
    "created_at" : "2019-08-06 00:00",
    "picture" : "null",
    "pictures" : "null",
    "raw_text" : "祝Vogue生日快乐[蛋糕][憧憬]#国模之美#",
    "reposts_count" : "5413",
    "source" : "nova 5i Pro",
    "text_" : "祝Vogue生日快乐<span class=\"url-icon\"><img alt=[蛋糕] src=\"//h5.sinaimg.cn/m/emoticon/icon/others/o_dangao-57caf5f65f.png\" style=\"width:1em; height:1em;\" /></span><span class=\"url-icon\"><img alt=[憧憬] src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_xingxingyan-06a3ca0ae4.png\" style=\"width:1em; height:1em;\" /></span><a  href=\"https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E5%9B%BD%E6%A8%A1%E4%B9%8B%E7%BE%8E%23&extparam=%23%E5%9B%BD%E6%A8%A1%E4%B9%8B%E7%BE%8E%23&luicode=10000011&lfid=1076031288739185\" data-hide=\"\"><span class=\"surl-text\">#国模之美#</span></a>",
    "thumbnail" : "null",
    "user" : 128873913,
}



db = pymysql.connect(host='ngrok.xfl.host',port=13306,user='developer',password='ignorance',db='weibo')#,charset='utf-8'
cursor = db.cursor()

#sql1 = 'CREATE TABLE IF NOT EXISTS users(id VARCHAR(255) NOT NULL,avatar VARCHAR(255) NOT NULL,cover VARCHAR(255) NOT NULL,crawled_at VARCHAR(100) NOT NULL,description VARCHAR(100) NOT NULL,fans_count VARCHAR(100) NOT NULL,follows_count VARCHAR(100) NOT NULL,gender VARCHAR(100) NOT NULL,name VARCHAR(255) NOT NULL,verified VARCHAR(100) NOT NULL,verified_reason VARCHAR(255) NOT NULL,verified_type VARCHAR(255) NOT NULL,weibos_count VARCHAR(255) NOT NULL,PRIMARY KEY (id))'
'''
sql0 = 'CREATE TABLE IF NOT EXISTS weibos(id VARCHAR(255) NOT NULL,attitudes_count VARCHAR(255) NOT NULL,comments_count VARCHAR(255) NOT NULL,crawled_at VARCHAR(255) NOT NULL,created_at VARCHAR(255) NOT NULL,picture VARCHAR(255) NOT NULL,pictures VARCHAR(255) NOT NULL,raw_text VARCHAR(255) NOT NULL,reposts_count VARCHAR(255) NOT NULL,source VARCHAR(255) NOT NULL,text_ VARCHAR(1255) NOT NULL,thumbnail VARCHAR(255) NOT NULL,user VARCHAR(255) NOT NULL,PRIMARY KEY (id))'
cursor.execute(sql0)
#cursor.execute(sql1)
cursor.close()
'''
'''
table = 'weis'
keys = ','.join(weibos.keys())
values = ','.join(['%s']*len(weibos))

sql1 = 'INSERT INTO {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)

try:
    cursor.execute(sql1,tuple(weibos.values()))
    print('successful')
    db.commit()
except:
    print('failed')
    db.rollback()
db.close()
'''

table = 'weibos'
keys = ', '.join(weibos.keys())
values = ', '.join(['%s']*len(datas))

sql2 = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
update = ','.join([" {key}=%s".format(key=key) for key in weibos])
sql2 += update
try:
    if cursor.execute(sql2,tuple(weibos.values())*2):
        print('successful')
        db.commit()
except:
    print('failed')
    db.rollback()
db.close()


print(sql2)

print(tuple(weibos.values()))


'''
#    cursor.execute(sql1,(id,user,age))
#    print('successful')
#    db.commit()
#except:
#    print('failed')
#    db.rollback()
#db.close()
#sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
#update = ','.join([" {key} = %s".format(key=key) for key in data])
#sql += update
#try:
#    if cursor.excute(sql,('20120001', 'bob', '21', '20120001', 'bob', '21')):
#        print('successful')
#        sql_db.commit()
#except:
#    print('failed')
#    sql_db.rollback()
#sql_db.close()
'''