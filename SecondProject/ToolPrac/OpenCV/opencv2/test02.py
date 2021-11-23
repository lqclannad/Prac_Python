# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/10 9:23
# 文件名称: test02.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/LQCLANNAD.png")

# 均值滤波
dst1 = cv2.blur(img,(5,5))
# 高斯滤波
dst2 = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("img",img)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
