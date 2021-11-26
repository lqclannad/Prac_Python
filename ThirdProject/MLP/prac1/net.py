# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/22 21:04
# 文件名称: net.py
# 开发工具: Pycharm
import torch
from torch import nn
from torch.nn.functional import one_hot


class net_v1(nn.Module):
    # 初始化神经网络结构组件
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 16),
            nn.ReLU(),
            nn.Linear(16, 10),
            nn.Softmax(dim=1)
        )

    # 网络前向计算
    def forward(self, x):
        return self.fc_layer(x)


class net_v2(nn.Module):
    # 初始化神经网络结构组件
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(784, 256),
            nn.Linear(256, 128),
            nn.Linear(128, 64),
            nn.Linear(64, 32),
            nn.Linear(32, 16),
            nn.Linear(16, 16),
            nn.Linear(16, 10),
            nn.Softmax(dim=1)
        )

    # 网络前向计算
    def forward(self, x):
        return self.fc_layer(x)


class net_v3(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Conv2d(3, 12, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(12, 24, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(24, 48, (3, 3), padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(48, 96, (3,3), padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.out_layer = nn.Sequential(
            nn.Linear(96*1*1,10),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        out = self.fc_layer(x)
        out = out.reshape(-1,96*1*1)
        return self.out_layer(out)


if __name__ == '__main__':
    net = net_v3()
    x = torch.randn(1, 3, 28, 28)
    y = net.forward(x)
    print(y)
    print(y.shape)
    y = torch.argmax(y,dim=1)
    y = one_hot(y,10)
    print(y)
