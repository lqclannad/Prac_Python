# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/21 15:48
# 平台: PyCharm
# 文件名: SamplePlots_test.py
import numpy as np
from matplotlib import pyplot as plt

# 参照：https://www.matplotlib.org.cn/tutorials/introductory/sample_plots.html#line-plot

# Line Plot - plot()
# x = [1, 2, 3]
# y = np.array([[1, 2], [3, 4], [5, 6]])
# plt.plot(x, y)
# plt.show()

# Multiple subplots - subplot()
# plt.plot([1, 2, 3])
# # 现在创建一个子图，表示具有 2 行和 1 列的网格的顶部图。
# # 由于此子图将与第一个重叠，因此先前创建的图（及其轴）将被删除
# plt.subplot(211)
#
# ax1 = plt.subplot(2, 2, 1)
# ax2 = plt.subplot(222, frameon=False)   # 添加一个没有框架的子图
# plt.subplot(223, projection='polar')    # polar 极线
# plt.subplot(224, sharex=ax1, facecolor='red')
# # plt.delaxes(ax2)    # 将ax2子图删除
# plt.subplot(ax2)    # 将ax2子图添加进来展示
# plt.show()

# Images - imshow()
plt.imshow()

