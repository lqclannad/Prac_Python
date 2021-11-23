# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/18 17:02
# 文件名称: test12.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/17.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours,hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

epsilon = 12  # 误差
approx = cv2.approxPolyDP(contours[0], epsilon, True)
print(approx)
cv2.drawContours(img,[approx],-1,(0,0,255),3)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
