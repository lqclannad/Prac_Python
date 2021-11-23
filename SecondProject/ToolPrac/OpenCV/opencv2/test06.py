# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/10 9:38
# 文件名称: test06.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/1.jpg")

# USM锐化 - 2倍原图减去高斯模糊
dst1 = cv2.GaussianBlur(img, (5, 5), 0)
dst2 = cv2.addWeighted(img, 2, dst1, -1, 0)
# 拉普拉斯锐化(高通滤波) - 提取边缘、轮廓
dst3 = cv2.Laplacian(img, -1)

cv2.imshow("img", img)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
