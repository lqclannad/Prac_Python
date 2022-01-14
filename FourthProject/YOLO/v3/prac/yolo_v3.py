# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/07 17:49
# 文件名称: yolo_v3.py
# 开发工具: Pycharm
import os
import time

import thop
import torch
from torch import nn
from torch.nn import functional
from torchvision import models


class ConvolutionalLayer(nn.Module):
    def __init__(self, in_channels, out_channels, kernerl, stride, padding, bias=False, groups=1):
        super(ConvolutionalLayer, self).__init__()
        self.sub_mode = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernerl, stride, padding, bias=bias, groups=groups),
            nn.BatchNorm2d(out_channels),
            nn.LeakyReLU(0.1)
        )

    def forward(self, x):
        return self.sub_mode(x)


class Upsampling(nn.Module):
    def __init__(self):
        super(Upsampling, self).__init__()
    def forward(self,x):
        return functional.interpolate(x,scale_factor=2,mode="nearest")


class Downsampling(nn.Module):
    def __init__(self, in_channels,out_channels):
        super(Downsampling, self).__init__()
        self.sub_mode = nn.Sequential(
            ConvolutionalLayer(in_channels, out_channels, 3, 2, 1)
        )

    def forward(self, x):
        return self.sub_mode(x)


class ResidualLayer(nn.Module):
    def __init__(self, in_channels):
        super(ResidualLayer, self).__init__()
        self.sub_mode = nn.Sequential(
            # ConvolutionalLayer(in_channels, in_channels//2, 1, 1, 0),
            # ConvolutionalLayer(in_channels//2, in_channels, 3, 1, 1)

            # ConvolutionalLayer(in_channels, in_channels // 2, 1, 1, 0),
            # ConvolutionalLayer(in_channels // 2, in_channels // 2, 3, 1, 1),
            # ConvolutionalLayer(in_channels // 2, in_channels, 1, 1, 0)

            ConvolutionalLayer(in_channels, in_channels*2, 1, 1, 0),
            ConvolutionalLayer(in_channels*2, in_channels*2, 3, 1, 1, groups=in_channels*2),
            ConvolutionalLayer(in_channels*2, in_channels, 1, 1, 0)
        )

    def forward(self, x):
        return self.sub_mode(x)


class Convtionalset(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Convtionalset, self).__init__()
        self.sub_mode = nn.Sequential(
            ConvolutionalLayer(in_channels, out_channels, 1, 1, 0),
            ConvolutionalLayer(out_channels, in_channels, 3, 1, 1),

            ConvolutionalLayer(in_channels, out_channels, 1, 1, 0),
            ConvolutionalLayer(out_channels, in_channels, 3, 1, 1),

            ConvolutionalLayer(in_channels, out_channels, 1, 1, 0)
        )

    def forward(self, x):
        return self.sub_mode(x)

class MainNet(nn.Module):
    def __init__(self):
        super(MainNet, self).__init__()
        self.trunk_52 = nn.Sequential(
            ConvolutionalLayer(3, 32, 3, 1, 1),
            ConvolutionalLayer(32, 64, 3, 2, 1),

            ResidualLayer(64),

            Downsampling(64,128),

            ResidualLayer(128),
            ResidualLayer(128),

            Downsampling(128, 256),

            ResidualLayer(256),
            ResidualLayer(256),
            ResidualLayer(256),
            # ResidualLayer(256),
            # ResidualLayer(256),
            # ResidualLayer(256),
            # ResidualLayer(256),
            ResidualLayer(256)
        )

        self.trunk_26 = nn.Sequential(
            Downsampling(256,512),

            ResidualLayer(512),
            ResidualLayer(512),
            ResidualLayer(512),
            # ResidualLayer(512),
            # ResidualLayer(512),
            # ResidualLayer(512),
            # ResidualLayer(512),
            ResidualLayer(512)
        )

        self.trunk_13 = nn.Sequential(
            Downsampling(512,1024),

            ResidualLayer(1024),
            ResidualLayer(1024),
            ResidualLayer(1024),
            ResidualLayer(1024)
        )

        self.convset_13 = nn.Sequential(
            Convtionalset(1024,512)
        )

        self.out_13 = nn.Sequential(
            ConvolutionalLayer(512,1024,3,1,1),
            nn.Conv2d(1024,15,1,1,0)
        )

        self.convset_up_26 = nn.Sequential(
            ConvolutionalLayer(512,256,1,1,0),
            Upsampling()
        )

        self.convset_26 = nn.Sequential(
            Convtionalset(768,256)
        )

        self.out_26 = nn.Sequential(
            ConvolutionalLayer(256,512,3,1,1),
            nn.Conv2d(512,15,1,1,0)
        )

        self.convset_up_52 = nn.Sequential(
            ConvolutionalLayer(256,128,1,1,0),
            Upsampling()
        )

        self.convset_52 = nn.Sequential(
            Convtionalset(384,128)
        )

        self.out_52 = nn.Sequential(
            ConvolutionalLayer(128,256,3,1,1),
            nn.Conv2d(256,15,1,1,0)
        )

    def forward(self,x):
        h_52 = self.trunk_52(x)
        h_26 = self.trunk_26(h_52)
        h_13 = self.trunk_13(h_26)

        convset_13 = self.convset_13(h_13)
        out_13 = self.out_13(convset_13)

        up_26 = self.convset_up_26(convset_13)
        convset_cat_26 = torch.cat((up_26,h_26),dim=1)

        convset_26 = self.convset_26(convset_cat_26)
        out_26 = self.out_26(convset_26)

        up_52 = self.convset_up_52(convset_26)
        convset_cat_52 = torch.cat((up_52, h_52), dim=1)
        convset_52 = self.convset_52(convset_cat_52)
        out_52 = self.out_52(convset_52)
        return out_13, out_26, out_52


if __name__ == '__main__':

    start = time.time()
    net = MainNet().cpu()
    data = torch.randn(20,3,416,416).cpu()
    # 3layer = (30869912307.0, 56569677.0)
    # 3layer = (  314130496.0,  3504872.0)
    # 2layer = (34531431155.0, 63158285.0)
    # 2layer = (25062152947.0, 51240781.0)
    a = thop.profile(net,(data,))
    print(a)
    exit()

    for i in range(10):
        x = torch.randn(100, 3, 416, 416)
        x = x.cpu()
        y1, y2, y3 = net(x)
    end = time.time()
    if os.path.exists("../log") is False:
        os.mkdir("../log")
    with open("../log/yolov3.txt", "a") as f:
        f.write(f"3-layer cpu epoch_100 100pic {end-start}s\n")
    print(f"耗时{end-start}s")



