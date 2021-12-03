# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/30 12:44
# 平台: PyCharm
# 文件名: net.py
import torch
from torch import nn


class Classification(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3,48,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(48,96,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(96,192,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(192,384,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(384,512,(3,3),padding=1),
            nn.ReLU(),
        )

        self.out_layer1 = nn.Sequential(
            nn.Linear(512*2*2,5),
            nn.Sigmoid()
        )

    def forward(self,x):
        out = self.layer1(x)
        out = out.reshape(-1,512*2*2)
        return self.out_layer1(out)


if __name__ == '__main__':
    net1 = Classification()
    x = torch.randn(10,3,300,300)
    y = net1(x)
    print(y)
    print(y.shape)


