# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/31 0:55
# 文件名称: test1.py
# 开发工具: Pycharm
import os

import cv2
import torchvision.models as models
from torch import nn
import torch
from torch.nn import functional as F
from torch import optim
from torch.utils.data import DataLoader
import torch.jit as jit
from PIL import Image
from torchvision import transforms

tf = transforms.Compose([
    transforms.Resize(112),
    transforms.ToTensor(),
])

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


def compare(face1, face2):
    face1_norm = F.normalize(face1)
    face2_norm = F.normalize(face2)
    print(face1_norm.shape)
    print(face2_norm.shape)
    cosa = torch.matmul(face1_norm, face2_norm.t())
    return cosa


if __name__ == '__main__':
    net = FaceNet().cuda()
    a = torch.load("register/刘泉.pt")
    a = torch.stack(a)
    img = (tf(Image.open("img/img_3.png").convert("RGB"))).cuda()
    feat = net.encode(img[None, ...])
    a = F.normalize(a)
    feat = F.normalize(feat).t()
    m = torch.matmul(a, feat)
    print(m)
