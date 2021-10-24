# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 16:32
# 文件名称: test10.py
# 开发工具: Pycharm
import torch

x = torch.tensor([3.0], requires_grad=True)
y = x * 3 + 2

# 对x求导
y.backward()
print(x.grad)
'''
张量求导
'''