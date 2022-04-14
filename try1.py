# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 15:01:03 2021

@author: LIGHT CHASER
"""
from numpy.ma import sin,exp,cos
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def functions (a,b):
    c = (100 * a**2+100 * b**2)/10000
    return c

def graph (x,globalbest_x,X,Y,Z):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x[:,0], x[:,1], y,alpha = 0.2)
    ax.scatter(globalbest_x[0],globalbest_x[1],functions(globalbest_x[0],globalbest_x[1]),cmap = 'summer',alpha = 1)
    ax.plot_surface(X, Y, Z,alpha=0.15,cmap='winter')
    plt.savefig('C:/Users/LIGHT CHASER/Desktop/figure/figure_{}'.format(k), format='jpg', dpi=100, pad_inches=0)

#rd = np.random.RandomState(np.random.randint(0,100000)) #设置随机数种子
rang = 100#散点图范围
time = 1#绘制连续图像大于散点图的范围倍数，检验散点图的误差
E = 0.000001#误差允许范围
maxnum = 10#最大迭代次数
narvs = 2#目标函数的自变量个数
particlesize = 50#粒子群规模
c1 = 3#每个粒子的个体学习因子，加速度常数
c2 = 2#每个粒子的社会学习因子，加速度常数
w = 0.6#惯性因子
vmax = 10#粒子的最大飞翔速度

v = 2*np.random.rand(particlesize,narvs) #粒子飞翔速度，为particlesize*narvs的矩阵
x = -rang + 2*rang*np.random.rand(particlesize,narvs)#粒子所在位置，为particlesize*narvs的矩阵
y = functions(x[:,0],x[:,1])

personalbest_x = x
personalbest_faval = y
globalbest_faval = min(personalbest_faval)
s = np.argmin(personalbest_faval)
globalbest_x = personalbest_x[s,:]

f = []
ff = [0]
k = 1
while k<=maxnum:
    
    f=functions(x[:,0],x[:,1])
    X = np.arange(-time*rang, time*rang, 0.25)
    Y = np.arange(-time*rang, time*rang, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = functions(X,Y)
    
    graph(x,globalbest_x,X,Y,Z)

    for i in range(0,particlesize):
        if f[i]<personalbest_faval[i]:
            personalbest_faval[i] = f[i]
            personalbest_x[i,:] = x[i,:]
    globalbest_faval = min(personalbest_faval)
    s = np.argmin(personalbest_faval)
    globalbest_x = personalbest_x[s,:]
    for i in range(0,particlesize):
        v[i,:] = w*v[i,:]+c1*np.random.rand()*(personalbest_x[i,:]-x[i,:])+c2*np.random.rand()*(globalbest_x-x[i,:])
        for j in range(0,narvs):
            if v[i,j]<-vmax:
                v[i,j]=-vmax
            elif v[i,j]>vmax:
                v[i,j]=vmax
        x[i,:] = x[i,:] + v[i,:]
    ff = np.append(ff,globalbest_faval)
    #if globalbest_faval<E:#若全局最优值小于误差值，则跳出循环
        #break
    k = k+1
xbest = globalbest_x#全局最优解
ff[0] = ff[1]#第零次迭代默认值为第一次
xx = np.arange(0,k,1)
print(k-1)#迭代次数输出
