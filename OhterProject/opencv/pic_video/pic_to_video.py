# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/03 21:40
# 文件名称: video_transform.py
# 开发工具: Pycharm
import glob

import cv2


if __name__ == '__main__':
    sort_arr = []
    img_arr = []
    w, h = 480, 854
    for i in range(1,12660):
        sort_arr.append(f"img/{i}.jpg")
    for f in sort_arr:
        img = cv2.imread(f)
        if img is None:
            print(f"{f} is Error")
            continue
        img_arr.append(img)

    fps = 25
    out = cv2.VideoWriter("videowc/1.wmv", cv2.VideoWriter_fourcc(*'MP42'), fps, (w, h))
    for i in range(12659):
        print(i)
        out.write(img_arr[i])
    out.release()
