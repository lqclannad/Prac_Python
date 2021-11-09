# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/08 13:10
# 平台: PyCharm
# 文件名: test10.py
from cv2 import cv2

img1 = cv2.imread("../img/92307362_p0_master1200.jpg")
img2 = cv2.imread("../img/lqclannad_822x1200.png")

dst1 = cv2.add(img1, img2)
dst2 = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
