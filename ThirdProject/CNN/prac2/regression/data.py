# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/30 10:22
# 平台: PyCharm
# 文件名: data.py
import os

import PIL.Image
import numpy as np
import torch
from torch.utils.data import Dataset
from PIL import Image, ImageDraw
from cv2 import cv2

class MyDataset(Dataset):
    def __init__(self,root,is_train=True):
        super().__init__()
        self.dataset = []
        sub_dir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{root}/{sub_dir}"):
            for file_name in os.listdir(f"{root}/{sub_dir}/{tag}"):
                img_path = root + "/" + sub_dir + "/" + tag + "/" + file_name
                points = file_name.split(".")[1:5]
                self.dataset.append((img_path,tag,points))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        data = self.dataset[index]
        img = PIL.Image.open(data[0])
        # img = cv2.imread(data[0])
        # img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # S_x = cv2.Sobel(img1,-1,1,0)
        # S_y = cv2.Sobel(img1,-1,0,1)
        # S = abs(S_x) + abs(S_y)
        # img2 = cv2.convertScaleAbs(S)
        # ret,binary = cv2.threshold(img2,250,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # cv2.imshow("img",img)
        # cv2.imshow("img1",img1)
        # cv2.imshow("binary",binary)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        img_arr = np.array(img,dtype=np.float32) / 255 - 0.5     # 归一化，去均值化
        tag = np.array([data[1]],dtype=np.float32)
        points = np.array(data[2],dtype=np.float32) / 300
        target = [img_arr, tag, points, data[0]]
        return target


if __name__ == '__main__':
    train_dataset = MyDataset(r"G:/code/python/Prac_Python/ThirdProject/CNN/prac2/regression/data",True)
    test_dataset = MyDataset(r"G:/code/python/Prac_Python/ThirdProject/CNN/prac2/regression/data",False)
    print(len(train_dataset))
    print(len(test_dataset))
    target = train_dataset[9000]
    img_arr = np.array((target[0]+0.5) * 255,dtype=np.uint8)
    print(img_arr.shape)
    img = Image.fromarray(img_arr)
    img1 = ImageDraw.Draw(img,"RGB")
    x1,y1,x2,y2 = np.array(target[2] * 300,dtype=np.uint8)
    img1.rectangle(((x1,y1),(x2,y2)),outline='red',width=2)
    img.show()
