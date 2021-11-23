# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/20 15:18
# 文件名称: test04.py
# 开发工具: Pycharm
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../img/16.jpg",0)

his = cv2.calcHist(img,[0],None,[256],[0,256])
plt.plot(his,color="r")

# 直方图均衡化 - 拉宽色域
dst = cv2.equalizeHist(img)
his = cv2.calcHist(dst,[0],None,[256],[0,256])
plt.plot(his,color="b")

cv2.imshow("img",img)
cv2.imshow("dst",dst)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
