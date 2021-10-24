# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/24 15:35
# 文件名称: and3.py
# 开发工具: Pycharm
import matplotlib.pyplot as plt
import numpy as np

# 1：定义w、b
w = np.random.rand(1)
b = np.random.rand(1)
_x = [i/100 for i in range(100)]
_y = [3*x+6 for x in _x]

plt.ion()
for _ in range(30):
    for x, y in zip(_x, _y):
        z = w * x + b
        # 2、求损失值
        o = z - y
        loss = o ** 2
        # 求导
        dw = 2 * o * w
        db = 2 * o
        # 3、确定步长、方向，通过当前位置算得下一步的位置
        w = w - 0.3 * dw
        b = b - 0.3 * db
        print(f'{w},{b}')
        v = [w*xx+b for xx in _x]
        plt.cla()
        plt.plot(_x, _y)
        plt.plot(_x, v)
        plt.pause(0.01)
plt.ioff()
plt.show()
