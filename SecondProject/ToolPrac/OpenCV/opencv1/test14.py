# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/08 20:56
# 文件名称: test14.py
# 开发工具: Pycharm
import numpy as np

from cv2 import cv2

img = cv2.imread("../img/2.jpg")

pts1 = np.float32([[25,30], [179,25], [12, 188], [189,190]])
pts2 = np.float32([[0,0], [200,0], [0, 200], [200,200]])

M = cv2.getPerspectiveTransform(pts1, pts2)
# 透视变换
dst = cv2.warpPerspective(img, M, (200,200))

cv2.imshow("img",img)
cv2.imshow("dat",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
