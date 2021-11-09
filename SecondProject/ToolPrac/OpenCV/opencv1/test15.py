# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/08 21:04
# 文件名称: test15.py
# 开发工具: Pycharm
from cv2 import cv2

img = cv2.imread("../img/LQCLANNAD.png")

# 定义滤波器(卷积核)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# 膨胀
dst1 = cv2.dilate(img, kernel)
# 腐蚀
dst2 = cv2.erode(img, kernel)

cv2.imshow("img",img)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
