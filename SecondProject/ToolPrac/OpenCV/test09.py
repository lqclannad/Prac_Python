# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/08 13:07
# 平台: PyCharm
# 文件名: test09.py
import numpy as np
from cv2 import cv2

x = np.uint8([250])
y = np.uint8([10])
# 像素点的加减
print(cv2.add(x,y))         # [[255]]
print(cv2.subtract(y,x))    # [[0]]
