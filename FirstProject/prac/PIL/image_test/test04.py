# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/14 14:21
# 平台: PyCharm
# 文件名: test04.py
# func: 裁剪原有图片分辨率为 800x1200(w,h)
import os

import PIL.Image as image

img_path = "../image1"
for name in os.listdir(img_path):
    img = image.open(f'{img_path}/{name}')
    # img.show()
    print(img.size)  # 查看图片的分辨率
    # 0, 0 起始坐标
    # 800, 1200 剪切宽高
    box = (0, 0, 800, 1200)
    p = img.crop(box)
    p.save(f"../image2/{name}")



