# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/25 9:43
# 平台: PyCharm
# 文件名: CIFAR10_2.py
import torch.optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch import nn
from torch.nn.functional import one_hot
from torch.utils.tensorboard import SummaryWriter

DEVICE = "cuda"

train_data = datasets.CIFAR10("E:\data\CIFAR10_data", train=True, transform=transforms.ToTensor(), download=True)
test_data = datasets.CIFAR10("E:\data\CIFAR10_data", train=False, transform=transforms.ToTensor(), download=True)

train_loader = DataLoader(train_data, batch_size=512, shuffle=True)
test_loader = DataLoader(test_data, batch_size=100, shuffle=True)


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Conv2d(3, 12, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(12, 24, (3, 3)),
            nn.ReLU(),  # 1, 24, 13, 13
            nn.MaxPool2d(2),  # 1, 24, 6, 6
            nn.Conv2d(24, 48, (3, 3)),
            nn.ReLU(),  # 1, 48, 4, 4
            nn.MaxPool2d(2)  # 1, 48, 2, 2
        )
        self.out_layer = nn.Sequential(
            nn.Linear(48 * 2 * 2, 10),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        out = self.fc_layer(x)
        out = out.reshape(-1, 48 * 2 * 2)
        return self.out_layer(out)


if __name__ == '__main__':
    summaryWriter = SummaryWriter("logs1")
    net = Net().to(DEVICE)
    opt = torch.optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    step = 0
    for epoch in range(10000):
        sum_loss = 0
        for i,(img,tag) in enumerate(train_loader):
            img,tag = img.to(DEVICE),tag.to(DEVICE)
            tag = one_hot(tag,10).float()
            out = net(img)
            loss = loss_func(out,tag)

            opt.zero_grad()
            loss.backward()
            opt.step()

            sum_loss = sum_loss + loss

            if i%10==0 and i!=0:
                avg_loss = sum_loss / 10
                print(avg_loss)
                summaryWriter.add_scalar("loss",avg_loss,step)
                step += 1

