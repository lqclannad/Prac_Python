# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/06 19:40
# 文件名称: net2.py
# 开发工具: Pycharm
import torch
from torch import nn


class Net_v2(nn.Module):
    def __init__(self):
        super(Net_v2, self).__init__()
        self.fc_layer = nn.Sequential(
            nn.Conv2d(3,32,3),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(32,64,3),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(64,128,3),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(128,256,3),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(256,256,3,padding=1),
            nn.ReLU(),
            nn.Conv2d(256,256,3,padding=1),
            nn.ReLU(),
            nn.Conv2d(256,256,3,padding=1),
            nn.ReLU()
        )
        self.out_layer = nn.Sequential(
            nn.Linear(256*2*2,1),
            nn.Sigmoid()
        )

    def forward(self,x):
        # return self.fc_layer(x)
        conv_out = self.fc_layer(x)
        conv_out = conv_out.reshape(-1,256*2*2)
        return self.out_layer(conv_out)


if __name__ == '__main__':
    net = Net_v2()
    x = torch.randn(1,3,300,300)
    y = net(x)
    print(y.shape)
