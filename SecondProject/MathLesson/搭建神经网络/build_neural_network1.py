# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 9:32
# 文件名称: build_neural_network1.py
# 开发工具: Pycharm
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
'''
use os.environ to solve problem：Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.
'''
import torch
import matplotlib.pyplot as plt
from torch import nn

xs = torch.arange(0.01, 1, 0.01)
ys = 3 * xs + 4 + torch.rand(99)


class Line(nn.Module):
    def __init__(self):
        super().__init__()
        self.w = nn.Parameter(torch.rand(1))
        self.b = nn.Parameter(torch.rand(1))

    # 前向计算
    def forward(self, x):
        return x * self.w + self.b


if __name__ == '__main__':
    line = Line()
    # 定义损失函数(均方案)
    loss_func = nn.MSELoss()
    # 梯度下降优化器
    opt = torch.optim.SGD(line.parameters(), lr=0.1)    # lr=0.1 代指步长
    plt.ion()
    for epoch in range(30):
        for _x, _y in zip(xs, ys):
            # 先进行前向计算
            z = line.forward(_x)
            # 将 输出结果z 和 样本y 代入损失函数求得损失值
            loss = loss_func(z, _y)
            # 清空梯度
            opt.zero_grad()
            # 自动求导
            loss.backward()
            # 更新梯度
            opt.step()
            # tensor.item()  将张量转换为标量
            print(line.w.item(), line.b.item())

            plt.cla()
            plt.plot(xs, ys, ".")
            # detach() - 解绑
            v = [line.w.detach() * e + line.b.detach() for e in xs]
            plt.plot(xs, v)
            plt.pause(0.001)
        plt.ioff()
        plt.show()
'''
解决一维线性问题
'''
