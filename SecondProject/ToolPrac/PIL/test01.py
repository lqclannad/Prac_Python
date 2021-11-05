# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/04 9:56
# 平台: PyCharm
# 文件名: test01.py
import numpy as np
from PIL import Image

img_data = np.array([[[255,0,255]]], dtype=np.uint8)
print(img_data.shape)
img = Image.fromarray(img_data)
img.show()
