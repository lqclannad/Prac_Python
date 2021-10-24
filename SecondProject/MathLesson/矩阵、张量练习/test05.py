# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 15:15
# 文件名称: test05.py
# 开发工具: Pycharm
import torch

a = torch.tensor([[[1, 2, 2], [3, 4, 3], [2, 1, 2], [3, 1, 3]]])
print(a)
print(a.shape)

b = torch.tensor([[[3, 1, 2], [3, 1, 3], [2, 2, 2], [3, 3, 3]]])
print(b)
print(b.shape)

c = torch.tensor([[[1, 2], [3, 4], [5, 6]]])
print(c)
print(c.shape)

print(a - b)
print(a * b)

print(a * 3)

# 张量乘法
d = torch.matmul(a, c)  # (1,4,3) * (1,3,2) = (1,4,2)
print(d)
print(d.shape)
'''
张量的运算
'''
