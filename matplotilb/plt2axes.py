# 比较plt与axes做比较
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

x=np.linspace(0,10,1000)
# 在此使用 plt编程
plt.subplot(2,1,1)
plt.plot(x,np.sin(x),'-r',label='123')
plt.subplot(2,1,2)
plt.title('plt')
plt.plot(x,np.cos(x),'--r',label='Cos')
plt.legend()
plt.show()

#在此使用axes
fig,axes=plt.subplots(2,1)
axes[0].plot(x,np.sin(x),'-r',label='Sin')
axes[1].plot(x,np.cos(x),'--r',label='cos')
axes[0].legend()
plt.show()

# 通过上面我们不难看出1、对于plt的生命周期只到下一个plt的出现，在单一图像处理中没有问题甚至与更为方便
# 对于面对对象axes中其生命周期更长且可对于多图像问题中方便选择，在对易于标号，在多图像中使用面向对象更好