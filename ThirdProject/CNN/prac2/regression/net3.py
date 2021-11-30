# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/30 17:42
# 平台: PyCharm
# 文件名: net3.py
import numpy as np
import torch
from torch import nn


class Classification_Regression(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3,48,(3,3)),
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

        self.layer2 = nn.Sequential(
            nn.Conv2d(3, 48, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(48, 96, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(96, 192, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(192, 384, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(384, 512, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(512, 784, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(784, 784, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(784, 784, (3, 3)),
            nn.ReLU()
        )

        self.out_layer2 = nn.Sequential(
            nn.Linear(784, 4),
            nn.Sigmoid()
        )

    def forward(self,x):
        out = self.layer1(x)
        out = out.reshape(-1,784)
        exist_Minions = self.out_layer1(out)
        exist_Minions = torch.gt(exist_Minions, 0.5).permute(1,0)[0]
        print("exist_Minions:",exist_Minions)
        print("x[exist_Minions]:",x[exist_Minions])
        print("X.shape:",x.shape)
        x = x[exist_Minions]
        out2 = self.layer2(x)
        out2 = out2.reshape(-1, 784)
        return exist_Minions, self.out_layer2(out2)


if __name__ == '__main__':
    net = Classification_Regression()
    x = torch.randn(10,3,300,300)
    y1, y2 = net(x)
    print(y2)
    print(y2.shape)

