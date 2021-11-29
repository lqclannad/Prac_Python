# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/23 19:57
# 文件名称: cat_dog.py
# 开发工具: Pycharm
# E:\data\cat_dog\img
import os

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from data import MNISTDataset
from net import net_v

DEVICE = "cuda"


class Trainer:
    def __init__(self):
        self.summaryWriter = SummaryWriter("logs1")
        # 加载数据
        self.train_dataset = MNISTDataset("E:/data/cat_dog",True)
        self.train_loader = DataLoader(self.train_dataset,batch_size=500,shuffle=True)

        self.test_dataset = MNISTDataset("E:/data/cat_dog",False)
        self.test_loader = DataLoader(self.test_dataset,batch_size=100,shuffle=True)

        # 创建模型
        self.net = net_v().to(DEVICE)
        # 创建优化器
        self.opt = optim.Adam(self.net.parameters())
        # 创建损失函数
        self.loss_func = nn.MSELoss()

    def __call__(self):
        train_step = 0
        test_step = 0
        for epoch in range(10000):
            # 训练代码
            train_sum_loss = 0
            train_sum_acc = 0
            for i,(img,tag) in enumerate(self.train_loader):
                # 将数据加载到GPU上
                img, tag = img.to(DEVICE), tag.to(DEVICE)
                out = self.net(img)
                train_loss = self.loss_func(out,tag)

                self.opt.zero_grad()
                train_loss.backward()
                self.opt.step()

                acc = torch.mean(torch.eq(torch.argmax(out,dim=1),torch.argmax(tag,dim=1)).float())
                # train_sum_acc = train_sum_acc + acc
                # train_sum_loss = train_sum_loss + train_loss
                if i%10==0 and i!=0:
                    print("train_loss-->", train_loss)
                    print("train_acc-->", acc)
                    self.summaryWriter.add_scalar("train_loss", train_loss, train_step)
                    self.summaryWriter.add_scalar("train_acc", acc, train_step)
                    train_step += 1
                # if i%10 == 0 and i != 0:
                #     _loss = train_sum_loss / 10
                #     _acc = train_sum_acc / 10
                #     print("train_loss-->",_loss)
                #     print("train_acc-->",_acc)
                #     self.summaryWriter.add_scalar("train_loss",_loss,train_step)
                #     self.summaryWriter.add_scalar("train_acc",_acc,train_step)
                #     train_sum_loss = 0
                #     train_sum_acc = 0

            # 测试代码
            test_sum_loss = 0
            test_sum_acc = 0
            sum_score = 0
            for i, (img, tag) in enumerate(self.test_loader):
                # 将数据加载到GPU上
                img, tag = img.to(DEVICE), tag.to(DEVICE)
                out = self.net(img)
                print("out:",out)
                test_loss = self.loss_func(out,tag)

                acc = torch.mean(torch.eq(torch.argmax(out,dim=1),torch.argmax(tag,dim=1)).float())
                test_sum_acc = test_sum_acc + acc
                test_sum_loss = test_sum_loss + test_loss
                # 验证精度
                sum_score = torch.mean(torch.eq(torch.argmax(out,dim=1),torch.argmax(tag,dim=1)).float()).item()
                # sum_score = sum_score + torch.mean(torch.eq(torch.argmax(out,dim=1),torch.argmax(tag,dim=1)).float()).item()
                if i % 10 == 0 and i != 0:
                    print("_loss==>", test_loss)
                    print("_acc==>", acc)
                    print("_score==>", sum_score)
                    self.summaryWriter.add_scalar("test_loss", test_loss, test_step)
                    self.summaryWriter.add_scalar("test_acc", acc, test_step)
                    self.summaryWriter.add_scalar("test_score", sum_score, test_step)
                    test_step += 1
                # if i%10==0 and i!=0:
                #     _loss = test_sum_loss / 10
                #     _acc = test_sum_acc / 10
                #     _score = sum_score / 10
                #     print("_loss==>",_loss)
                #     print("_acc==>",_acc)
                #     print("_score==>",_score)
                #     self.summaryWriter.add_scalar("test_loss",_loss,test_step)
                #     self.summaryWriter.add_scalar("test_acc",_acc,test_step)
                #     self.summaryWriter.add_scalar("test_score",_score,test_step)
                #     test_sum_loss = 0
                #     test_sum_acc = 0
                #     sum_score = 0


if __name__ == '__main__':
    trainer = Trainer()
    trainer()

