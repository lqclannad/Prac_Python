# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/12 21:25
# 文件名称: test01.py
# 开发工具: Pycharm
import matplotlib.pyplot as plt
import numpy as np

# ★波形图
''' 正弦余弦函数
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)  # 控制曲线
y2 = np.cos(x)  # 控制曲线
plt.title("sin&cos")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
'''

# 堆叠/并列柱状图
'''
name_list = ["A","B","C","D","E"]
num_list1 = [10, 8, 5, 6, 2.1]
num_list2 = [5, 5, 5, 2, 5]
x = list(range(0, len(name_list)))
width = 0.4
plt.bar(x, num_list1, width=width, color="r", tick_label=name_list)
for i in range(5):
    x[i] = x[i] + width
plt.bar(x, num_list2, width=width, color="g", tick_label=name_list)
# plt.legend()
plt.show()
'''

# 饼状图
'''
label = ["A", "B", "C", "D"]
num = [20, 25, 27, 28]
ex = [0.1, 0, 0.1, 0] #
# plt.axis(aspet=1) ×× TypeError
plt.axis = 1   # 1等分
plt.pie(x=num, autopct='%.2f%%', explode=ex, labels=label, colors="rgby", shadow=True, startangle=30)
plt.show()
'''

# ★★★★★ 实时画图
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
