# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/18 18:42
# 文件名称: test15.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/23.jpg")

# 1.高斯模糊
dst1 = cv2.GaussianBlur(img, (3,3), 1)
# 2.图片灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 3.Sobel算子
S_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0)
# S_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1)
# S = abs(S_x) + abs(S_y)
# 高亮，并转回8位
absx = cv2.convertScaleAbs(S_x)
# 4.图像二值化
ret, binary = cv2.threshold(absx, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# 5.闭操作
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
image = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
# 6.去噪
kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (20,1))
kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (1,20))
image = cv2.dilate(image, kernelX)
image = cv2.erode(image, kernelX)
image = cv2.erode(image, kernelY)
image = cv2.dilate(image, kernelY)
# 7.中值滤波
image = cv2.medianBlur(image,15)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 8.查找轮廓
contours,_ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 9.判断车牌区域
for item in contours:
    rect = cv2.boundingRect(item)
    x, y, w, h = rect[0],rect[1],rect[2],rect[3]
    print(x,y,w,h)
    if w>2*h:
        chepai = img[y:y+h,x:x+w]
        cv2.imshow("chepai:"+str(x),chepai)
# 绘制轮廓
cv2.imshow("image", image)
cv2.drawContours(image,contours,-1,(0,0,255),2)


cv2.imshow("img", img)
# cv2.imshow("dst1", dst1)
# cv2.imshow("absx", absx)
# cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
