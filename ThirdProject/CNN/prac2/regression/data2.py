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
        # img = PIL.Image.open(data[0])
        img = cv2.imread(data[0],cv2.IMREAD_GRAYSCALE)
        img = cv2.Laplacian(img,-1)
        # cv2.imshow("img",img)
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
    img_arr, tag, points, img_path = target[0], target[1], target[2], target[3]
    print(img_arr.shape)
