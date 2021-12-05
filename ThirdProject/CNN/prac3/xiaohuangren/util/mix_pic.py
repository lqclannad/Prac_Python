# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/03 22:07
# 文件名称: mix_pic.py
# 开发工具: Pycharm
import os
import random

import PIL
from PIL import Image
import numpy as np

bg_path = "E:/data/xiaohuangren/bg_pic"
x = 1

for sub_dir in os.listdir(bg_path):
    for filename in os.listdir(f"{bg_path}/{sub_dir}"):
        try:
            background = Image.open("{0}/{1}/{2}".format(bg_path, sub_dir, filename))
            shape = np.shape(background)
            if len(shape) == 3 and shape[0] > 100 and shape[1] > 100:
                background = background
            else:
                continue
            background_resize = background.resize((300, 300))
            background_resize = background_resize.convert("RGB")
            name = np.random.randint(1, 21)
            img_font = Image.open("E:/data/xiaohuangren/yellow/{0}.png".format(name))
            ran_w = np.random.randint(50, 180)
            img_new = img_font.resize((ran_w, ran_w))

            ran_x1 = np.random.randint(0, 300 - ran_w)
            ran_y1 = np.random.randint(0, 300 - ran_w)

            r, g, b, a = img_new.split()
            rand = random.randint(0, 4)
            if rand > 0:
                background_resize.paste(img_new, (ran_x1, ran_y1), mask=a)

                ran_x2 = ran_x1 + ran_w
                ran_y2 = ran_y1 + ran_w

                background_resize.save("E:/data/xiaohuangren/data/TRAIN/1/{0}{1}.png".format(x, "." + str(ran_x1) + "." + str(ran_y1) +
                                                                  "." + str(ran_x2) + "." + str(ran_y2)))
            else:
                background_resize.save("E:/data/xiaohuangren/data/TRAIN/0/{0}{1}.png".format(x, ".0.0.0.0"))

            x += 1
        except PIL.UnidentifiedImageError:
            print(f"PIL.UnidentifiedImageError==>{bg_path}/{sub_dir}/{filename}")
        except OSError:
            print(f"OSError==>{bg_path}/{sub_dir}/{filename}")
