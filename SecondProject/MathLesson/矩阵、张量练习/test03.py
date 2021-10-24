# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 15:12
# 文件名称: test03.py
# 开发工具: Pycharm
import numpy as np
import torch

a = np.array([[1, 2, 3], [4, 5, 6]])
print(type(a))
print(a)
print(a.shape)
print(a.ndim)

b = torch.tensor([[1, 2], [3, 4], [5, 6]])
print(b)
print(b.shape)
'''
2维数组和张量
'''
