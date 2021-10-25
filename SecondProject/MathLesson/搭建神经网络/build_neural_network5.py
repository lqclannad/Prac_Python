# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/25 23:02
# 文件名称: build_neural_network5.py
# 开发工具: Pycharm
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
import matplotlib.pyplot as plt
from torch import nn
import random

# /20 是做归一化处理
xs = torch.unsqueeze(torch.arange(-20., 20.), dim=1) / 20
# [tensor([x.]),...] 列表内含多个张量元素
ys = [e.pow(3) * random.randint(1, 6) for e in xs]
# 将列表中的张量元素通过stack函数组合成一个新的张量
# tensor([[x.],...])
ys = torch.stack(ys)


class Line(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(1, 20),
            nn.ReLU(),
            nn.Linear(20, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    # 前向计算
    def forward(self, x):
        return self.fc_layer(x)


if __name__ == '__main__':
    net = Line()
    # 定义损失函数(均方差)
    loss_func = nn.MSELoss()
    # 梯度下降优化器
    # opt = torch.optim.SGD(net.parameters(), lr=0.003)
    opt = torch.optim.Adam(net.parameters())
    plt.ion()
    for epoch in range(30000):
        out = net.forward(xs)
        loss = loss_func(out, ys)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if epoch%5==0:
            print(loss.item())
            plt.cla()
            plt.plot(xs, ys, ".")
            plt.plot(xs, out.detach())
            plt.pause(0.001)
    plt.ioff()
    # plt.show()
