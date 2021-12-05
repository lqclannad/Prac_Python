# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/03 22:05
# 文件名称: data.py
# 开发工具: Pycharm
import os

import numpy as np
from PIL import Image
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self,root,is_train=True):
        self.dataset = []
        sub_dir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{root}/{sub_dir}"):
            for file_name in os.listdir(f"{root}/{sub_dir}/{tag}"):
                tags = file_name.split(".")[1:5]
                tags.insert(0, tag)
                self.dataset.append((f"{root}/{sub_dir}/{tag}/{file_name}", tags))

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        img = Image.open(self.dataset[index][0])
        img = np.array(img, dtype=np.float32) / 255 - 0.5
        tags = np.zeros(5)
        tags[0] = self.dataset[index][1][0]
        tags[1:] = np.array(self.dataset[index][1][1:], dtype=np.float32) / 300
        return img, tags

# 49929 12500
if __name__ == '__main__':
    data = MyDataset("E:/data/xiaohuangren/data")
    tag = data[10022][1]
    print(tag.dtype)
