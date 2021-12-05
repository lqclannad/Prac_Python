# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/04 0:48
# 文件名称: net.py
# 开发工具: Pycharm
import torch
from torch import nn


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Conv2d(3,6,(3,3)),
            nn.ReLU(),
            nn.Conv2d(6,12,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(12,24,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(24,48,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(48,96,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(96,192,(3,3)),
            nn.ReLU()
        )

        self.out_layer = nn.Sequential(
            nn.Linear(192*2*2,5),
            nn.Sigmoid()
        )

    def forward(self,x):
        conv_out = self.fc_layer(x)
        conv_out = conv_out.reshape(-1,192*2*2)
        return self.out_layer(conv_out)


if __name__ == '__main__':
    net = Net()
    x = torch.randn(1,3,300,300)
    y = net(x)
    print(y.shape)
