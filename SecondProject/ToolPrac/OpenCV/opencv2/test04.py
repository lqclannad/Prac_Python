# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/10 9:29
# 文件名称: test04.py
# 开发工具: Pycharm
from cv2 import cv2

img = cv2.imread("../img/24.jpg")

'''
双边滤波(非线性) - 衔接断开的线
作用：降噪、保持边缘
d - 断线之间最大距离
sigmaColor - 控制色彩灰度
sigmaSpace - 控制颜色梯度
'''
dst = cv2.bilateralFilter(img,9,75,75)

cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
