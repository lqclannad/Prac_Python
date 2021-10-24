# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 14:49
# 文件名称: build_neural_network4.py
# 开发工具: Pycharm
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
import matplotlib.pyplot as plt
from torch import nn

xs = torch.unsqueeze(torch.arange(0.01, 1, 0.01), dim=1)
ys = 3 * xs + 4


class Line(nn.Module):
    # 设计神经网络
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(1, 20),
            nn.Linear(20, 64),
            nn.Linear(64, 128),
            nn.Linear(128, 64),
            nn.Linear(64, 1),
        )

    # 前向计算
    def forward(self, x):
        return self.fc_layer(x)


if __name__ == '__main__':
    net = Line()
    # 定义损失函数(均方差)
    loss_func = nn.MSELoss()
    # 梯度下降优化器
    # 优化器Adam较SGD更好
    # opt = torch.optim.SGD(net.parameters(), lr=0.001)
    opt = torch.optim.Adam(net.parameters())

    plt.ion()
    for epoch in range(3000):
        out = net.forward(xs)

        loss = loss_func(out, ys)

        opt.zero_grad()
        loss.backward()
        opt.step()

        if epoch % 5 == 0:
            print(loss.item())
            plt.cla()
            plt.title("loss%.4f" % loss.item())
            plt.plot(xs, ys, ".")
            plt.plot(xs, out.detach())
            plt.pause(0.001)
    plt.ioff()
    plt.show()
