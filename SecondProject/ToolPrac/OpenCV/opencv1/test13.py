# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/08 19:49
# 文件名称: test13.py
# 开发工具: Pycharm
import numpy as np

from cv2 import cv2

img = cv2.imread("../img/92307362_p0_master1200.jpg")
h,w,c = img.shape

# 定义变换矩阵,
# M = np.float32([[1,0,50],0,1,50]])
# M = np.float32([[0.4,0,0],[0,0.4,0]])
# M = np.float32([[np.cos(1/6*np.pi),np.sin(1/6*np.pi),0],[-np.sin(1/6*np.pi),np.cos(1/6*np.pi),0]])
# M = np.float32([[1,np.tan(1/18*np.pi),0],[0,1,0]])
# M = np.float32([[1,0,0],[np.tan(1/18*np.pi),1,0]])
# M = np.float32([[-1,0,0],[0,-1,0]])
# M = np.float32([[1,0,0],[0,-1,0]])
M = np.float32([[-1,0,0],[0,1,0]])

# 仿射变换
dst = cv2.warpAffine(img,M,(w,h))

cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
