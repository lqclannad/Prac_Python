# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/10 10:59
# 文件名称: test07.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/2.jpg")

'''
Sobel算子
Sobel - ( , ,1,0) - 沿着x轴取梯度
Sobel - ( , ,0,1) - 沿着y轴取梯度
Scharr - 比Sobel的梯度更大，提取的轮廓更亮
'''
S_x = cv2.Sobel(img,-1,1,0)
S_y = cv2.Sobel(img,-1,0,1)
Sc_x = cv2.Scharr(img,-1,1,0)
Sc_y = cv2.Scharr(img,-1,0,1)

cv2.imshow("img",img)
cv2.imshow("S_x",S_x)
cv2.imshow("S_y",S_y)
cv2.imshow("Sc_x",Sc_x)
cv2.imshow("Sc_y",Sc_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
