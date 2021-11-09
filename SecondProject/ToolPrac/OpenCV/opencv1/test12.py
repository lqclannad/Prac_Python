# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/08 13:20
# 平台: PyCharm
# 文件名: test12.py
from cv2 import cv2

img = cv2.imread("../img/92307362_p0_master1200.jpg")

h,w,c = img.shape

# 改变大小
dst1 = cv2.resize(img,(w//2,h//2))
# 转置
dst2 = cv2.transpose(img)
# 沿y轴对称
dst3 = cv2.flip(img,1)

cv2.imshow("img",img)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.imshow("dst3",dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
