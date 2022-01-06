# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/15 20:40
# 文件名称: detect.py
# 开发工具: Pycharm
import os
import time

import cv2
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont
from torchvision import transforms

# from ThirdProject.MTCNN.prac1 import nets
from ThirdProject.MTCNN.prac1 import utils
from ThirdProject.MTCNN.prac1.test.face_detect import nets

# 网络调参
# P网络:
p_cls = 0.6 #原为0.6
p_nms = 0.1 #原为0.5
# R网络：
r_cls = 0.6 #原为0.6
r_nms = 0.5 #原为0.5
# o网络：
o_cls = 0.9 #原为0.97
o_nms = 0.5 #原为0.7



class Detector:
    def __init__(self, pnet_param="param/pnet.pt", rnet_param="param/rnet.pt", onet_param="param/onet.pt", isCuda=True):
        self.isCuda = isCuda

        # 初始化三个网络
        self.pnet = nets.PNet()
        self.rnet = nets.RNet()
        self.onet = nets.ONet()

        # 传入cuda给模型加速
        if self.isCuda:
            self.pnet.cuda()
            self.rnet.cuda()
            self.onet.cuda()

        # 加载训练好的权重
        self.pnet.load_state_dict(torch.load(pnet_param))
        self.rnet.load_state_dict(torch.load(rnet_param))
        self.onet.load_state_dict(torch.load(onet_param))

        #
        self.pnet.eval()
        self.rnet.eval()
        self.onet.eval()

        # 图片数据类型转换
        self.__image_transform = transforms.Compose([
            transforms.ToTensor()
        ])

    def detect(self, image):
        # p网络检测 ---- 1st
        start = time.time()
        pnet_boxes = self.__pnet_detect(image)
        if pnet_boxes.shape[0] == 0:
            return torch.Tensor([])
        end = time.time()
        p_time = end - start

        # R网络检测 ---- 2nd
        start = time.time()
        rnet_boxes = self.__rnet_detect(image, pnet_boxes)
        end = time.time()
        r_time = end - start

        # O网络检测 ---- 3rd
        start = time.time()
        onet_boxes = self.__onet_detect(image, rnet_boxes)
        end = time.time()
        o_time = end - start
        return onet_boxes


    # 创建p网络检测函数
    def __pnet_detect(self, image):
        # 创建空盒子用以接收符合条件的框
        boxes = torch.Tensor([])

        img = image
        h, w, c = img.shape
        # 找出较小的边
        min_side_len = min(w, h)

        scale = 1
        while min_side_len > 12:
            # 对图像数据做系列处理
            img_data = self.__image_transform(img)  # hwc->chw, 归一化, 转tensor
            # 放入cuda加速
            if self.isCuda:
                img_data = img_data.cuda()
            # print(img_data.shape)     # [3, 601, 800]
            # img_data.unsqueeze(0)     # [3, 601, 800]
            img_data.unsqueeze_(0)  # [1, 3, 601, 800]  chw -> nchw
            _cls, _offset = self.pnet(img_data)

            # 置信度
            cls = _cls[0, 0].cpu().data  # [296, 395]
            # 偏移量
            offset = _offset[0].cpu().data  # [4, 296, 395]
            index = torch.nonzero(torch.gt(cls, p_cls))
            # shape [5,n].T -> [n,5]
            boxs = self._box(index, cls[index[:, 0], index[:, 1]], offset[:, index[:, 0], index[:, 1]], scale).T

            if boxes.shape[0] == 0:
                boxes = boxs.clone()
            else:
                boxes = torch.vstack((boxes, boxs))

            scale *= 0.7
            _w = int(w*scale)
            _h = int(h*scale)

            # img = img.resize((_w,_h))
            # for box in boxes:
            #     cv2.rectangle(img, (box[0],box[1]), (box[2],box[3]), (0,0,255), 2)
            img = cv2.resize(img, (_w, _h), interpolation=cv2.INTER_CUBIC)
            min_side_len = min(_w,_h)
        return utils.nms(boxes, p_nms)

    def _box(self, index, cls, offset, scale, stride=2, side_len=12):
        _x1 = (index[:, 1].float() * stride) / scale
        _y1 = (index[:, 0].float() * stride) / scale
        _x2 = (index[:, 1].float() * stride + side_len - 1) / scale
        _y2 = (index[:, 0].float() * stride + side_len - 1) / scale
        ow = _x2 - _x1
        oh = _y2 - _y1
        x1 = _x1 + ow * offset[0]
        y1 = _y1 + oh * offset[1]
        x2 = _x2 + ow * offset[2]
        y2 = _y2 + oh * offset[3]
        box = torch.stack([x1,y1,x2,y2,cls])
        return box

    # r模型检测函数
    def __rnet_detect(self, image, pnet_boxes):
        # 用于存放抠图
        _img_dataset = []
        # [5,2033]
        _pnet_boxes = utils.convert_to_square(pnet_boxes)
        _x1 = _pnet_boxes[:,0]
        _y1 = _pnet_boxes[:,1]
        _x2 = _pnet_boxes[:,2]
        _y2 = _pnet_boxes[:,3]
        for i in range(len(_x1)):
            x1 = _x1[i].item()
            y1 = _y1[i].item()
            x2 = _x2[i].item()
            y2 = _y2[i].item()
            img = image[round(y1):round(y2),round(x1):round(x2)]
            img = cv2.resize(img, (24, 24), interpolation=cv2.INTER_CUBIC)
            img = self.__image_transform(img)
            _img_dataset.append(img)
        img_dataset = torch.stack(_img_dataset)     # [2033, 3, 24, 24]
        if self.isCuda:
            img_dataset = img_dataset.cuda()
        _cls, _offset = self.rnet(img_dataset)
        cls = _cls.cpu().data           # [n, 1]
        offset = _offset.cpu().data     # [n, 4]
        indexs, _ = torch.where(cls > r_cls)       # index [n,]
        _x1 = _x1[indexs]
        _y1 = _y1[indexs]
        _x2 = _x2[indexs]
        _y2 = _y2[indexs]
        ow = _x2 - _x1
        oh = _y2 - _y1
        x1 = _x1 + ow * offset[indexs, 0]
        y1 = _y1 + oh * offset[indexs, 1]
        x2 = _x2 + ow * offset[indexs, 2]
        y2 = _y2 + oh * offset[indexs, 3]
        cls = cls[indexs, 0]
        boxs = torch.stack((x1,y1,x2,y2,cls)).T
        t1 = utils.nms(boxs,r_nms)
        return utils.nms(boxs,r_nms)

    def __onet_detect(self, image, rnet_box):
        _img_dataset = []
        _rnet_boxes = utils.convert_to_square(rnet_box)
        _x1 = _rnet_boxes[:,0]
        _y1 = _rnet_boxes[:,1]
        _x2 = _rnet_boxes[:,2]
        _y2 = _rnet_boxes[:,3]
        for i in range(len(_x1)):
            x1 = _x1[i].item()
            y1 = _y1[i].item()
            x2 = _x2[i].item()
            y2 = _y2[i].item()
            img = image[round(y1):round(y2),round(x1):round(x2)]
            img = cv2.resize(img, (48,48), interpolation=cv2.INTER_CUBIC)
            img = self.__image_transform(img)
            _img_dataset.append(img)
        img_dataset = torch.stack(_img_dataset)
        if self.isCuda:
            img_dataset = img_dataset.cuda()
        _cls, _offset = self.onet(img_dataset)
        cls = _cls.cpu().data
        offset = _offset.cpu().data
        indexs, _ = torch.where(cls > o_cls)
        _x1 = _x1[indexs]
        _y1 = _y1[indexs]
        _x2 = _x2[indexs]
        _y2 = _y2[indexs]
        ow = _x2 - _x1
        oh = _y2 - _y1
        x1 = _x1 + ow * offset[indexs, 0]
        y1 = _y1 + oh * offset[indexs, 1]
        x2 = _x2 + ow * offset[indexs, 2]
        y2 = _y2 + oh * offset[indexs, 3]
        cls = cls[indexs, 0]
        boxs = torch.stack((x1,y1,x2,y2,cls)).T
        t2 = utils.nms(boxs,o_nms)
        return utils.nms(boxs,o_nms)


