# R/P/O网络搭建
import torch
import torch.nn as nn


# P网路
from torchvision import models


class PNet(nn.Module):
    def __init__(self):
        super(PNet,self).__init__()

        self.pre_layer = nn.Sequential(
            nn.Conv2d(in_channels=3,out_channels=10,kernel_size=3,stride=1,padding=1), # conv1
            nn.PReLU(),                                                               # prelu1
            nn.MaxPool2d(kernel_size=3,stride=2),    # pool1；conv1里的填充在此处操作，效果更好★
            nn.Conv2d(10,16,kernel_size=3,stride=1), # conv2
            nn.PReLU(),                              # prelu2
            nn.Conv2d(16,32,kernel_size=3,stride=1), # conv3
            nn.PReLU()                               # prelu3
        )
        self.conv4_1 = nn.Conv2d(32,1,kernel_size=1,stride=1)
        self.comv4_2 = nn.Conv2d(32,4,kernel_size=1,stride=1)

    def forward(self, x):
        x = self.pre_layer(x)
        cond = torch.sigmoid(self.conv4_1(x)) # 置信度用sigmoid激活(用BCEloos时先要用sigmoid激活)
        offset = self.comv4_2(x)         # 偏移量不需要激活，原样输出
        return cond,offset


# R网路
class RNet(nn.Module):
    def __init__(self):
        super(RNet,self).__init__()
        self.pre_layer = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=28, kernel_size=3, stride=1,padding=1), # conv1
            nn.PReLU(),                                                                  # prelu1
            nn.MaxPool2d(kernel_size=3, stride=2),                                       # pool1
            nn.Conv2d(28, 48, kernel_size=3, stride=1),  # conv2
            nn.PReLU(),                                  # prelu2
            nn.MaxPool2d(kernel_size=3, stride=2),       # pool2
            nn.Conv2d(48, 64, kernel_size=2, stride=1),          # conv3
            nn.PReLU()                                           # prelu3
        )
        self.conv4 = nn.Linear(64*3*3,128) # conv4
        self.prelu4 = nn.PReLU()           # prelu4
        #detetion
        self.conv5_1 = nn.Linear(128,1)
        #bounding box regression
        self.conv5_2 = nn.Linear(128, 4)

    def forward(self, x):
        #backend
        x = self.pre_layer(x)
        x = x.reshape(x.size(0),-1)
        x = self.conv4(x)
        x = self.prelu4(x)
        #detection
        label = torch.sigmoid(self.conv5_1(x)) # 置信度
        offset = self.conv5_2(x) # 偏移量
        return label,offset


# O网路
class ONet(nn.Module):
    def __init__(self):
        super(ONet,self).__init__()
        # backend
        self.pre_layer = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1,padding=1),  # conv1
            nn.PReLU(),                                          # prelu1
            nn.MaxPool2d(kernel_size=3, stride=2),              # pool1
            nn.Conv2d(32, 64, kernel_size=3, stride=1),  # conv2
            nn.PReLU(),                                 # prelu2
            nn.MaxPool2d(kernel_size=3, stride=2),     # pool2
            nn.Conv2d(64, 64, kernel_size=3, stride=1),        # conv3
            nn.PReLU(),                                       # prelu3
            nn.MaxPool2d(kernel_size=2, stride=2),           # pool3
            nn.Conv2d(64, 128, kernel_size=2, stride=1),  # conv4
            nn.PReLU()                                   # prelu4
        )
        self.conv5 = nn.Linear(128 * 3 * 3, 256)  # conv5
        self.prelu5 = nn.PReLU()                 # prelu5
        # detection
        self.conv6_1 = nn.Linear(256, 1)
        # bounding box regression
        self.conv6_2 = nn.Linear(256, 4)

    def forward(self, x):
        # backend
        x = self.pre_layer(x)
        x = x.reshape(x.size(0), -1)
        x = self.conv5(x)
        x = self.prelu5(x)
        # detection
        label = torch.sigmoid(self.conv6_1(x)) # 置信度
        offset = self.conv6_2(x)          # 偏移量
        return label, offset


class Arcsoftmax(nn.Module):
    def __init__(self, feature_num, cls_num):
        super().__init__()
        self.w = nn.Parameter(torch.randn((feature_num, cls_num)))
        self.func = nn.Softmax()

    def forward(self, x, s=1, m=0.2):
        x_norm = F.normalize(x, dim=1)
        w_norm = F.normalize(self.w, dim=0)

        cosa = torch.matmul(x_norm, w_norm) / 10
        a = torch.acos(cosa)

        arcsoftmax = torch.exp(
            s * torch.cos(a + m) * 10) / (torch.sum(torch.exp(s * cosa * 10), dim=1, keepdim=True) - torch.exp(
            s * cosa * 10) + torch.exp(s * torch.cos(a + m) * 10))

        return arcsoftmax


class FaceNet(nn.Module):

    def __init__(self):
        super(FaceNet, self).__init__()
        self.sub_net = nn.Sequential(
            models.densenet121(pretrained=True),
        )
        self.feature_net = nn.Sequential(
            nn.LeakyReLU(0.1),
            nn.Linear(1000, 512, bias=False),
        )
        self.arc_softmax = Arcsoftmax(512, 12)

    def forward(self, x):
        y = self.sub_net(x)
        feature = self.feature_net(y)
        return feature, self.arc_softmax(feature, 1, 1)

    def encode(self, x):
        return self.feature_net(self.sub_net(x))


if __name__ == '__main__':
    p_net = PNet()
    r_net = RNet()
    o_net = ONet()

    x1 = torch.randn(1,3,12,12)
    x2 = torch.randn(1,3,24,24)
    x3 = torch.randn(1,3,48,48)

    y1 = p_net(x1)
    y2 = r_net(x2)
    y3 = o_net(x3)

    print(y1)
    print(y2)
    print(y3)