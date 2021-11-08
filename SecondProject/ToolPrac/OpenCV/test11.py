# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/08 13:16
# 平台: PyCharm
# 文件名: test11.py
from cv2 import cv2

img1 = cv2.imread("img/92307362_p0_master1200.jpg")
img2 = cv2.imread("img/lqclannad_822x1200.png")
print(img2.shape)

# 像素算法运算
dst_and = cv2.bitwise_and(img1,img2)
dst_or = cv2.bitwise_or(img1,img2)
dst_not = cv2.bitwise_not(img1,img2)
dst_xor = cv2.bitwise_xor(img1,img2)
# cv2.imshow("dst_and",dst_and)
# cv2.imshow("dst_or",dst_or)
# cv2.imshow("dst_not",dst_not)
cv2.imshow("dst_xor",dst_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
