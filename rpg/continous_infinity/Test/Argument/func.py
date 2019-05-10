import matplotlib.pylab as plt
import numpy as np

plt.figure(figsize=(6,4))
x= np.linspace(-2 * np.pi,2 * np.pi,100)
y= np.sin(x)
y1 = np.cos(x)

plt.ylim(-3,3)#限制X轴坐标范围
plt.xlim(-4,4)

plt.xlabel("X")#X轴名称
plt.ylabel("Y")#Y轴名称
plt.title("sinx & cosx")#图像标题
plt.xticks((-2 * np.pi,-np.pi,0,np.pi))#设置X轴刻度

plt.plot(x,y,label= "sinx")#根据函数坐标绘制折线图
plt.plot(x,y1,label = "cosx")

plt.annotate('sin(np.pi)=',xy=(-np.pi,0),xytext = (-np.pi,2),fontsize=16,arrowprops= dict(facecolor = 'black',shrink=0.01))#设置注解

plt.text(1,1,"Text",fontdict={'size':16,'color':'r'})
plt.legend()
plt.show()
--------------------- 
作者：一只有情调的程序猿 
来源：CSDN 
原文：https://blog.csdn.net/weixin_42880774/article/details/83856953 
版权声明：本文为博主原创文章，转载请附上博文链接！