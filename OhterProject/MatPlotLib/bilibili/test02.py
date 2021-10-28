# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/28 17:03
# 平台: PyCharm
# 文件名: test02.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.arange(5)
y = np.random.randint(-5, 5, 5)

# subplots()可以画多个子图
# 该函数返回两个参数 fig和axes，fig表示图形，axes表示轴
# ncols=n指定生成n个子图
fig, axes = plt.subplots(ncols=3)
# 生成两个条形图
v_bars = axes[0].bar(x, y, color='red')
h_bars = axes[1].barh(x, y, color='blue')
d_bars = axes[2].bar(x, y, color='green')
# 画一条y=0的线
axes[0].axhline(0, color='grey', linewidth=2)
axes[1].axhline(0, color='grey', linewidth=2)
axes[2].axhline(0, color='grey', linewidth=2)
plt.show()
