# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/19 16:17
# 文件名称: test02.py
# 开发工具: Pycharm
import cv2
import numpy as np

img = cv2.imread("../img/50.jpg")

dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测圆
circles = cv2.HoughCircles(dst, cv2.HOUGH_GRADIENT,1,30,param1=40,param2=20,minRadius=30,maxRadius=80)
print(circles)

if not circles is None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
