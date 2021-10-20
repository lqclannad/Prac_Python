# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/20 19:27
# 文件名称: func_img.py
# 开发工具: Pycharm
import matplotlib.pyplot as plt
import numpy as np

_x = [_ for _ in range(-10, 10)]
'''
_y = [x**2 for x in _x]
_y = [x**3 for x in _x]
_y = [2*x-2 for x in _x]
_y = [1/(1+np.e**(-x)) for x in _x]
_y = [(np.e(x)-np.e(-x))/(np.e(x)+np.e(-x)) for x in _x]
func函数：x**2、x**3、2x-2、sigmod、tanh
'''
_y = []
plt.plot(_x, _y)
plt.show()

