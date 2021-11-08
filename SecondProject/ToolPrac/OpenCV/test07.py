# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/08 12:38
# 平台: PyCharm
# 文件名: test07.py
from cv2 import cv2

img = cv2.imread("img/92307362_p0_master1200.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值化
ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(ret)
print(binary)
cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("binary",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
