# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/20 16:45
# 文件名称: test07.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/1.jpg")
img_down = cv2.pyrDown(img)
img_up = cv2.pyrUp(img_down)

# 拉普拉斯金字塔 -- 原图-模糊(先下采样后上采用)
# 得到的是轮廓
img_new = cv2.subtract(img, img_up)
# 为了更容易看清楚，做了个提高对比度的操作
img_new = cv2.convertScaleAbs(img_new, alpha=5, beta=0)

cv2.imshow("img",img)
cv2.imshow("img_up",img_up)
cv2.imshow("img_new",img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
