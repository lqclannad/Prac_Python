# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/15 9:58
# 文件名称: test08.py
# 开发工具: Pycharm
from cv2 import cv2
import numpy as np

img = cv2.imread("../img/2.jpg")
# 画梯度
dst1 = cv2.Laplacian(img, -1)
# 拉普拉斯卷积核
kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]],dtype=np.float32)
dst2 = cv2.filter2D(img, -1, kernel)

cv2.imshow("img", img)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
