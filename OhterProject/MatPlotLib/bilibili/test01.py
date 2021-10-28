# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/28 16:37
# 平台: PyCharm
# 文件名: test01.py
import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('ggplot')
# plt.style.use(['ggplot', 'bmh'])
plt.xkcd()
plt.plot([1,2,3,4,5],[1,4,9,16,25],'-',color='r')
plt.xlabel("time")
plt.ylabel("price")
plt.title("time-price")
plt.show()
'''
# 打印能使用的风格
print(plt.style.available)# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
# 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
# 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel',
# 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
'''
