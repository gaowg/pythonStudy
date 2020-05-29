#导入工具包
import pandas_datareader as pdr
#获取阿里巴巴股票数据
alibaba = pdr.get_data_yahoo("BABA")
#显示数据前5行
print(alibaba.head())