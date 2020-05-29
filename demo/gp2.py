#先引入后面可能用到的包（package）
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
#正常显示画图时出现的中文
from pylab import mpl
#这里使用微软雅黑字体
mpl.rcParams['font.sans-serif']=['SimHei']
#画图时显示负号
mpl.rcParams['axes.unicode_minus']=False
import seaborn as sns  #画图用的
import tushare as ts
#Jupyter Notebook特有的magic命令
#直接在行内显示图形
#matplotlib inline    

sh=ts.get_k_data(code='300098',ktype='D',
  autype='qfq', start='2010-04-20')
#code:股票代码，个股主要使用代码，如‘600000’
#ktype:'D':日数据；‘m’：月数据，‘Y’:年数据
#autype:复权选择，默认‘qfq’前复权
#start：起始时间
#end：默认当前时间
#查看下数据前5行
print(sh.head(5))

#将数据列表中的第0列'date'设置为索引
sh.index=pd.to_datetime(sh.date) 
#画出上证指数收盘价的走势
sh['close'].plot(figsize=(12,6))
plt.title('gxx 2019-2020年走势图')
plt.xlabel('日期')
plt.show()

#pandas的describe()函数提供了数据的描述性统计
#count:数据样本，mean:均值，std:标准差
print(sh.describe().round(2))

#再查看下每日成交量 
#2006年市场容量小，交易量比较小，我们从2007年开始看
sh.loc["2007-01-01":]["volume"].plot(figsize=(12,6))
plt.title('上证指数2007-2018年日成交量图')
plt.xlabel('日期')
plt.show()