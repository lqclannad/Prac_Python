# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/22 21:04
# 文件名称: net.py
# 开发工具: Pycharm
import torch
from torch import nn


class net_v(nn.Module):
    # 初始化神经网络结构组件
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(100 * 100, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 24),
            nn.ReLU(),
            nn.Linear(24, 16),
            nn.ReLU(),
            nn.Linear(16, 2),
            nn.Softmax(dim=1)
        )

    # 网络前向计算
    def forward(self,x):
        return self.fc_layer(x)


if __name__ == '__main__':
    net = net_v()
    x = torch.randn(1,100*100)
    y = net.forward(x)
    print(y.shape)
