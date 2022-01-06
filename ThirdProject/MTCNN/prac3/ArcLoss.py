# Coding:utf-8
# Author:Naturino
import torch
import torch.nn as nn
import torch.nn.functional as F

class Arc(nn.Module):
    def __init__(self,feature_dim=2,cls_dim=10):
        super().__init__()
        self.W=nn.Parameter(torch.randn(feature_dim,cls_dim))
    def forward(self, feature,m=1,s=10):
        x=F.normalize(feature,dim=1)
        w = F.normalize(self.W, dim=0)
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
            nn.Linear(784,512),
            nn.ReLU(),
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,2)
        )
        # self.fc2 = nn.Sequential(
        #     nn.Linear(2,10),
        #     nn.Softmax(dim=1)
        # )
    def forward(self,x):
        # fc1_out = self.fc1(x)
        # out = self.fc2(fc1_out)
        # return fc1_out,out
        return self.fc1(x)


if __name__ == '__main__':

    net=Net()
    arc=Arc()

    data=torch.Tensor(1,784)

    out1=net(data)
    print(out1.shape)

    out2=arc(out1)
    print(out2.shape)


