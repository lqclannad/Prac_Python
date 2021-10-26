# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/26 16:32
# 平台: PyCharm
# 文件名: requires_grad_test.py
import torch
from torch.autograd import Variable

x = Variable(torch.randn(5,5))
y = Variable(torch.randn(5,5))
z = Variable(torch.randn(5,5), requires_grad=True)
a = x + y
print(a.requires_grad)
a.requires_grad = True
print(a.requires_grad)
# 有一个参数的属性为自动求导，那么结果的属性也就为自动求导
b = a + z
print(b.requires_grad)
