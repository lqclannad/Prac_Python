# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/26 13:04
# 平台: PyCharm
# 文件名: data2.py
import os

from cv2 import cv2
import numpy as np
from torch.utils.data import Dataset, DataLoader


class MNISTDataset(Dataset):
    # 初始化数据集
    def __init__(self, root, is_train=True):
        self.dataset = []  # 记录测试数据
        sub_dir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{root}/{sub_dir}"):
            img_dir = f"{root}/{sub_dir}/{tag}"
            for img_filename in os.listdir(img_dir):
                img_path = f"{img_dir}/{img_filename}"
                self.dataset.append((img_path, tag))

    # 统计数据集的长度
    def __len__(self):
        return len(self.dataset)

    # 每条数据的处理方式
    def __getitem__(self, index):
        data = self.dataset[index]

        img_data = cv2.imread(data[0])
        img_data = cv2.cvtColor(img_data,cv2.COLOR_BGR2RGB)
        img_data = img_data.reshape(3,28,28)
        img_data = img_data / 255  # 归一化

        # one_hot
        tag_one_hot = np.zeros(10)
        tag_one_hot[int(data[1])] = 1
        return np.float32(img_data), np.float32(tag_one_hot)


if __name__ == '__main__':
    dataset = MNISTDataset("E:\data\MNIST_IMG")
    train_loader = DataLoader(dataset,batch_size=500,shuffle=True)
    # x - 图像数据 ， y - 标签
    for i,(x,y) in enumerate(train_loader):
        print(i)
        print(x.shape)
        print(y.shape)
