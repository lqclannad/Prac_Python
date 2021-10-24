# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 15:01
# 文件名称: test02.py
# 开发工具: Pycharm
import numpy as np
import torch

a = np.array([3, 2])
print(type(a))
print(a)
print(a.shape)
print(a.ndim)

b = torch.tensor([4, 4, 5])
print(b)
print(b.shape)
'''
1维数组和张量
'''