if __name__ == '__main__':
    font = ImageFont.truetype("font/arial.ttf", size=23)
    for i, img in enumerate(os.listdir("img")):
        print("====================\n", img)
        d = Detector()
        img = cv2.imread(f"img/{img}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = d.detect(img)
        for box in boxes:  # 多个框，每循环一次框一个人脸
            x1 = int(box[0])
            y1 = int(box[1])
            x2 = int(box[2])
            y2 = int(box[3])

            print((x1, y1, x2, y2))
            print("置信度:",box[4])
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.putText(img,str(box[4].item())[:5],(x1,y1-20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow(f"{i}",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # with Image.open(f"img/{img}") as im:
        #     print("-------------------")
        #     print("size:",im.size)
        #     print("boxes:",boxes)
        #     imDraw = ImageDraw.Draw(im)
        #     for box in boxes:  # 多个框，没循环一次框一个人脸
        #         x1 = int(box[0])
        #         y1 = int(box[1])
        #         x2 = int(box[2])
        #         y2 = int(box[3])
        #
        #         print((x1, y1, x2, y2))
        #
        #         print("conf:", box[4])  # 置信度
        #         imDraw.rectangle((x1, y1, x2, y2), outline='red')
        #         imDraw.text((x1, y1), "{:.2f}".format(box[4]), font=font, fill=(255, 0, 255))
        #         # im.show() # 每循环一次框一个人脸
        #     im.show()
