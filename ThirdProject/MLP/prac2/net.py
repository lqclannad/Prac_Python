# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/22 21:54
# 文件名称: net.py
# 开发工具: Pycharm
import torch
from torch import nn


class net_v1(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 10),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        return self.fc_layer(x)


class net_v2(nn.Module):
    def __init__(self):
        super(net_v2, self).__init__()
        self.W = nn.Parameter(torch.randn(784, 10))
        self.B = nn.Parameter(torch.randn(10))

    # 模拟softmax过程
    def forward(self, x):
        h = x @ self.W + self.B
        # softmax
        h = torch.exp(h)
        z = torch.sum(h, dim=1, keepdim=True)
        return h / z


class net_v3(nn.Module):
    def __init__(self):
        super(net_v3, self).__init__()
        self.fc1 = nn.Linear(784,10)

    def forward(self,x):
        return torch.softmax(self.fc1(x),dim=1)


class net_v4(nn.Module):
    # 初始化网络结构组件
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 10),
            nn.Softmax(dim=1)
        )

    # 网络前向计算
    def forward(self,x):
        return self.fc_layer(x)


class net_v5(nn.Module):
    # 初始化网络结构组件
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(784, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            nn.Softmax(dim=1)
        )

    # 网络前向计算
    def forward(self,x):
        return self.fc_layer(x)


if __name__ == '__main__':
    net = net_v5()
    x = torch.randn(1, 784)
    y = net.forward(x)
    print(y.shape)
