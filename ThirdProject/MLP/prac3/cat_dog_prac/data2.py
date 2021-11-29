# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/24 11:28
# 平台: PyCharm
# 文件名: data2.py
import os

import PIL.Image
import numpy as np
from torch.utils.data import Dataset, DataLoader
import torch


class MyDataset(Dataset):
    def __init__(self, root, is_train):
        super().__init__()
        self.dataset = []
        sub_dir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{root}/{sub_dir}"):
            for filename in os.listdir(f"{root}/{sub_dir}/{tag}"):
                self.dataset.append((root + "/" + sub_dir + "/" + tag + "/" + filename, tag))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        data = self.dataset[index]
        img = PIL.Image.open(data[0])
        img = np.array(img) / 255
        tag = [int(data[1])]
        return np.float32(img), np.float32(tag)


if __name__ == '__main__':
    data = MyDataset("E:/data/cat_dog",True)
    data_loader = DataLoader(data,batch_size=512,shuffle=True)
    for i,(img,tag) in enumerate(data_loader):
        # print("img",img)
        print(tag)
        print(tag.dtype)
        print(img.shape)
        # print(tag.shape)
