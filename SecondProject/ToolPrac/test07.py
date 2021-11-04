# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/04 16:09
# 平台: PyCharm
# 文件名: test07.py
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(20)
y = np.random.randn(20)

plt.scatter(x,y,s=150,label="boy",c="blue",marker="*")
# 添加新数据
x = np.random.randn(10)
y = np.random.randn(10)
plt.scatter(x,y,s=150,label="girl",c="red",marker="o")
# 显示图例
plt.legend()
plt.show()
