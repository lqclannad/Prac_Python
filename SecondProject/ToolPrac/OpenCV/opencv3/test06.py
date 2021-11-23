# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/20 16:31
# 文件名称: test06.py
# 开发工具: Pycharm
import cv2

img = cv2.imread("../img/1.jpg")

for i in range(5):
    cv2.imshow(f"img{i}",img)
    # 下采样
    img = cv2.pyrDown(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
