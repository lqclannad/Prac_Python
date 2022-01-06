# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/28 12:31
# 文件名称: 5层卷积.py
# 开发工具: Pycharm
import time

import torch
from torch import nn
import thop


class _5_layer_conv(nn.Module):
    def __init__(self):
        super(_5_layer_conv, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv2d(1,16,3),
            nn.ReLU(),
            nn.Conv2d(16,32,3),
            nn.ReLU(),
            nn.Conv2d(32,64,3),
            nn.ReLU(),
            nn.Conv2d(64,128,3),
            nn.ReLU(),
            nn.Conv2d(128,256,3),
        )

    def forward(self,x):
        return self.layer(x)

class _5_layer_linear(nn.Module):
    def __init__(self):
        super(_5_layer_linear, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
        )

    def forward(self,x):
        return self.layer(x)


if __name__ == '__main__':
    start = time.time()

    conv = _5_layer_conv()
    x1 = torch.randn(1,1,28,28)
    y1 = conv(x1)     # _cpu 0.014915704727172852   _cuda 3.2193074226379395

    # linear = _5_layer_linear().cuda()
    # x2 = torch.randn(1,784).cuda()
    # y2 = linear(x2)     # _cpu 0.004984855651855469   _cuda 3.4207842350006104

    end = time.time()
    print(end-start)

    # print(thop.profile(conv,(x1,)))     # (136909696.0, 392320.0)
    # print(thop.profile(linear,(x2,)))     # (244032.0, 244522.0)
    # print(thop.clever_format(thop.profile(conv,(x1,))))   # ('136.91M', '392.32K')
    # print(thop.clever_format(thop.profile(linear,(x2,))))   # ('244.03K', '244.52K')

