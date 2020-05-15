import re


aa = '3|2|3|1200PCS飞利浦牌'

s = re.findall('\d+PCS',aa)
print(s)