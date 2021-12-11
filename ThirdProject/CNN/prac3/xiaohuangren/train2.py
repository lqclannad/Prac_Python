# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/06 19:46
# 文件名称: train2.py
# 开发工具: Pycharm
import os
import time

import torch
from torch import optim, nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from ThirdProject.CNN.prac3.xiaohuangren.util.iou import iou
from data2 import MyDataset
from net2 import Net_v2


train_dataset = MyDataset("E:/data/xiaohuangren/data", True)
test_dataset = MyDataset("E:/data/xiaohuangren/data", False)
train_loader = DataLoader(train_dataset,batch_size=50,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=10,shuffle=True)

DEVICE = "cuda"

summarywriter = SummaryWriter("logs1")

if __name__ == '__main__':
    net = Net_v2().to(DEVICE)
    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    min_loss = 0.026255859062075615
    step=0

    for epoch in range(1000):
        start = time.time()
        if os.path.exists("param/classification.pt"):
            print("========加载预训练参数========")
            net.load_state_dict(torch.load("param/classification.pt"))
        print(f"==========< epoch {epoch} >==========")
        train_sum_loss = 0
        for i,(img, tag, tag2) in enumerate(train_loader):
            img, tag, tag2 = img.to(DEVICE), tag.to(DEVICE).float(), tag2
            img = img.permute(0,3,1,2)
            out = net(img)
            train_loss = loss_func(out, tag)
            opt.zero_grad()
            train_loss.backward()
            opt.step()
            print(train_loss)
            train_sum_loss = train_sum_loss + train_loss
        train_avg_loss = train_sum_loss / len(train_loader)
        print("train_sum_loss:",train_sum_loss)
        print("len(train_loader):",len(train_loader))
        print("train_avg_loss:",train_avg_loss)
        if train_avg_loss < min_loss:   # 0.026255859062075615
            min_loss = train_avg_loss
            torch.save(net.state_dict(), "param/classification.pt")
            print(f"覆盖新的参数模型{min_loss}")
        summarywriter.add_scalar("train_avg_loss",train_avg_loss,step)
        step+=1
        end = time.time()
        print(f"轮次{epoch}花时{(end-start)/60}分钟")

