import pandas as pd
import numpy as np 
 
#对于series的数据选择
ser_data=pd.Series(np.random.rand(4),index=[1,2,3,4])

#对于series进行索引查询
#如上所示由于其中存在数值索引，分为显式索引loc与隐式索引iloc

#loc
print('显式索引')
print(ser_data.loc[1])#取到index为1的数

#iloc
print('隐式索引')
print(ser_data.iloc[1])

#判断索引是否存在
print(ser_data.keys())#获得字典的key
print(1 is ser_data)#查询是否存在key

#Dataframe数据索引
#对于Dataframe索引主要分为三类，1、对标签进行索引；2、对数据进行切片
DF_data=pd.DataFrame(np.random.rand(2,3),columns=['are','2','3'],index=[1,2])

#1、对标签进行索引；
print("标签索引")
print(DF_data.iloc[1,1])#同样可以使用loc,iloc作为显/隐式索引
print(DF_data.are)#同时可以将列名作为属性进行显示，但不可与方法重合

#2、对数据进行切片
print("数值索引")#使用Dataframe。value相当于转化为二维数组
print(DF_data.values[1,1])



print(ser_data)
