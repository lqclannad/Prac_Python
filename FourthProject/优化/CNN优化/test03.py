# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/06 10:31
# 文件名称: test03.py
# 开发工具: Pycharm
import torch
from torch import nn

config = [
    [-1,32,1,2],
    [1,16,1,1],
    [6,24,2,2],
    [6,32,3,2],
    [6,64,4,2],
    [6,96,3,1],
    [6,160,3,2],
    [6,320,1,1]
]

class Block(nn.Module):
    """
        p_c:: 输入通道
        i:: 当前次序
        t:: 通道膨胀倍数
        c:: 输出通道
        n:: 重复次数
        s:: 步长
    """
    def __init__(self,p_c,i,t,c,n,s):
        super(Block, self).__init__()
        self.i = i
        self.n = n

        _s = s if i==n-1 else 1
        _c = c if i==n-1 else p_c

        _p_c = p_c * t

        self.layer = nn.Sequential(
            nn.Conv2d(p_c,_p_c,1,1,bias=False),
            nn.BatchNorm2d(_p_c),
            nn.ReLU6(),
            nn.Conv2d(_p_c,_p_c,3,_s,padding=1,groups=_p_c,bias=False),
            nn.BatchNorm2d(_p_c),
            nn.ReLU6(),
            nn.Conv2d(_p_c,_c,1,1,bias=False),
            nn.BatchNorm2d(_c)
        )
    def forward(self,x):
        # 判断当前重复的次序是否是最后一次
        # 如果是最后一次，就加残差
        if self.i == self.n-1:
            return self.layer(x)
        else:
            return self.layer(x) + x

class MobileNetV2(nn.Module):
    def __init__(self,config):
        super(MobileNetV2, self).__init__()
        self.input_layer = nn.Sequential(
            nn.Conv2d(3,32,3,2,1,bias=False),
            nn.BatchNorm2d(32),
            nn.ReLU6()
        )
        # 开辟一片空间，存放神经网络层
        self.blocks = []
        p_c = config[0][1]
        for t,c,n,s in config[1:]:
            for i in range(n):
                self.blocks.append(Block(p_c,i,t,c,n,s))
            p_c = c
        self.hidden_layer = nn.Sequential(*self.blocks)
        self.output_layer = nn.Sequential(
            nn.Conv2d(320,1280,1,1,bias=False),
            nn.BatchNorm2d(1280),
            nn.ReLU6(),
            nn.AvgPool2d(7,1),
            nn.Conv2d(1280,10,1,1)
        )
    def forward(self,x):
        h = self.input_layer(x)
        h = self.hidden_layer(h)
        h = self.output_layer(h)
        return h


if __name__ == '__main__':
    net = MobileNetV2(config)
    y = net(torch.randn(1,3,224,224))
    print(y.shape)
    print(net)