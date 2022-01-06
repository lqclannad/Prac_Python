# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/17 16:52
# 文件名称: test01.py
# 开发工具: Pycharm
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import torch
import torch.nn as nn
import torch.utils.data as data
import torch.nn.functional as F
import torchvision
from matplotlib import pyplot as plt
from torchvision import transforms

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
train_data = torchvision.datasets.MNIST(root="E:\data\MNIST_data",download=False,train=True,transform=transforms.ToTensor())
# train_data = torchvision.datasets.CIFAR10(root="D:\data\CIFAR10_data",download=False,train=True,transform=transforms.ToTensor())
train_loader = data.DataLoader(dataset=train_data,shuffle=True,batch_size=512)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Sequential(
            nn.Linear(784,512),
            nn.ReLU(),
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,2)
        )
        self.fc2 = nn.Sequential(
            nn.Linear(2,10),
            nn.Softmax(dim=1)
        )
    def forward(self,x):
        fc1_out = self.fc1(x)
        out = self.fc2(fc1_out)
        return fc1_out,out


#特征可视化
def visualize(feat,labels,epoch):
    plt.ion()
    c = ["#ff0000","#ffff00","#00ff00","#00ffff","#0000ff",
         "#ff00ff","#990000","#999900","#009900","#009999"]
    plt.clf()
    for i in range(10):
        plt.plot(feat[labels == i,0],feat[labels==i,1],".",c=c[i])
    plt.legend(["0","1","2","3","4","5","6","7","8","9"],loc="upper right")
    plt.title("epoch=%d"%epoch)
    plt.savefig("images/epoch=%d.jpg"%epoch)
    plt.draw()
    plt.pause(0.001)


if __name__ == '__main__':
    net = Net().to(device)
    loss_func = nn.MSELoss()
    # loss_func = nn.CrossEntropyLoss()
    # opt = torch.optim.SGD(net.parameters(),lr=0.01,momentum=0.5)
    opt = torch.optim.Adam(net.parameters())

    epoch = 0
    min_loss = 1
    while True:
        feat_loader = []
        label_laoder = []
        sum_loss = 0
        for i, (x, y) in enumerate(train_loader):
            x = x.reshape(-1, 784).to(device)
            target = F.one_hot(y, 10).to(device).float()
            # target = y.to(device)

            feat, out_put = net(x)
            loss = loss_func(out_put, target)
            sum_loss = sum_loss + loss.item()

            opt.zero_grad()
            loss.backward()
            opt.step()

            feat_loader.append(feat)
            label_laoder.append(y)

            if i % 10 == 0:
                print(loss.item())
        feat = torch.cat(feat_loader, 0)
        labels = torch.cat(label_laoder, 0)
        visualize(feat.detach().cpu().numpy(), labels.detach().cpu().numpy(), epoch)
        avg_loss = sum_loss / len(train_loader)
        if avg_loss < min_loss:
            min_loss = avg_loss
            print(f"保存最小损失{min_loss}")
            torch.save(net.state_dict(), "param/net.pt")
        epoch += 1
