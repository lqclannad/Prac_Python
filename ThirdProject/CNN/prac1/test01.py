# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/24 16:32
# 平台: PyCharm
# 文件名: test01.py
from torch import nn
import torch

layer = nn.Conv2d(3,12,(3,3),stride=1,padding=1)
print(layer.weight)
print(layer.bias)
print("===========================")
pool = nn.MaxPool2d(3)
x = torch.randn(1,3,5,5)
print("x:",x)
print("===========================")
y = layer(x)
print(y)
print(y.shape)
print("===========================")
y = pool(y)
print(y)
print(y.shape)