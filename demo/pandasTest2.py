import pandas as pd
import numpy as np
import os
print('****************************************************************')

#打开文件
df = pd.read_excel('/Users/gaowenguo/Desktop/PythonStudy/demo/connect.xlsx')
#01 基于位置（数字）的索引
#print(df.iloc[2,3])
#要想选取0-12的索引行，我们得输入“0:13”，列想要全部选取，则输入冒号“：”即可。
#按条件索引/筛选 loc
#print(df.iloc[0:6,:])
#print(df.iloc[:,0:3])
#print(df.loc[df['部门']=='研发三部',:])
print(df)

#保存excel文件
#df.to_excel('/Users/gaowenguo/Desktop/PythonStudy/demo/connect.xlsx') 