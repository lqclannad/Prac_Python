# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/22 15:09
# 文件名称: test01.py
# 开发工具: Pycharm
import os

from mpl_toolkits.mplot3d import Axes3D
import numpy as np

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import torch.nn as nn
import torch
import torch.utils.data as data
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt
from torch.nn.functional import one_hot, normalize
import torch.nn.functional as F

class CenterLoss(nn.Module):
    def __init__(self,cls_num,feature_num):
        super(CenterLoss, self).__init__()
        self.cls_num = cls_num
        self.center = nn.Parameter(torch.randn(cls_num, feature_num))

    def forward(self, xs, ys):
        # normalize - 范数归一化
        xs = normalize(xs)
        center_exp = self.center.index_select(dim=0, index=ys.long())
        count = torch.histc(ys, bins=self.cls_num, min=0, max=self.cls_num-1)
        count_exp = count.index_select(dim=0, index=ys.long())
        return torch.sum(torch.div(torch.sum(torch.pow(xs-center_exp, 2), dim=1), count_exp))

class Arc(nn.Module):
    def __init__(self,feature_dim=3,cls_dim=10):
        super().__init__()
        self.W=nn.Parameter(torch.randn(feature_dim,cls_dim))
    def forward(self, feature,m=1,s=10):
        x = F.normalize(feature, dim=1).cuda()
        w = F.normalize(self.W, dim=0).cuda()
        cos = torch.matmul(x, w)/10
        a=torch.acos(cos)
        top=torch.exp(s*torch.cos(a+m))
        down2=torch.sum(torch.exp(s*torch.cos(a)),dim=1,keepdim=True)-torch.exp(s*torch.cos(a))
        out=torch.log(top/(top+down2))
        return out

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Sequential(
            # nn.Linear(784,512),
            nn.Conv2d(1,16,3,stride=1,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            # nn.Linear(512,256),
            nn.Conv2d(16,32,3,stride=1,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            # nn.Linear(256,128),
            nn.Conv2d(32,64,3,stride=1),
            nn.ReLU(),
            nn.Conv2d(64,128,3,stride=1),
            nn.ReLU(),
            nn.Conv2d(128,256,3,stride=1),
            nn.ReLU(),
            nn.Conv2d(256,256,3,stride=1,padding=1),
            nn.ReLU(),
            nn.Conv2d(256,256,3,stride=1,padding=1),
            nn.ReLU()
            # nn.Linear(256,2)
            # nn.Linear(128,2)
        )
        self.fc2 = nn.Sequential(
            nn.Linear(256,3)
        )
        self.fc3 = nn.Sequential(
            nn.Linear(3,10)
        )
        self.center_loss_layer = CenterLoss(10,3)
        self.celoss = nn.CrossEntropyLoss()

    def forward(self,x):
        fc_out1 = self.fc1(x).reshape(-1,256)
        fc_out = self.fc2(fc_out1)
        out = self.fc3(fc_out)
        return fc_out,out

    def get_loss(self, outputs, features, labels):
        loss_cls = self.celoss(outputs, labels)
        loss_center = self.center_loss_layer(features,labels)
        loss = loss_cls + loss_center
        return loss

    # def get_loss2(self):


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
train_data = torchvision.datasets.MNIST(root="E:\data\MNIST_data",download=False,train=True,transform=transforms.ToTensor())
# train_data = torchvision.datasets.CIFAR10(root="D:\data\CIFAR10_data",download=False,train=True,transform=transforms.ToTensor())
train_loader = data.DataLoader(dataset=train_data,shuffle=True,batch_size=512)


fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
#特征可视化
def visualize(feat,labels,epoch):
    c = ["#ff0000","#ffff00","#00ff00","#00ffff","#0000ff",
         "#ff00ff","#990000","#999900","#009900","#009999"]
    for i in range(10):
        print(feat[:5])
        ax.plot(feat[labels == i,0],feat[labels==i,1],feat[labels == i,2],".",c=c[i])
        # plt.plot(feat[labels == i,0],feat[labels==i,1],".",c=c[i])
    ax.legend(["0","1","2","3","4","5","6","7","8","9"],loc="upper right")
    ax.set_title("epoch=%d"%epoch)
    plt.savefig("images/epoch=%d.jpg"%epoch)
    # plt.show()
    # plt.pause(0.001)

if __name__ == '__main__':
    net = Net().to(device)
    # loss_func = nn.MSELoss()
    # loss_func = nn.CrossEntropyLoss()
    # opt = torch.optim.SGD(net.parameters(),lr=0.01,momentum=0.5)
    opt = torch.optim.Adam(net.parameters())

    epoch = 0
    min_loss = 10000
    while True:
        feat_loader = []
        label_laoder = []
        sum_loss = 0
        if os.path.exists("param/net.pt"):
            print("加载模型权重...")
            net.load_state_dict(torch.load("param/net.pt"))
        for i,(x,y) in enumerate(train_loader):
            # x = x.reshape(-1,784).to(device)
            x = x.to(device)
            # target = one_hot(y,10).to(device).float()
            target = y.to(device)

            feat,out_put = net(x)
            loss = net.get_loss(out_put,feat,target)
            sum_loss = sum_loss + loss.item()

            opt.zero_grad()
            loss.backward()
            opt.step()

            feat_loader.append(feat)
            label_laoder.append(y)

            if i%10 ==0:
                print(loss.item())
        loss = sum_loss / len(train_loader)
        # if loss < min_loss:
        #     min_loss = loss
        #     print(f"轮次{epoch}保存模型,此权重轮损失为{min_loss}")
        #     torch.save(net.state_dict(), "param/net.pt")
        #     with open("param/min_loss.txt", "a") as f:
        #         f.write(f"epoch{epoch} saved model weights,and it's min_loss is {min_loss}\n")
        feat = torch.cat(feat_loader,0)
        labels = torch.cat(label_laoder,0)
        if epoch % 10 == 0:
            visualize(feat.detach().cpu().numpy(), labels.detach().cpu().numpy(), epoch)
        # visualize(feat.detach().cpu().numpy(), labels.detach().cpu().numpy(), epoch)
        epoch+=1
