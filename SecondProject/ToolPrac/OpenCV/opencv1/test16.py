# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/08 21:12
# 文件名称: test16.py
# 开发工具: Pycharm
from cv2 import cv2

img = cv2.imread("../img/LQCLANNAD.png")

# 定义卷积核(滤波器)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
'''开操作 等价于 先腐蚀再膨胀 👉 去噪'''
# dst1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)     # 开操作
# dst = cv2.erode(img, kernel)
# dst = cv2.dilate(dst, kernel)
'''闭操作 等价于 先膨胀再腐蚀 👉 补漏洞'''
# dst1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)       # 闭操作
# dst = cv2.dilate(img, kernel)
# dst = cv2.erode(dst, kernel)
'''梯度操作 等价于 膨胀-腐蚀 👉 获取轮廓'''
# dst1 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# dst21 = cv2.dilate(img, kernel)
# dst22 = cv2.erode(img, kernel)
# dst = cv2.subtract(dst21, dst22)
'''顶帽操作 等价于 原图-开操作 👉 获取噪音'''
# dst1 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# dst21 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# dst = cv2.subtract(img, dst21)
'''黑帽操作 等价于 闭操作-原图 👉 获取漏洞-'''
dst1 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
dst21 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
dst = cv2.subtract(dst21, img)


cv2.imshow("img", img)
cv2.imshow("dst", dst)
cv2.imshow("dst1", dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()
