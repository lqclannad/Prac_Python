# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/30 18:03
# 平台: PyCharm
# 文件名: net2.py
import torch
from torch import nn


class Classification(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1,48,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(48,96,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(96,192,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(192,384,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(384,512,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(512,784,(3,3)),
            nn.ReLU(),
            nn.Conv2d(784,784,(3,3)),
            nn.ReLU(),
            nn.Conv2d(784,784,(3,3)),
            nn.ReLU()
        )

        self.out_layer1 = nn.Sequential(
            nn.Linear(784,1),
            nn.Sigmoid()
        )

    def forward(self,x):
        out = self.layer1(x)
        out = out.reshape(-1,784)
        return self.out_layer1(out)


class Regression(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer2 = nn.Sequential(
            nn.Conv2d(1,48,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(48,96,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(96,192,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(192,384,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(384,512,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(512,784,(3,3)),
            nn.ReLU(),
            nn.Conv2d(784,784,(3,3)),
            nn.ReLU(),
            nn.Conv2d(784,784,(3,3)),
            nn.ReLU()
        )

        self.out_layer2 = nn.Sequential(
            nn.Linear(784,4),
            nn.Sigmoid()
        )

    def forward(self,x):
        out = self.layer2(x)
        out = out.reshape(-1,784)
        return self.out_layer2(out)


if __name__ == '__main__':
    net1 = Classification()
    x = torch.randn(10,1,300,300)
    y = net1(x)
    print(y)
    print(y.shape)
    tmp = []    # 存储有小黄人的图像集
    for i,t in enumerate(y):
        if t > 0.5:
            tmp.append((y[i],torch.randn(1,1,300,300)))
    net2 = Regression()
    for y in tmp:
        z = net2(y[1])
        print(z)
        print(z.shape)


