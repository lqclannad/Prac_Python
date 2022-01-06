# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/15 20:46
# 文件名称: nets.py
# 开发工具: Pycharm
# P网络
import torch
from torch import nn

# P网络
class PNet(nn.Module):
    def __init__(self):
        super(PNet, self).__init__()
        self.pre_layer = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=10, kernel_size=3, stride=1, padding=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3,stride=2),
            nn.Conv2d(10,16,kernel_size=3,stride=1),
            nn.PReLU(),
            nn.Conv2d(16,32,kernel_size=3,stride=1),
            nn.PReLU()
        )
        self.conv4_1 = nn.Conv2d(32,1,kernel_size=1,stride=1)
        self.conv4_2 = nn.Conv2d(32,4,kernel_size=1,stride=1)

    def forward(self, x):
        x = self.pre_layer(x)
        cond = torch.sigmoid(self.conv4_1(x))   # 置信度要用sigmoid激活（用BCELoss时要先用sigmoid激活）
        offset = self.conv4_2(x)    # 偏移量不需要激活，原样输出
        return cond, offset

# R网络
class RNet(nn.Module):
    def __init__(self):
        super(RNet, self).__init__()
        self.pre_layer = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=28, kernel_size=3, stride=1, padding=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(28, 48, kernel_size=3, stride=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(48, 64, kernel_size=2, stride=1),
            nn.PReLU()
        )
        self.conv4 = nn.Linear(64*3*3, 128)
        self.prelu4 = nn.PReLU()
        # detection
        self.conv5_1 = nn.Linear(128, 1)
        # bounding box regression
        self.conv5_2 = nn.Linear(128, 4)

    def forward(self, x):
        # backward
        x = self.pre_layer(x)
        x = x.reshape(x.size(0), -1)
        x = self.conv4(x)
        x = self.prelu4(x)
        # detection
        label = torch.sigmoid(self.conv5_1(x))      # 置信度
        offset = self.conv5_2(x)     # 偏移量
        return label, offset

# ONet
class ONet(nn.Module):
    def __init__(self):
        super(ONet, self).__init__()
        # backend
        self.pre_layer = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(32, 64, kernel_size=3, stride=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 64, kernel_size=3, stride=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 128, kernel_size=3, stride=1),
            nn.PReLU()
        )
        self.conv5 = nn.Linear(128*3*3, 256)
        self.prelu5 = nn.PReLU()
        # detection
        self.conv6_1 = nn.Linear(256, 1)
        # bouding box regression
        self.conv6_2 = nn.Linear(256, 4)

    def forward(self, x):
        # backend
        x = self.pre_layer(x)
        x = x.reshape(x.size(0), -1)
        x = self.conv5(x)
        x = self.prelu5(x)
        # detection
        label = torch.sigmoid(self.conv6_1(x))      # 置信度
        offset = self.conv6_2(x)     # 偏移量
        return label, offset


if __name__ == '__main__':
    p_net = PNet()
    r_net = RNet()
    o_net = ONet()

    x1 = torch.randn(1,3,12,12)
    x2 = torch.randn(1,3,24,24)
    x3 = torch.randn(1,3,48,48)

    y1 = p_net(x1)
    y2 = p_net(x2)
    y3 = p_net(x3)

    print(y1)
    print(y2)
    print(y3)