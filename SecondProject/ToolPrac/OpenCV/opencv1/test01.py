# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/05 11:25
# 平台: PyCharm
# 文件名: test01.py

import cv2.cv2 as cv2

# cap = cv2.VideoCapture(0)  # 读取摄像头
# cap = cv2.VideoCapture("http://39.134.65.162/PLTV/88888888/224/3221225611/index.m3u8")  #读取视频流
cap = cv2.VideoCapture("cup.mp4")  #读取视频文件

while (True):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)
        if cv2.waitKey(1000//24) & 0xFF == ord('q'):
            break
    else:
        print(".....")
        break

cap.release()
cv2.destroyAllWindows()
