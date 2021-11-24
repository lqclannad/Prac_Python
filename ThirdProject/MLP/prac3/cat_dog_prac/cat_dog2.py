# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/24 13:07
# 平台: PyCharm
# 文件名: cat_dog2.py
from torch.utils.data import Dataset,DataLoader
from torch import nn
import torch
from torch.utils.tensorboard import SummaryWriter
from data2 import MyDataset
from net2 import net2


DEVICE = "cuda"

dataset = MyDataset("E:\data\cat_dog\img")
data_loader = DataLoader(dataset,batch_size=512,shuffle=True)
summaryWriter = SummaryWriter("logs")

if __name__ == '__main__':
    net = net2().to(DEVICE)
    opt = torch.optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    step=0
    for epoch in range(10000):
        for i,(img,tag) in enumerate(data_loader):
            img,tag = img.to(DEVICE), tag.to(DEVICE)
            img = img.reshape(-1,3*100*100).float()
            out = net(img)
            loss = loss_func(out,tag)

            opt.zero_grad()
            loss.backward()
            opt.step()

            if i%10==0 and i!=0:
                print(loss)
                summaryWriter.add_scalar("loss",loss,step)
                step+=1
