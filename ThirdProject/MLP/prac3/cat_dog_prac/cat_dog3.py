# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/24 17:54
# 平台: PyCharm
# 文件名: cat_dog3.py
from torch.nn.functional import one_hot
from torch.utils.data import DataLoader
from torch import nn
import torch
from torch.utils.tensorboard import SummaryWriter
from data2 import MyDataset
from net3 import net3

DEVICE = "cuda"

train_dataset = MyDataset("E:\data\cat_dog",True)
train_loader = DataLoader(train_dataset,batch_size=500,shuffle=True)

test_dataset = MyDataset("E:\data\cat_dog",False)
test_loader = DataLoader(test_dataset,batch_size=100,shuffle=True)

summaryWriter = SummaryWriter("logs3")

if __name__ == '__main__':
    net = net3().to(DEVICE)
    opt = torch.optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    test_step = 0
    for epoch in range(10000):
        for i,(img,tag) in enumerate(train_loader):
            img,tag = img.to(DEVICE), tag.to(DEVICE)
            img = img.reshape(-1,3,100,100).float()
            out = net(img)
            train_loss = loss_func(out,tag)

            opt.zero_grad()
            train_loss.backward()
            opt.step()

            if i%10==0 and i!=0:
                print("train_loss:",train_loss)
                # summaryWriter.add_scalar("train_loss",train_loss,step)

        test_sum_loss = 0
        test_sum_score = 0
        for i,(img,tag) in enumerate(test_loader):
            img,tag = img.to(DEVICE), tag.to(DEVICE)
            img = img.reshape(-1, 3, 100, 100).float()
            out = net(img)
            out = torch.gt(out, 0.5)
            test_loss = loss_func(out, tag)
            test_score = torch.sum(torch.eq(out,tag).float())

            test_sum_loss = test_sum_loss + test_loss
            test_sum_score = test_sum_score + test_score
        test_avg_loss = test_sum_loss / len(test_loader)
        test_avg_score = test_sum_score / len(test_dataset)
        print("test_step:",test_step)
        print("test_avg_loss:",test_avg_loss)
        print("test_avg_score:",test_avg_score)
        summaryWriter.add_scalar("test_avg_loss", test_avg_loss, test_step)
        summaryWriter.add_scalar("test_avg_score", test_avg_score, test_step)
        test_step += 1

