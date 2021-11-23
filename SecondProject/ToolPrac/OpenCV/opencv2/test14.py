# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/18 17:12
# 文件名称: test14.py
# 开发工具: Pycharm
import cv2
import numpy as np

img = cv2.imread("../img/17.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 边界矩形
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)

# 最小矩形
rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box)
img_contour = cv2.drawContours(img, [box], 0, (0,255,0), 2)

# 最小外切圆
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))
radius = int(radius)
img_contour = cv2.circle(img, center, radius, (255,0,0), 2)

# 边界矩形的宽高比
x,y,w,h = cv2.boundingRect(contours[0])
aspect_ratio = float(w)/h
print('aspect_ratio',aspect_ratio)

# 轮廓面积与边界矩形面积的比
area = cv2.contourArea(contours[0])
x,y,w,h = cv2.boundingRect(contours[0])
rect_area = w*h
extent = float(area)/rect_area
print(f'轮廓面积/边界矩形面积={area}/{rect_area}={extent}')

# 轮廓面积与凸包面积的比
area = cv2.contourArea(contours[0])
hull = cv2.convexHull(contours[0])
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print(solidity)

# 与轮廓面积相等的圆形的直径
area = cv2.contourArea(contours[0])
equi_diameter = np.sqrt(4*area/np.pi)
print(equi_diameter)

# 对象的方向
(x, y), (MA, ma), angle = cv2.fitEllipse(contours[0])
print(angle)

cv2.drawContours(img,contours,0,(0,0,255),3)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
