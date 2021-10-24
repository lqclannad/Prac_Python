# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 15:32
# 文件名称: test08.py
# 开发工具: Pycharm
import numpy as np

x = np.array([[3], [1], [6]])
y = 4 * x

print(x)
print(y)

print("=================")
# np.linalg.inv(array) - 矩阵求逆
# np.linalg.det(array) - 矩阵求行列式
print(np.linalg.inv(x.T@x)@x.T@y)
# np.linalg.norm(array) - 矩阵求模长
print(np.linalg.norm([1, 1]))
'''
矩阵求逆求模长
'''
