# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/12 22:15
# 文件名称: test02.py
# 开发工具: Pycharm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 三维画点
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
z = np.random.normal(0, 1, 100)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z)
plt.show()

# 二维散点图
'''
n = 1000
x = np.random.randn(n)
y = np.random.randn(n)
plt.scatter(x, y)
plt.show()
'''
