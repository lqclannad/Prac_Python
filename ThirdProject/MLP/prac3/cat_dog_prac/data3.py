# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/29 19:26
# 文件名称: data3.py
# 开发工具: Pycharm
import os

from PIL import Image
import numpy as np
from torch.utils.data import DataLoader, Dataset


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
        img = Image.open(data[0])
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
