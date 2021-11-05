# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/04 16:12
# 平台: PyCharm
# 文件名: test08.py
import os

import matplotlib.pyplot as plt
from PIL import Image

plt.ion()
while True:
    for i in os.listdir("img"):
        img = Image.open(os.path.join("img/", i))
        plt.clf()
        plt.axis(False)
        plt.imshow(img)
        plt.pause(1)
plt.ioff()
plt.show()
