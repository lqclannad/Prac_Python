# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/05 15:17
# 平台: PyCharm
# 文件名: test02.py
import cv2.cv2 as cv2

img1 = cv2.imread("../img/92307362_p0_master1200.jpg")
img2 = cv2.imread("../img/lqclannad_822x1200.png")
img = cv2.bitwise_or(img1,img2)
# img = cv2.bitwise_not(img2)
# img = cv2.bitwise_xor(img1,img2)
# img = cv2.bitwise_and(img1,img2)


cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
