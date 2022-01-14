# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/13 12:21
# 文件名称: make_label.py
# 开发工具: Pycharm
import os
from xml.etree import cElementTree as ET

from FourthProject.YOLO.v3.make import cfg

dir = "outputs"
lines = []
for i in range(1,21):
    line = ""
    tree = ET.parse(os.path.join(dir, f"{i}.xml"))

    ################ path ################
    path = f"data/{i}.jpeg "
    line += path

    ################ img_w,img_h ################
    img_w, img_h = tree.findtext("./size/width"), tree.findtext("./size/height")
    img_w, img_h = int(img_w), int(img_h)
    if img_w > img_h:
        img_h = img_w
    else:
        img_w = img_h

    ################ name,cx,cy,w,h ################
    objs = tree.iter("object")
    for obj in objs:
        obj_index = -1
        obj_name = obj.findtext("item/name")
        for i in range(4):
            if obj_name == cfg.CLASS_NAME[i]:
                obj_index = i
                break
        items = obj.iter("item")
        for item in items:
            x1 = int(item.findtext("bndbox/xmin"))
            y1 = int(item.findtext("bndbox/ymin"))
            x2 = int(item.findtext("bndbox/xmax"))
            y2 = int(item.findtext("bndbox/ymax"))
            cx = round((x1+x2) / 2 / img_w * 416)
            cy = round((y1+y2) / 2 / img_h * 416)
            w = round((x2 - x1) / img_w * 416)
            h = round((y2 - y1) / img_h * 416)
            line += f"{obj_index} {cx} {cy} {w} {h} "
        line += "\n"
    lines.append(line)
with open("label.txt", 'w') as f:
    for line in lines:
        f.write(line)
