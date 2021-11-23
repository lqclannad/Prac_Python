# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/22 16:48
# 文件名称: skin.py
# 开发工具: Pycharm
import cv2
import numpy as np

cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 皮肤色调阈值
    lower_blue = np.array([0,18,102])
    upper_blue = np.array([17,133,242])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    img = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("show HSV", np.hstack((frame,img)))
    if cv2.waitKey(42) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
