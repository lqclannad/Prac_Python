# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/06 23:57
# 文件名称: train3.py
# 开发工具: Pycharm
import os
import time

import torch
from torch import optim, nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from ThirdProject.CNN.prac3.xiaohuangren.util.iou import iou
from data2 import MyDataset
from net3 import Net_v3


train_dataset = MyDataset("E:/data/xiaohuangren/data", True)
test_dataset = MyDataset("E:/data/xiaohuangren/data", False)
train_loader = DataLoader(train_dataset,batch_size=50,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=10,shuffle=True)

DEVICE = "cuda"

summarywriter = SummaryWriter("logs1")

if __name__ == '__main__':
    net = Net_v3().to(DEVICE)
    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    min_loss = 0.00015074263501446694
    step = 0

    for epoch in range(1000):
        start = time.time()
        if os.path.exists("param/regression3.pt"):
            print("========加载预训练参数========")
            net.load_state_dict(torch.load("param/regression3.pt"))
        print(f"==========< epoch {epoch} >==========")
        train_sum_loss = 0
        for i,(img, tag, tag2) in enumerate(train_loader):
            img, tag, tag2 = img.to(DEVICE), tag, tag2.to(DEVICE)
            img = img.permute(0,3,1,2)
            out = net(img)
            train_loss = loss_func(out, tag2)
            opt.zero_grad()
            train_loss.backward()
            opt.step()
            print(train_loss)
            # print("tag2:",tag2[:5])
            # print("out:",out[:5])
            # iou1 = []
            # for i in range(50):
            #     iou1.append(iou(out[i].detach().cpu(),tag2[i].detach().cpu()))
            # print("iou:",iou1)
            train_sum_loss = train_sum_loss + train_loss
        train_avg_loss = train_sum_loss / len(train_loader)
        print("train_avg_loss:",train_avg_loss)
        if train_avg_loss < min_loss:   # 1 0.0026233247481286526   3 0.00015074263501446694
            min_loss = train_avg_loss
            torch.save(net.state_dict(), "param/regression3.pt")
            print(f"覆盖新的参数模型{min_loss}")
        summarywriter.add_scalar("train_avg_loss",train_avg_loss,step)
        step+=1
        end = time.time()
        print(f"轮次{epoch}花时{(end-start)/60}分钟")

