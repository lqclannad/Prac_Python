# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/05 17:25
# 平台: PyCharm
# 文件名: test03.py
import cv2.cv2
import numpy as np

img = np.zeros((200,300,3),dtype=np.uint8)
img[...,[0,1,2]] = [0,0,255]    # BGR
cv2.cv2.imshow("img",img)
cv2.cv2.waitKey(0)
cv2.cv2.destroyAllWindows()
