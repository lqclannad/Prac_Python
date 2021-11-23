# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/19 16:25
# 文件名称: test03.py
# 开发工具: Pycharm
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../img/23.jpg")

img_B = cv2.calcHist(img,[0],None,[256],[0,256])
print(img_B)
plt.plot(img_B,label="B",color="b")

img_G = cv2.calcHist(img,[1],None,[256],[0,256])
plt.plot(img_G,label="G",color="g")

img_R = cv2.calcHist(img,[2],None,[256],[0,256])
plt.plot(img_R,label="R",color="r")

cv2.imshow("img",img)
plt.legend()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
