# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/04 15:34
# 平台: PyCharm
# 文件名: test06.py
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# # 创建测试数据
# x = np.random.randn(20)
# y = np.random.randn(20)
#
# # 绘制点
# plt.scatter(x, y, s=200, marker="*")
# plt.show()
# # 绘制折线图
# plt.plot(x,y)
# plt.show()

# img = Image.open("img/92307362_p0_master1200.jpg")
# plt.imshow(img)
# plt.axis(False)
# plt.show()

# # 实时绘图
# ax = []
# ay = []
# # 开启绘画
# plt.ion()
# for i in range(100):
#     ax.append(i)
#     ay.append(i**2)
#     plt.clf()
#     plt.plot(ax,ay)
#     plt.pause(0.01)
# # 结束绘画
# plt.ioff()
# plt.show()

# 3D画板
x = np.random.normal(0,1,1000)
y = np.random.normal(0,1,1000)
z = np.random.normal(0,1,1000)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z)
plt.show()
