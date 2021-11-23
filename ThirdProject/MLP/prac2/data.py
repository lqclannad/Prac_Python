# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/22 21:33
# 文件名称: data.py
# 开发工具: Pycharm
import os

import cv2
import numpy as np
from torch.utils.data import Dataset, DataLoader


class MNISTDataset(Dataset):
    # 初始化数据集
    def __init__(self,root,is_train=True):
        # 记录所有数据
        self.train_dataset = []
        sub_dir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{root}/{sub_dir}"):
            img_dir = f"{root}/{sub_dir}/{tag}"
            for img_filename in os.listdir(img_dir):
                img_path = f"{img_dir}/{img_filename}"
                self.train_dataset.append((img_path,tag))

    # 返回数据集的长度
    def __len__(self):
        return len(self.train_dataset)

    # 对每个数据做处理
    def __getitem__(self, index):
        data = self.train_dataset[index]

        img_data = cv2.imread(data[0],cv2.IMREAD_GRAYSCALE)
        img_data = img_data.reshape(-1)
        img_data = img_data/255

        # one_hot
        tag_one_hot = np.zeros(10)
        tag_one_hot[int(data[1])] = 1

        return np.float32(img_data),np.float32(tag_one_hot)


if __name__ == '__main__':
    dataset = MNISTDataset("E:\data\MNIST_IMG")
    train_loader = DataLoader(dataset,batch_size=500,shuffle=True)
    for i,(x,y) in enumerate(train_loader):
        print(i)
        print(x.shape)
        print(y.shape)
