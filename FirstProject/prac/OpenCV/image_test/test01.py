# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/12 22:40
# 文件名称: test01.py
# 开发工具: Pycharm
import cv2

# ★★★ opencv
img = cv2.imread("../image/92307362_p0_master1200.jpg")

blue = (255, 0, 0)
# 画线
cv2.line(img, (10, 10), (100, 10), blue, 1)
# 画矩形
cv2.rectangle(img, (50, 50), (150, 150), blue)
# 画圆
cv2.circle(img, (50, 50), 50, blue)
# 展示图片
cv2.imshow("image", img)
# 设置等待任意键销毁资源
cv2.waitKey(0)
cv2.destroyAllWindows()
