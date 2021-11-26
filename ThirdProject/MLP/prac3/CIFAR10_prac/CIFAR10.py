# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/25 9:40
# 平台: PyCharm
# 文件名: CIFAR10.py
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
            nn.Linear(32*32*3,512),
            nn.ReLU(),
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU(),
            nn.Linear(32,16),
            nn.ReLU(),
            nn.Linear(16,14),
            nn.ReLU(),
            nn.Linear(14,12),
            nn.ReLU(),
            nn.Linear(12,10),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        return self.fc_layer(x)


if __name__ == '__main__':
    summaryWriter = SummaryWriter("logs1")
    print("开始...")
    net = Net().to(DEVICE)
    opt = torch.optim.Adam(net.parameters())
    loss_func = nn.MSELoss()

    step = 0
    test_step = 0
    _step = 0
    for epoch in range(10000):
        sum_loss = 0
        sum_acc = 0
        for i, (img, label) in enumerate(train_loader):
            img, label = img.to(DEVICE), label.to(DEVICE)

            img = img.reshape(-1, 32 * 32 * 3)

            out = net(img)

            label = one_hot(label, 10).float()
            loss = loss_func(out, label)

            opt.zero_grad()
            loss.backward()
            opt.step()

            acc = torch.mean(torch.eq(torch.argmax(out, dim=1), torch.argmax(label, dim=1)).float())
            sum_acc = sum_acc + acc
            sum_loss = sum_loss + loss
            if i % 10 == 0 and i != 0:
                _loss = sum_loss / 10
                _acc = sum_acc / 10
                # summaryWriter.add_scalar("acc",_acc,step)
                # summaryWriter.add_scalar("loss",_loss,step)
                summaryWriter.add_scalars("train", {"acc": _acc, "loss": _loss}, step)
                print("loss:", _loss.item())
                print("acc:", _acc.item())
                sum_loss = 0
                sum_acc = 0
                step += 1

        test_sum_loss = 0
        test_sum_acc = 0
        sum_score = 0
        for i, (img, label) in enumerate(test_loader):
            img, label = img.to(DEVICE), label.to(DEVICE)

            img = img.reshape(-1, 32 * 32 * 3)

            out = net(img)
            label = one_hot(label, 10).float()
            loss = loss_func(out, label)

            # 测试集不用反向传播！！！

            acc = torch.mean(torch.eq(torch.argmax(out, dim=1), torch.argmax(label, dim=1)).float())
            test_sum_acc = test_sum_acc + acc
            test_sum_loss = test_sum_loss + loss
            sum_score = sum_score + torch.sum(torch.eq(torch.argmax(out, dim=1), torch.argmax(label, dim=1)).float())
            if i % 10 == 0 and i != 0:
                _loss = test_sum_loss / 10
                _acc = test_sum_acc / 10
                # summaryWriter.add_scalar("test_acc", _acc, test_step)
                # summaryWriter.add_scalar("test_loss", _loss, test_step)
                # summaryWriter.add_scalar("test_score", _score, test_step)
                summaryWriter.add_scalars("test", {"test_acc": _acc, "test_loss": _loss},
                                          test_step)
                print("acc:", _acc.item())
                print("loss:", _loss.item())
                test_sum_acc = 0
                test_sum_loss = 0
                test_step += 1
        print('''
        ====================================================
        ====================================================
        ====================================================
        ====================================================
        
        ''')
        _score = sum_score.item() / len(test_data)
        summaryWriter.add_scalar("score",_score,_step)
        print("score:", _score)
        sum_score = 0
        _step += 1



