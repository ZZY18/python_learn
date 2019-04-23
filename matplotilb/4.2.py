import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

# p219配置图例（图标签legend）
# 对于多线图形标签
x=np.linspace(0,10,1000)
plt.plot(x,np.sin(x),'-r',label='Sin')
plt.plot(x,np.cos(x),'--b',label='Cos')
plt.legend(['Sin','Cos'])#通过数组大小可以控制输出标签数
plt.axis('equal')
plt.show()
#对于散点图不同大小标签设置
cities=pd.read_csv('california_cities.csv')
lat,lon=cities['latd'],cities['longd']
population,area=cities['population_total'],cities['area_total_km2']
sca=plt.scatter(lat,lon,s=area,c=np.log10(population),cmap='viridis',alpha=0.5)#如果直接建立数据标签会很大
plt.axis('equal')
plt.xlabel('latd')
plt.ylabel('lon')
plt.title('Area and Population')
plt.colorbar(label='poplation')

# 加上对图中大小的描述
for area in [100,300,500]:
    plt.scatter([],[],c='k',s=area,alpha=0.3,label=area)#其目的是建立label标签，其没有数据被显示
plt.legend(scatterpoints=1,frameon=False,labelspacing=1.5)#scatterpoints表示标注组数,labelspacing标注点之间的距离
plt.show()