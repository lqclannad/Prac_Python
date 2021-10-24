# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 15:23
# 文件名称: test06.py
# 开发工具: Pycharm
import numpy as np
import torch

# 方阵
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a)
#
# b = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(b)

# a = np.zeros((2, 3))
# print(a)
# b = np.ones((2, 3))
# print(b)
#
# c = torch.zeros(2, 3)
# print(c)
# d = torch.ones(2, 3)
# print(d)

# 单位矩阵
# a = np.eye(3, 4)
# print(a)
#
# b = torch.eye(3, 4)
# print(b)

# 下三角矩阵
# a = np.tri(4, 4)
# print(a)
#
# b = torch.tril(torch.ones(4, 4))    # 先放入一个张量，再将张量变成三角矩阵
# print(b)

# 对角矩阵
a = np.diag([1, 2, 3, 4])
print(a)

b = torch.diag(torch.tensor([1, 2, 3, 4]))
print(b)
'''
一些特性矩阵/张量
'''
