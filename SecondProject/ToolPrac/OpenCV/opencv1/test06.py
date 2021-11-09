# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/08 9:48
# 平台: PyCharm
# 文件名: test06.py
import numpy as np
from cv2 import cv2

img = cv2.imread("../img/92307362_p0_master1200.jpg")
# cv2.line(img,(400,250),(625,500),color=(0,0,255),thickness=2)
# cv2.circle(img,(50,50),30,(255,0,0),2)
cv2.rectangle(img,(400,250),(625,500),(0,255,0),2)
cv2.ellipse(img,(100,100),(100,50),0,0,360,(0,255,0),-1)

# 多边形
pts = np.array([[50,50],[150,180],[100,300],[0,120]])
cv2.polylines(img,[pts],True,(0,0,255),2)
cv2.putText(img,"hello",(30,330),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,0),5,lineType=cv2.LINE_AA)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
