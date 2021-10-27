# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/27 17:38
# 平台: PyCharm
# 文件名: build_test02.py
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import matplotlib.pyplot as plt
import torch
from torch import nn

# 目标 圆
xs = torch.unsqueeze(torch.arange(-1, 1, 0.01), dim=1)
ys = 1 - xs ** 2


# 解决线性
class Net1(nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.randn(1, 60))
        self.b1 = nn.Parameter(torch.randn(60))
        self.w2 = nn.Parameter(torch.randn(60, 120))
        self.b2 = nn.Parameter(torch.randn(120))
        self.w3 = nn.Parameter(torch.randn(120, 1))
        self.b3 = nn.Parameter(torch.randn(1))

    def forward(self, x):
        fc1 = torch.matmul(x, self.w1) + self.b1
        fc2 = torch.matmul(fc1, self.w2) + self.b2
        fc3 = torch.matmul(fc2, self.w3) + self.b3
        return fc3


# 激活后 可解决非线性
class Net2(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(1, 60),
            nn.Sigmoid(),
            nn.Linear(60, 120),
            nn.Sigmoid(),
            nn.Linear(120, 1)
        )

    def forward(self, x):
        return self.fc_layer(x)


if __name__ == '__main__':
    net = Net2()
    # 定义损失函数(均方差)
    loss_func = nn.MSELoss()
    # 选择优化器
    # opt = torch.optim.SGD(net.parameters(), lr=0.001)
    opt = torch.optim.Adam(net.parameters())

    plt.ion()

    for _ in range(3000):
        out = net.forward(xs)
        loss = loss_func(out, ys)

        # 清空梯度 - 自动求导 - 更新梯度
        opt.zero_grad()
        loss.backward()
        opt.step()

        # 打印损失值
        plt.cla()
        plt.title("loss%.4f" % loss.item())
        plt.plot(xs, ys, ".")
        plt.plot(xs, out.detach())
        plt.pause(0.1)
    plt.ioff()
    plt.show()
