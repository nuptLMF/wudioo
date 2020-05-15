import pandas as pd
import numpy as np
from pandas_datareader import data, wb # 需要安装 pip install pandas_datareader
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


start = datetime.datetime(2019,8,1)
end = datetime.date.today()

cnpc = data.DataReader("601857.SS","yahoo",start, end)
a = cnpc.describe()


print(a)