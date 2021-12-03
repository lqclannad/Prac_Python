# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/30 13:33
# 平台: PyCharm
# 文件名: train.py
import PIL.Image
import numpy as np
import torch
from torch import optim, nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from data import MyDataset
from net import Classification

train_dataset = MyDataset(r"G:/code/python/Prac_Python/ThirdProject/CNN/prac2/regression/data", True)
test_dataset = MyDataset(r"G:/code/python/Prac_Python/ThirdProject/CNN/prac2/regression/data", False)

train_loader = DataLoader(train_dataset, batch_size=50, shuffle=True)
# test_loader = DataLoader(test_dataset, batch_size=10, shuffle=True)

DEVICE = "cuda"

summaryWriter = SummaryWriter("logs1")

if __name__ == '__main__':
    net1 = Classification().to(DEVICE)
    opt1 = optim.Adam(net1.parameters())
    loss_func1 = nn.MSELoss()

    step = 0
    step2 = 0
    for epoch in range(10000):
        sum_score = 0
        max_score = 0
        for i, target in enumerate(train_loader):
            img_path_arr = []  # 存储判有小黄人的图片集
            img, tag1, tag2, img_path = target[0], target[1], target[2], target[3]  # 输入图片信息,标签1,标签2
            img, tag1 = img.to(DEVICE), tag1.to(DEVICE)

            img = img.permute(0, 3, 1, 2).float()

            out1 = net1(img)
            t_out = torch.gt(out1,0.5)
            # t_out = t_out.permute(1,0)[0]
            # tag2 = tag2[t_out].to(DEVICE)
            train_loss = loss_func1(out1, tag1)
            print("t_out:",t_out)
            print("tag1:",tag1)

            opt1.zero_grad()
            train_loss.backward()
            opt1.step()

            print("train_loss:",train_loss)
            summaryWriter.add_scalar("train_loss", train_loss, step)

            score = torch.sum(torch.eq(t_out, tag1).float())
            if score > max_score:
                # 保存模型的权重
                torch.save(net1.state_dict(), f"param/classfication1.pt")

            # out_1 = out1.detach().cpu()
            # print("out_1:", out_1)
            # for i, j in enumerate(out_1):
            #     if j[0] > 0.5:
            #         img_path_arr.append(img_path[i])
            # step += 1
            #
            # imgs = []
            # if len(img_path_arr) > 0:
            #     for img_path in img_path_arr:
            #         img = PIL.Image.open(img_path)
            #         imgs.append(np.array(img, dtype=np.float32) / 255 - 0.5)
            #     imgs = torch.tensor(imgs, dtype=torch.float32)
            #     imgs = imgs.permute(0, 3, 1, 2).to(DEVICE)
            #     print("net2:imgs:", imgs)
            #     print("net2:imgs.shape:", imgs.shape)
            #
            #     out2 = net2(imgs)
            #     print("out2:", out2)
            #     train_loss2 = loss_func2(out2, tag2)
            #
            #     opt2.zero_grad()
            #     train_loss2.backward()
            #     opt2.step()
            #
            #     print("train_loss2:", train_loss2)
            #     summaryWriter.add_scalar("train_loss2",train_loss2,step2)
            #     step2 += 1
