# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/24 17:46
# 平台: PyCharm
# 文件名: net_cnn.py
from torch import nn
import torch

class net3(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Conv2d(3,12,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(12,24,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(24,48,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(48,96,(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(96,192,(3,3)),
            nn.ReLU(),
            nn.Conv2d(192,384,(3,3),padding=1),
            nn.ReLU(),
            nn.Conv2d(384,384,(3,3),padding=1),
            nn.ReLU(),
            nn.Conv2d(384,384,(3,3),padding=1),
            nn.ReLU()
        )

        self.out_layer = nn.Sequential(
            nn.Linear(384*2*2,1),
            nn.Sigmoid()
        )

    def forward(self,x):
        out = self.fc_layer(x)
        out = out.reshape(-1,384*2*2)
        return self.out_layer(out)


if __name__ == '__main__':
    net = net3()
    # 传入卷积的小批量图像的形状应为(n,c,h,w)
    x = torch.randn(1,3,100,100)
    y = net(x)
    print(y.shape)