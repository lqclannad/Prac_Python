# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/22 22:05
# 文件名称: test01.py
# 开发工具: Pycharm
from torch import jit

from ThirdProject.MLP.prac2.net import net_v1
import torch

# a = torch.tensor([45])
# a = torch.Tensor([45])
# print(a.dtype)
# b = torch.softmax(a,dim=0)
# print(b)
# print(torch.sum(b))

a = torch.Tensor([1,2,45])
b = torch.Tensor([1,5,45])
print(torch.sum(torch.eq(a,b).float()/a.shape[0]))
print(torch.mean(torch.eq(a,b).float()))
print(torch.exp(torch.Tensor([1,2,3])))

# a = torch.Tensor([2])
# print(a/2)
# print(a.item()/2)

# if __name__ == '__main__':
#     model = net_v1()
#     model.load_state_dict(torch.load("param/10.pt"))
#
#     # 虚拟一个输入
#     input = torch.randn(1, 784)
#     # 将模型和权重打包
#     tsm = jit.trace(model,input)
#     tsm.save("mnist.pt")
