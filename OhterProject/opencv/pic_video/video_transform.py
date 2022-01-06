# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/03 21:40
# 文件名称: video_transform.py
# 开发工具: Pycharm
import cv2
import numpy as np

video = cv2.VideoCapture("video/1.mp4")
i = 0
while True:
    ret, frame = video.read()
    if ret:
        h, w, c = frame.shape   # (480, 854, 3)
        if frame is None:
            continue
        i += 1
        frame2=np.transpose(frame,(1,0,2))
        # frame2 = cv2.resize(frame,(h,w))
        cv2.imwrite(f"img/{i}.jpg", frame2)
        if cv2.waitKey(1000//24) & 0xFF == ord('q'):
            break
video.release()
cv2.destroyAllWindows()
