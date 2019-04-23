
# -*- coding: utf-8 -*
# 导入matplotlit库并保存图片
#添加后可以在matplotile中显示中文
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

class name():
    """
    ok
    """
    def name():
        """
        在此写注释会被显示
        """     
        pass

    
from  matplotlib import pyplot as plt
import numpy as np 
x=np.linspace(0,10,10)
fig=plt.figure()
ax=plt.axes()
ax.plot(x,np.sin(x),'r')
ax.plot(x,np.cos(x),color='c')
plt.xlim(0,20)
plt.ylim(-5,5)
plt.show()
a=name()
a.name

# 绘制散点图
# 使用plt.plot绘制
plt.subplot(2,1,1)
plt.plot(x,np.sin(x),'-o')
# 对于plt.scatter其对于subplot的优势在于其可以对每个离散点进行操作，但是这也意味浪费大量的内存
plt.subplot(2,1,2)
plt.scatter(x,np.sin(x),s=x)
plt.show()

# 基本误差线表示
# 离散误差线
plt.subplot(2,1,1)
x1=np.linspace(0,10,100)
y1=np.sin(x1)+np.random.randn(100)
err=np.random.rand(100)
plt.errorbar(x1,y1,yerr=err,fmt='o',ecolor='r')#可以调节各点的误差值长度但是对于绘图格式不能修改
# 连续误差线,使用fill_bewteen来实现连续误差区间
modal=lambda x2:x2*np.sin(x2)
xdata=np.array([1,3,5,7,9])
ydata=modal(xdata)
plt.subplot(2,1,2)
plt.plot(x1,y1,'-r')
plt.fill_between(x1,y1-err/2,y1+err/2,color="gray",alpha=0.5)
plt.show()

# 对于频率直方图
# 对于一维问题
plt.subplot(2,1,1)
data1=np.random.normal(0.8,1.8,1000)
data2=np.random.normal(1,2,1000)
data3=np.random.normal(1.8,2.8,1000)
kwarge=dict(bins=40,normed=True,alpha=0.5,histtype='stepfilled')
plt.hist(data1,**kwarge)#使用normed可以实现标准化
plt.hist(data2,**kwarge)
plt.hist(data3,**kwarge)
plt.title("频率直方图",)
# 对于二维数据直方图
mean=[0,0]
cov=[[1,1],[1,2]]
[x,y]=np.random.multivariate_normal(mean,cov,1000).T
plt.subplot(2,1,2)
plt.hist2d(x,y,bins=40,cmap='Blues')#对于二维平面图使用cmap确定颜色
cb=plt.colorbar()#对于二维问题其中颜色的参数使用colorbar进行表示，同时实例化后可以对其各部操作
cb.set_label('count in bar')
plt.show()


