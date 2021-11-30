# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/10 9:26
# 文件名称: test03.py
# 开发工具: Pycharm
from cv2 import cv2

img = cv2.imread("../img/5.jpg")

dst1 = cv2.GaussianBlur(img,(7,7),6)
# 中值滤波(特殊低通) - 专门去椒盐噪音
dst2 = cv2.medianBlur(img,3)

cv2.imshow("img",img)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
