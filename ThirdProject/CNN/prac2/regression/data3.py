# coding: utf-8
# 用户: 刘泉
# 时间: 2021/12/02 9:55
# 平台: PyCharm
# 文件名: data3.py
import os

import PIL.Image
from cv2 import cv2
import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


class MyDataset(Dataset):
    def __init__(self,root,train=True):
        super().__init__()
        self.dataset = []
        sub_dir = "TRAIN" if train else "TEST"
        for tag in os.listdir(f"{root}/{sub_dir}"):
            for filename in os.listdir(f"{root}/{sub_dir}/{tag}"):
                img_path = root + "/" + sub_dir + "/" + tag + "/" + filename
                tag2 = filename.split(".")[1:5]
                tag2.insert(0,tag)
                self.dataset.append((img_path, tag2))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        img = PIL.Image.open(self.dataset[index][0])
        img = np.array(img)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = cv2.Laplacian(img,-1)
        img = img / 255 - 0.5
        print(self.dataset[index][1])
        return np.array(img,dtype=np.float32), np.array()



if __name__ == '__main__':
    dataset = MyDataset("G:/code/python/Prac_Python/ThirdProject/CNN/prac2/regression/data")
    dataset[9000]


