# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/18 15:29
# 文件名称: test11.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/26.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值图
ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# 找轮廓
contours,hierachy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours[0].shape)
print(contours)
M = cv2.moments(contours[0])
print("M:",M)
cx,cy = int(M['m10']/M['m00']),int(M['m01']/M['m00'])
print("重心：", cx, cy)
area = cv2.contourArea(contours[0])
print("面积：", area)
perimeter = cv2.arcLength(contours[0],True)
print("周长：", perimeter)
cv2.drawContours(img,contours,-1,(0,0,255),3)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
