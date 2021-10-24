# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 14:55
# 文件名称: test01.py
# 开发工具: Pycharm
import numpy as np
import torch

a = np.array(1)
print(type(a))
print(a)
print(a.shape)
print(a.ndim)

b = torch.tensor(2)
print(b)
print(b.shape)
'''
numpy - array - 数组
torch - tensor - 张量
0维数组和张量
'''
