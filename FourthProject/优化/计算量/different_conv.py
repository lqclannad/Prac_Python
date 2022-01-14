# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/11 16:28
# 文件名称: different_conv.py
# 开发工具: Pycharm
import time

import thop
import torch
from torch import nn


class net1(nn.Module):
    def __init__(self):
        super(net1, self).__init__()
        self.fc_layer = nn.Sequential(
            nn.Conv2d(6,6,3,1,1,groups=1)
        )
    def forward(self,x):
        return self.fc_layer(x)

class net2(nn.Module):
    def __init__(self):
        super(net2, self).__init__()
        self.fc_layer = nn.Sequential(
            nn.Conv2d(6,18,1,1,0,groups=3),
            nn.Conv2d(18,18,3,1,1,groups=18),
            nn.Conv2d(18,6,1,1,0,groups=3)
        )
    def forward(self,x):
        return self.fc_layer(x)


if __name__ == '__main__':
    n1 = net1()
    n2 = net2()
    data = torch.randn(1,6,32,32)
    t1 = thop.profile(n1,(data,))
    t2 = thop.profile(n2,(data,))
    print(t1)   # 96-30412800-0.0019953250885009766   416-571084800  -0.0359044075012207    640-1351680000.0-0.07779145240783691    960-3041280000-0.1356356143951416
    print(t2)   # 96-25436160-0.009973526000976562    416-477634560.0-0.1934823989868164    640-1130496000.0-0.44281554222106934    960-2543616000-1.0960681438446045

    s1 = time.time()
    y1 = n1(data)
    e1 = time.time()

    s2 = time.time()
    y2 = n2(data)
    e2 = time.time()

    print(e1-s1)
    print(e2-s2)
    print(y1.shape)
    print(y2.shape)
