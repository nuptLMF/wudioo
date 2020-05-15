import time
from io import BytesIO
from PIL import Image
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import listdir
from os.path import abspath, dirname


TEMPLATES_FOLDER = dirname(abspath(__file__)) + '/pictures/'

d = listdir(TEMPLATES_FOLDER)
tem = Image.open(TEMPLATES_FOLDER+d[0])
pic1 = tem.load()
pic = []

for x in range(tem.size[0]):
	for y in range(tem.size[1]):
		pic.append(pic1[x,y])
print(tem.size)
print(tem)
#print(pic)
