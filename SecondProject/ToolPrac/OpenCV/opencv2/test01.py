# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/08 22:24
# 文件名称: test01.py
# 开发工具: Pycharm
import cv2
import numpy as np

img = cv2.imread("../img/LQCLANNAD.png")
kernel = np.array([[1,1,0],[1,0,-1],[0,-1,-1]],np.float32)
# 二维的滤波器 高通滤波
dst = cv2.filter2D(img, -1, kernel)

cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
