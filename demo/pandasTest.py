import pandas as pd
import numpy as np
import os
print('****************************************************************')
#print(dir(pd))

print(os.__dir__)

#print( np.random.rand(3,4))
#构造DataFrame最常用的方式是字典+列表，语句很简单，先是字典外括，然后依次打出每一列标题及其对应的列值（此处一定要用列表）
#df1 = pd.DataFrame({'工资':[5000,6000,7000,8500],'绩效分':[60,70,80.,65],'备注':['不及格','及格','良好','优秀']},index=['老王','小刘','小赵','老公'])
#print(df1)

#打开文件
df2 = pd.read_excel('/Users/gaowenguo/Desktop/PythonStudy/demo/connect.xlsx')
#df2.head(5)
#显示各列数据的类型，以及缺失情况
print(df2.info())   

#增加一列，用df['新列名'] = 新列值的形式，在原数据基础上赋值即可：
df2['demo']=range(1,len(df2)+1)
#print(df2[['姓名','手机号码','demo']])  #显示多列

#选择列
#print(df2['姓名'])  #显示一列
#print(df2[['姓名','手机号码']])  #显示多列
#print(df2[['姓名','手机号码','demo']])  #显示多列

#删：
#我们用drop函数制定删除对应的列，axis = 1表示针对列的操作，inplace为True，则直接在源数据上进行修改，否则源数据会保持原样。
df2.drop('demo',axis=1,inplace=True)


#保存excel文件
#df2.to_excel('/Users/gaowenguo/Desktop/PythonStudy/demo/connect.xlsx') 

#快速计算数值型数据的关键统计指标，像平均数、中位数、标准差等等。
#只针对数值型的列。其中count是统计每一列的有多少个非空数值，mean、std、min、max对应的分别是该列的均值、标准差、最小值和最大值，25%、50%、75%对应的则是分位数。
#print(df2.describe())
