# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/19 15:44
# 文件名称: test01.py
# 开发工具: Pycharm
import cv2
import numpy as np

img = cv2.imread("../img/pic1.jpg")

std = cv2.Canny(img,100,350)

lines_p = cv2.HoughLinesP(std,1,np.pi/180,threshold=80)
print(lines_p)
# 绘制直线
for i in range(len(lines_p)):
    x1,y1,x2,y2 = lines_p[i][0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("img",img)
cv2.imshow("std",std)

cv2.waitKey(0)
cv2.destroyAllWindows()
