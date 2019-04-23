import pandas as pd
import numpy as np
area_dict={'california':423967,'texas':695662,'new york':141297,
            'florida':170312,'illinois':149995}#字典类型数据
area_pd=pd.Series(area_dict)
state=pd.DataFrame({'area':area_pd})#相当与字典的字典，必须使用{}将所有类别包括
#对于DataFrame类型数据其中分别存在columns与index分别代表着列、行标签

#创建方式
#1由series创建，注意相当于字典，同时其中定义列->series定义行，Dataframe定义列

#2由字典定义
DataF1=pd.DataFrame([{'a':1,'b':2},{'a':2,'c':3}])#其中在字典数组中，没一个字典相当与一行数据，其中标签为列
#当两行数据之间存在不同列时会广播同时对于空缺至补NaN值

#3由numpy类型建立
DataF2=pd.DataFrame(np.random.rand(3,2),columns=['a','b'],index=['1','2','3'])
#当不定义columns与index的时候自动会赋值0,1,2-
#通过对numpy操作可以实现dataframe多类数据

#注对于标签建立
ind=pd.Index([1,2,3])
#使用标签
DataF3=pd.DataFrame(np.random.rand(3,3),columns=ind,index=ind)
print(DataF3)


#对于DataFrame索引,对其索引形式为Dataframe[col][index]
# print(state['area'])
# print(state['area']['florida'])
# print(area_dict)
