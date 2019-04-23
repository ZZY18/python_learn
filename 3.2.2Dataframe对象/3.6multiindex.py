#对于Dataframe类型的多级索引，主要用于创建多维数据的存储
#对于多维数据的建立

import pandas as pd 
import numpy as np 

#1、series
ser=pd.Series([np.random.rand(3,1),np.random.rand(3,1)],index=['ni','w'])
#建立多级索引
muliIdex=pd.MultiIndex.from_product([['a','b'],[1,2,3]])#建立索引
ser1=pd.Series(np.random.rand(6),index=muliIdex)#可以只给索引不给赋值，其中对多维series数据赋值时也只能是一维数组

mulicol=pd.MultiIndex.from_product([['a','b'],['c','d']],names=['1','2'])
muliidx=pd.MultiIndex.from_product([['f','g'],['h','l']])
DataF=pd.DataFrame(columns=mulicol,index=muliidx)
print(ser1)