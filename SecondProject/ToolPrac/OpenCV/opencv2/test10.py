# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/17 19:57
# 文件名称: test10.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/24.jpg")
cv2.imshow("img",img)

# 增亮
img = cv2.convertScaleAbs(img,alpha=6,beta=5)
# 高斯模糊
dst = cv2.GaussianBlur(img,(5,5),1)
# 卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# 开操作(先腐蚀后膨胀) - 去噪
dst = cv2.morphologyEx(dst,cv2.MORPH_OPEN,kernel)
# 闭操作(先膨胀后腐蚀) - 补空洞
dst = cv2.morphologyEx(dst,cv2.MORPH_CLOSE,kernel)
cv2.imshow("dst",dst)
# 画边缘
dst2 = cv2.Canny(dst,80,150)
cv2.imshow("dst2",dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()
