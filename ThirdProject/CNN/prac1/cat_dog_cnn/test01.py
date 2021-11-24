# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/24 17:20
# 平台: PyCharm
# 文件名: test01.py
import torch
from torch.nn.functional import one_hot
from torch.utils.data import DataLoader
from torchvision import datasets
from torch import nn
from torchvision.transforms import transforms
from torch.utils.tensorboard import SummaryWriter


dataset = datasets.CIFAR10("E:/data/CIFAR10_data", train=True, transform=transforms.ToTensor(), download=True)
train_loader = DataLoader(dataset, batch_size=512, shuffle=True, num_workers=1)

DEVICE = "cuda"
summaryWriter = SummaryWriter("logs")

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Conv2d(3, 24, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(24, 52, (3, 3)),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(52, 128, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(128, 256, (3, 3)),
            nn.ReLU()
        )

        self.out_layer = nn.Sequential(
            nn.Linear(256 * 2 * 2, 10),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        out = self.fc_layer(x)
        out = out.reshape(-1,256*2*2)
        return self.out_layer(out)


if __name__ == '__main__':
    net = Net().to(DEVICE)
    opt = torch.optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    step = 0
    for epoch in range(10000):
        for i,(img,tag) in enumerate(train_loader):
            img, tag = img.to(DEVICE), tag.to(DEVICE)
            tag = one_hot(tag,10).float()
            out = net(img)
            loss = loss_func(out,tag)

            opt.zero_grad()
            loss.backward()
            opt.step()

            if i%10==0 and i!=0:
                summaryWriter.add_scalar("loss",loss,step)
                print(loss)
                step += 1
