# ★★★★★ 实时画图
from matplotlib import pyplot as plt

ax = []
ay = []
plt.ion()   # 打开实时画图工具
for i in range(100):
    ax.append(i)
    ay.append(i**2)
    plt.clf()   # 需进行实时清除，否则长时间循环运行会造成内存泄露，从而导致程序崩溃
    plt.plot(ax, ay)
    plt.pause(0.1)
plt.ioff()  # 关闭实时画图工具
