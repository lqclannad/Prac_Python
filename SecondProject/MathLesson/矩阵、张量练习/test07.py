# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 15:28
# 文件名称: test07.py
# 开发工具: Pycharm
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

b = a.T
print(b.shape)

c = a.dot(b)
print(c.shape)
'''
矩阵与自身的转置点乘后变成方阵
'''

