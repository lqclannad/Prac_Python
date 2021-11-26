# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/11/22 21:09
# 文件名称: train.py
# 开发工具: Pycharm

from torch import optim, nn
from torch.utils.tensorboard import SummaryWriter

from data2 import MNISTDataset, DataLoader
from net import net_v1, net_v2, net_v3

DEVICE = "cuda"
summaryWriter = SummaryWriter("conv2d_relu")


class Trainer:
    def __init__(self, root):
        # 加载训练数据
        self.train_dataset = MNISTDataset(root, True)
        self.train_loader = DataLoader(self.train_dataset, batch_size=12, shuffle=True)
        # 创建模型
        self.net = net_v3()
        # 将模型加载到GPU上
        self.net.to(DEVICE)
        # 创建优化器
        self.opt = optim.Adam(self.net.parameters())
        # 损失函数
        self.loss_func = nn.MSELoss()

    # 训练代码
    def __call__(self):
        step = 0
        for epoch in range(10000):
            sum_loss = 0
            for i, (imgs, tags) in enumerate(self.train_loader):
                # 将数据加载到GPU上
                imgs, tags = imgs.to(DEVICE), tags.to(DEVICE)

                y = self.net.forward(imgs)
                loss = self.loss_func(y, tags)

                self.opt.zero_grad()
                loss.backward()
                self.opt.step()
                sum_loss = sum_loss + loss
                if i % 10 == 0 and i != 0:
                    avg_loss = sum_loss / 10
                    print(sum_loss)
                    summaryWriter.add_scalar("avg_loss", avg_loss, step)
                    sum_loss = 0
                    step += 1


if __name__ == '__main__':
    trainer = Trainer("E:\data\MNIST_IMG")
    trainer()
