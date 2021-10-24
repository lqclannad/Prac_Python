# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 16:29
# 文件名称: test09.py
# 开发工具: Pycharm
import numpy as np
import torch

a = np.array([[1, 2], [3, 4]])
print(np.linalg.det(a))

b = torch.tensor([[1., 2.], [3., 4.]])
print(b.det())
'''
求矩阵/张量的行列式
'''
