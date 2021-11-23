# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/10 9:31
# 文件名称: test05.py
# 开发工具: Pycharm
import cv2
import numpy as np

img = cv2.imread("../img/1.jpg")

'''
laplacian核 也叫 laplacian锐化
laplacian锐化(特殊的高通滤波)
高通滤波的结果和原图相加得来，加深轮廓
'''
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)

dst = cv2.filter2D(img,-1,kernel)

cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()