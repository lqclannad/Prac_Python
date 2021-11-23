# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/21 17:36
# 文件名称: red_green_light.py
# 开发工具: Pycharm
import cv2
import numpy as np

img = cv2.imread("img/img_2.png")
# 1.高斯模糊
dst = cv2.GaussianBlur(img, (5, 5), 1)
# 2.图片灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 3.Sobel算子
S_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
absX = cv2.convertScaleAbs(S_x)
# 4.二值化
ret, binary = cv2.threshold(absX, 0, 255, cv2.THRESH_OTSU)
# 5.闭操作
kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
dst2 = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelX)
cv2.imshow("dst2", dst2)
# 6.膨胀腐蚀
kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 20))
dst2 = cv2.dilate(dst2, kernelX)
dst2 = cv2.erode(dst2, kernelX)
dst2 = cv2.erode(dst2, kernelY)
dst2 = cv2.dilate(dst2, kernelY)
# 7.中值滤波
dst3 = cv2.medianBlur(dst2, 5)
cv2.imshow("dst3", dst3)
# 8.轮廓提取
contours, _ = cv2.findContours(dst3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 9.判断区域
# red色调
lower_hsv_red = np.array([139, 56, 100])
upper_hsv_red = np.array([179, 255, 255])
# green色调
lower_hsv_green = np.array([32, 73, 169])
upper_hsv_green = np.array([92, 255, 255])
for contour in contours:
    contour = cv2.boundingRect(contour)
    x,y,w,h = contour[0],contour[1],contour[2],contour[3]
    if w*2<h and h<w*2.5:
        light = img[y:y+h,x:x+w]
        light = cv2.cvtColor(light,cv2.COLOR_BGR2HSV)
        mask_red = cv2.inRange(light, lowerb=lower_hsv_red, upperb=upper_hsv_red)
        mask_grren = cv2.inRange(light, lowerb=lower_hsv_green, upperb=upper_hsv_green)
        if np.max(mask_red) == 255:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255))
        elif np.max(mask_grren) == 255:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))
        else:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0))
        mask_red = None
        mask_green = None
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
