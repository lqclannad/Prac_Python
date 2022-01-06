# coding: utf-8
# 用户: 刘泉
# 时间: 2021/12/14 14:18
# 平台: PyCharm
# 文件名: test01.py
import PIL.Image
import numpy as np
import torch
from torchvision import transforms

import utils

####### 第一个for循环 #######
# p_cls = 0.6
# _cls = torch.randn((1,1,6,7))
# _offset = torch.randn((1,4,6,7))
# print("_cls:",_cls)
# print("_offset:",_offset)
# cls= _cls[0][0]
# offset = _offset[0]
# idxs = torch.nonzero(torch.gt(cls, p_cls))
# print(idxs)
# print(cls[idxs[:,0],idxs[:,1]])
# print(offset[idxs[:,0],idxs[:,1]])


####### 第二个for循环 #######
# image = PIL.Image.open("test_images/img.png")
# _pnet_boxes = torch.randn(15,5)
# _x1 = _pnet_boxes[:,0]
# _y1 = _pnet_boxes[:,1]
# _x2 = _pnet_boxes[:,2]
# _y2 = _pnet_boxes[:,3]
# img = image.crop((_x1,_y1,_x2,_y2))
# img = img.resize((24,24))
# img_data = transforms.Compose([transforms.ToTensor(img)])


####### 第三个for循环 #######
r_cls = 0.6
cls = torch.randn((1,6,7))
offset = torch.randn((4,6,7))
idxs, _ = np.where(cls > r_cls)

print("cls:",cls)
print("offset:",offset)
print("idxs:",idxs)
