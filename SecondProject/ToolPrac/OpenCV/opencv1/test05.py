# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/08 9:37
# 平台: PyCharm
# 文件名: test05.py
from cv2 import cv2
import numpy as np

img = cv2.imread("../img/92307362_p0_master1200.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_color = np.array([0,100,80])
upper_color = np.array([179,255,200])
mask = cv2.inRange(hsv, lower_color, upper_color)
cv2.imshow("img",img)
cv2.imshow("dst",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()