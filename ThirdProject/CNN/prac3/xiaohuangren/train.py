# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/04 0:54
# 文件名称: train.py
# 开发工具: Pycharm
import os
import time

import torch
from torch import optim, nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from ThirdProject.CNN.prac3.xiaohuangren.util.iou import iou
from data import MyDataset
from net import Net


train_dataset = MyDataset("E:/data/xiaohuangren/data", True)
test_dataset = MyDataset("E:/data/xiaohuangren/data", False)
train_loader = DataLoader(train_dataset,batch_size=100,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=50,shuffle=True)

DEVICE = "cuda"

summarywriter = SummaryWriter("logs1")

if __name__ == '__main__':
    net = Net().to(DEVICE)
    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    max_iou = 0.3521

    for epoch in range(1000):
        start = time.time()
        if os.path.exists("param/max_iou.pt"):
            print("========加载预训练参数========")
            net.load_state_dict(torch.load("param/max_iou.pt"))
        print(f"==========< epoch {epoch} >==========")
        avg_iou = 0
        sum_iou = 0
        x = 0
        train_step = 0
        train_sum_loss = 0
        test_sum_loss = 0
        test_step = 0
        for i,(img, tag) in enumerate(train_loader):
            img, tag = img.to(DEVICE), tag.to(DEVICE).float()
            img = img.reshape(-1,3,300,300)
            out = net(img)
            train_loss = loss_func(out, tag)
            opt.zero_grad()
            train_loss.backward()
            opt.step()
            train_sum_loss = train_sum_loss + train_loss
            if i%10 == 0 and i!=0:
                train_avg_loss = train_sum_loss / 10
                print("train_avg_loss:",train_avg_loss)
                train_step += 1
                summarywriter.add_scalar("train_avg_loss",train_avg_loss,train_step)
        for i, (img, tag) in enumerate(test_loader):
            img, tag = img.to(DEVICE), tag.to(DEVICE).float()
            img = img.reshape(-1, 3, 300, 300)
            out = net(img)
            test_loss = loss_func(out, tag)
            test_sum_loss = test_sum_loss + test_loss
            if i%10==0 and i!=0:
                test_avg_loss = test_sum_loss / 10
                print(i, ":test_avg_loss:", test_avg_loss)
                test_step += 1
                summarywriter.add_scalar("test_avg_loss",test_avg_loss,test_step)
            tag2 = out.detach()
            for i in range(len(tag)):
                if tag2[i][0]>0.5 and tag[i][0] == 1:
                    x += 1
                    arr1 = tag[i][1:].cpu()
                    arr2 = tag2[i][1:].cpu()
                    sum_iou = sum_iou + iou(arr1, arr2)
            print(f"iou1:{sum_iou},x:{x}")
        avg_iou = sum_iou / x
        if avg_iou > max_iou:   # 0.3521
            max_iou = avg_iou
            print("max_iou:", max_iou)
            torch.save(net.state_dict(), f"param/max_iou.pt")
            with open('param/max_iou.txt', 'a') as f:
                f.write(f"最大iou:{max_iou} 时间戳:{time.time()}\n")
        end = time.time()
        print(f"轮次{epoch}花时{(end-start)/60}分钟")

