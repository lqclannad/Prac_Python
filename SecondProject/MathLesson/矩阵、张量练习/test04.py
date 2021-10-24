# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 15:14
# 文件名称: test04.py
# 开发工具: Pycharm
import numpy as np
import torch

a = np.array([[[1, 2], [3, 4]]])
print(type(a))
print(a)
print(a.shape)
print(a.ndim)

b = torch.tensor([[[1, 2], [3, 4]]])
print(b)
print(b.shape)
'''
3维数组和张量
'''
