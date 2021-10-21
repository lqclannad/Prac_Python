# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/21 15:21
# 平台: PyCharm
# 文件名: figure_test.py
import numpy as np
import pandas
from matplotlib import pyplot as plt

# 参照：https://www.matplotlib.org.cn/tutorials/introductory/usage.html#legends

# fig = plt.figure()
# fig.suptitle('lqclannad')   # give a title
# fig, ax_lst = plt.subplots(2, 2)    # a figure with a 2x2 gird of Axes
# plt.show()

# a = pandas.DataFrame(np.random.rand(4, 5), columns=list('abcde'))
# a_asarray = a.values    # 将 DataFrame -> ndarray
# b = np.matrix([[1, 2], [3, 4]])  # 将 matrix -> ndarray
# b_asarray = np.asarray(b)
# print(type(a), type(a_asarray))
# print(type(b), type(b_asarray))

# x = np.linspace(-2, 2, 100)
# plt.plot(x, x, label='linear')  # y = x
# plt.plot(x, x**2, label='quadratic')    # y = x**2
# plt.plot(x, x**3, label='cubic')    # y = x**3
# plt.xlabel('x label')   # x轴说明
# plt.ylabel('y label')   # y轴说明
# plt.title('Simple Plot')    # 标题
# plt.legend()    # 说明
# plt.show()

x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
