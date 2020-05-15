import requests  #abc
from bs4 import BeautifulSoup  #abc
import time

def Page_download(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    content = requests.get(url,headers = headers)
    content.encoding='utf-8'
    return content.text

def Web_message(html):
    soup=BeautifulSoup(html,'html.parser')
    Link = soup.find(class_= 't z')
    Links = Link.find_all('tr',align = 'center')
    count = 0
    for i in Links:
        try:
            con = i.find('h3').find('a')
            link = con['href']
            URL='http://e1.zxhgqgp.info/pw/'+link
            titles = con.text
            save_text(titles,Download_message(Page_download(URL)),'\n')
            count = count+1
            print(count)
        except:
            pass

def Download_message(html):
	soup = BeautifulSoup(html,'html.parser')
	LoadLink = soup.find('div',class_='tpc_content').find('a')['href']
	return LoadLink


def save_text(*args):
    for i in args:
    	with open('E:\practise_01\save_text\website_04.txt', 'a', encoding='utf-8') as f:
    		f.write(i)

def main():
	for j in range(157,325):
	    url = "http://e1.zxhgqgp.info/pw/thread.php?fid=18&page={}".format(j)
	    print('第{}页'.format(j))
	    pages = Page_download(url)
	    Web_message(pages)

if __name__ == '__main__':
	main()