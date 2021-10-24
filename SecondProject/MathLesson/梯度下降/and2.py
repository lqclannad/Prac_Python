# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/20 18:55
# 文件名称: and2.py
# 开发工具: Pycharm
import random
import matplotlib.pyplot as plt

# 确定样本的函数
_x = [i/100 for i in range(100)]
# y = 3x + 4 + (0,1)
_y = [3 * e + 4 + random.random() for e in _x]
# 1：生成w、b
w = random.random()
b = random.random()
plt.ion()
for _ in range(30):
    for x, y in zip(_x, _y):
        # 2： 代入函数式(h=xw+b)求损失值
        z = w * x + b
        o = z - y
        loss = o ** 2
        # 3：将步长λ和求得的导δ代入函数式(w'=w-λδ)进行优化
        w = w - 2 * 0.3 * x * o
        b = b - 2 * 0.3 * o
        print(f'{w}  {b}')
        plt.cla()
        v = [w * x + b for x in _x]
        plt.plot(_x, _y)
        plt.plot(_x, v)
        plt.pause(0.05)
plt.ioff()
plt.show()
