# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/22 22:36
# 文件名称: train.py
# 开发工具: Pycharm
import torch
from torch import optim, nn
from torch.utils.data import Dataset, DataLoader
from torch.utils.tensorboard import SummaryWriter

from net import net_v1, net_v2, net_v3, net_v4, net_v5
from data import MNISTDataset

DEVICE = "cuda"


class Trainer:
    def __init__(self, root):
        self.summaryWriter = SummaryWriter("logs")
        # 加载训练数据
        self.train_dataset = MNISTDataset(root, True)
        self.train_loader = DataLoader(self.train_dataset, batch_size=512, shuffle=True)

        # 加载测试数据
        self.test_dataset = MNISTDataset(root, is_train=False)
        self.test_loader = DataLoader(self.test_dataset, batch_size=512, shuffle=True)

        # 创建模型
        self.net = net_v1()

        # 加载预训练参数
        # self.net.load_state_dict(torch.load("param/10.pt"))

        # 将模型加载到GPU上
        self.net.to(DEVICE)
        # 创建优化器
        self.opt = optim.Adam(self.net.parameters())
        # 损失函数(均方差)
        self.loss_func = nn.MSELoss()

    def __call__(self):
        test_step = 0
        train_step = 0
        for epoch in range(10000):
            train_sum_loss = 0
            # 训练代码
            for i, (imgs, tags) in enumerate(self.train_loader):
                # 将数据加载到GPU上
                imgs, tags = imgs.to(DEVICE), tags.to(DEVICE)
                y = self.net.forward(imgs)
                train_loss = self.loss_func(y, tags)

                self.opt.zero_grad()
                train_loss.backward()
                self.opt.step()
                train_sum_loss = train_sum_loss + train_loss.cpu().item()
            avg_train_loss = train_sum_loss / len(self.train_loader)
            print("train_loss==>", avg_train_loss)
            # 收集训练损失
            # self.summaryWriter.add_scalar("train_loss_v5", avg_train_loss, train_step)
            train_step += 1

            # 测试代码
            test_sum_loss = 0
            sum_score = 0
            for i, (imgs, tags) in enumerate(self.test_loader):
                # 将数据加载到GPU上
                imgs, tags = imgs.to(DEVICE), tags.to(DEVICE)
                y = self.net.forward(imgs)
                test_loss = self.loss_func(y, tags)

                # 测试不用反向传播，所以不加更新梯度操作
                test_sum_loss = test_sum_loss + test_loss.cpu().item()
                # 验证精度
                sum_score = sum_score + torch.sum(torch.eq(y, tags).float())
            avg_test_loss = test_sum_loss / len(self.test_loader)
            score = sum_score / len(self.test_dataset)
            print("test_loss==>", avg_test_loss)
            print("score==>", score)
            # 收集测试损失
            # self.summaryWriter.add_scalar("test_loss_v5", avg_test_loss, test_step)
            # self.summaryWriter.add_scalar("score_v5", score, test_step)
            self.summaryWriter.add_scalars("test_v4",{"train_loss_v4":avg_train_loss,"test_loss_v4":avg_test_loss,"score_v4":score},test_step)

            test_step += 1

            # 保存模型的权重
            torch.save(self.net.state_dict(),f"param/{epoch}.pt")


if __name__ == '__main__':
    trainer = Trainer("E:\data\MNIST_IMG")
    trainer()
