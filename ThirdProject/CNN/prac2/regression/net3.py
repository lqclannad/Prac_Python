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
        self.layer = nn.Sequential(
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

        self.out_layer = nn.Sequential(
            nn.Linear(784,5),
            nn.Sigmoid()
        )

    def forward(self,x):
        out = self.layer(x)
        out = out.reshape(-1,784)
        return self.out_layer(out)


if __name__ == '__main__':
    net = Classification_Regression()
    x = torch.randn(10,3,300,300)
    y = net(x)
    print(y)
    print(y.shape)

