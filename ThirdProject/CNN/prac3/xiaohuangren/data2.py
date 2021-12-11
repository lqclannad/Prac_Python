# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/03 22:05
# 文件名称: data.py
# 开发工具: Pycharm
import os

import numpy as np
import torch
from PIL import Image
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self, root, is_train=True):
        self.dataset = []
        sub_dir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{root}/{sub_dir}"):
            for i,file_name in enumerate(os.listdir(f"{root}/{sub_dir}/{tag}")):
                if i == 2500 and sub_dir == "TRAIN": break
                elif i == 500 and sub_dir == "TEST": break
                tag2 = file_name.split(".")[1:5]
                self.dataset.append((f"{root}/{sub_dir}/{tag}/{file_name}", tag, tag2))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        img = Image.open(self.dataset[index][0])
        img = np.array(img, dtype=np.float32) / 255 - 0.5
        tag1 = np.array([self.dataset[index][1]], dtype=np.float32)
        tag2 = np.array(self.dataset[index][2], dtype=np.float32) / 300
        return torch.Tensor(img), torch.Tensor(tag1), torch.Tensor(tag2)


# 49929 12500
if __name__ == '__main__':
    data = MyDataset("E:/data/xiaohuangren/data")
    print(len(data))
    img,tag1,tag2 = data[4000]
    print(tag1)
    print(tag2*300)
