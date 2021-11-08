# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/08 12:45
# 平台: PyCharm
# 文件名: test08.py
from cv2 import cv2

img = cv2.imread("img/92307362_p0_master1200.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,30,255,cv2.THRESH_BINARY)
print(ret)
print(binary)
# 自适应阈值（局部阈值）
th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,33,2)
th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,33,2)

cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("binary",binary)
cv2.imshow("th2",th2)
cv2.imshow("th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
