# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/16 14:58
# 文件名称: tst1.py
# 开发工具: Pycharm
import PIL.Image
import torch

a = torch.Tensor([[285.8558, 287.5629, 289.7778, 227.7385, 229.3761, 230.0974],
        [  4.8432,   3.2671,   3.3201, 559.5891, 559.1429, 558.7172],
        [297.9180, 300.5203, 302.0245, 236.9349, 238.9687, 239.6904],
        [ 20.2777,  20.1089,  19.3185, 571.4871, 571.8381, 571.4153],
        [  0.9559,   0.8702,   0.8775,   0.6383,   0.8196,   0.6042]])
b = torch.Tensor([[2.8558, 287.5629, 289.7778, 227.7385, 229.3761, 230.0974],
        [  14.2,   3.2671,   3.3201, 559.5891, 559.1429, 558.7172],
        [29.9180, 300.5203, 302.0245, 236.9349, 238.9687, 239.6904],
        [120.2777,  20.1089,  19.3185, 571.4871, 571.8381, 571.4153],
        [ 20.9559,   0.8702,   0.8775,   0.6383,   0.8196,   0.6042]])
# numpy -> copy  ,  torch -> clone
# print(torch.hstack([torch.Tensor([]),b]))
# print(torch.hstack([a,b]))
# print(a.clone())
img = PIL.Image.open("../img/1.jpg")
x1 = torch.Tensor([200,400])
x2 = torch.Tensor([600,500])
img = img.crop((x1.item(),x1.item(),x2.item(),x2.item()))
img.show()
print(img)
print(img.size)
print(type(img))
