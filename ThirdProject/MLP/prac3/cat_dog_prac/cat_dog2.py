# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/24 13:07
# 平台: PyCharm
# 文件名: cat_dog2.py
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
from torch import nn
import torch
from torch.utils.tensorboard import SummaryWriter
from data2 import MyDataset
from net2 import net2

DEVICE = "cuda"


class Trainer():
    def __init__(self):
        self.train_dataset = MyDataset("E:\data\cat_dog", True)
        self.train_loader = DataLoader(self.train_dataset, batch_size=500, shuffle=True)
        self.test_dataset = MyDataset("E:\data\cat_dog", False)
        self.test_loader = DataLoader(self.test_dataset, batch_size=100, shuffle=True)

        self.net = net2().to(DEVICE)
        self.opt = torch.optim.Adam(self.net.parameters())
        self.loss_func = nn.MSELoss()

    def __call__(self, *args, **kwargs):
        summaryWriter = SummaryWriter("logs11")
        test_step = 0
        for epoch in range(10000):
            train_sum_loss = 0
            for i, (img, tag) in enumerate(self.train_loader):
                img, tag = img.to(DEVICE), tag.to(DEVICE)
                img = img.reshape(-1, 3 * 100 * 100)
                # img = img.requires_grad_()
                # img = Variable(img,requires_grad=True)
                out = self.net(img)
                out = torch.gt(out, 0.5).float()
                out.requires_grad_()
                train_loss = self.loss_func(out,tag)

                self.opt.zero_grad()
                train_loss.backward()
                self.opt.step()
                print("train_loss:",train_loss)

            #     train_sum_loss = train_sum_loss + train_loss
            # train_avg_loss = train_sum_loss / len(self.train_loader)
            # print(f'''
            # =========================================
            # train_avg_loss:{train_avg_loss}
            # =========================================
            # ''')

            test_sum_loss = 0
            sum_score = 0
            for i,(img,tag) in enumerate(self.test_loader):
                img, tag = img.to(DEVICE), tag.to(DEVICE)
                img = img.reshape(-1, 3*100*100)
                out = self.net(img)
                out = torch.gt(out, 0.5)
                test_loss = self.loss_func(out,tag)

                # 测试集不进行反向传播！！
                print("test_loss:",test_loss)
                test_sum_loss = test_sum_loss + test_loss
                print("test_sum_loss:",test_sum_loss)
                score = torch.sum(torch.eq(out,tag).float())
                print("score:",score)
                sum_score = sum_score + score
                print("sum_score:", sum_score)
            test_avg_loss = test_sum_loss / len(self.test_loader)
            test_avg_score = sum_score / len(self.test_dataset)
            summaryWriter.add_scalar("test_avg_loss",test_avg_loss,test_step)
            summaryWriter.add_scalar("test_avg_score",test_avg_score,test_step)
            print(f'''
            =========================================
            test_avg_loss:{test_avg_loss}
            =========================================
            test_avg_score:{test_avg_score}
            =========================================
            ''')
            test_step += 1



if __name__ == '__main__':
    trainer = Trainer()
    trainer()
