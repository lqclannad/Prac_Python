# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/15 10:39
# 文件名称: test09.py
# 开发工具: Pycharm
import cv2
import torch

img = cv2.imread("../img/92307362_p0_master1200.jpg",0)

# 画边缘
dst = cv2.Canny(img, 30, 150)
dst2 = cv2.Laplacian(img, -1)

cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.imshow("dst2",dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
