# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/24 13:02
# 平台: PyCharm
# 文件名: net2.py
from torch import nn
import torch

class net2(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(3*100*100,784),
            nn.ReLU(),
            nn.Linear(784,512),
            nn.ReLU(),
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,1),
            nn.Sigmoid()
        )

    def forward(self,x):
        return self.fc_layer(x)


if __name__ == '__main__':
    net = net2()
    x = torch.randn(1,3*100*100)
    y = net(x)
    print(y.shape)
