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
    def __init__(self, root):
        super().__init__()
        self.dataset = []
        for filename in os.listdir(root):
            tag = filename[0]
            self.dataset.append((root + "/" + filename, tag))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        data = self.dataset[index]
        img = PIL.Image.open(data[0])
        img = np.array(img) / 255
        tag = torch.tensor([int(data[1])], dtype=torch.float32)
        return img, tag


if __name__ == '__main__':
    data = MyDataset("E:/data/cat_dog/img")
    data_loader = DataLoader(data,batch_size=512,shuffle=True)
    for i,(img,tag) in enumerate(data_loader):
        print(img.shape)
        print(tag.shape)
