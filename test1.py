import re
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *


with open('e:\\day2020_05_10.log','r',encoding = 'utf-8') as f:
	s = f.read()
num = re.findall("epoch: 1 step: (.*?), loss is (.*?)\n",s)
plt.figure(1)
x_label = [int(num[0][0])]
#t_now = 0
y_label = [float(num[0][1])]


for i in range(1,len(num)):
#    plt.clf() #清空画布上的所有内容
    x_label.append(int(num[i][0]))
    y_label.append(float(num[i][1]))
plt.xlabel("step")
plt.ylabel("loss")
plt.plot(x_label,y_label,'-r')
plt.show()
    

