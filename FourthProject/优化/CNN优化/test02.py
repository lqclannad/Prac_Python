# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/06 10:23
# 文件名称: test02.py
# 开发工具: Pycharm
import torch.optim
from torch import nn


def weight_init(m):
    if(isinstance(m,nn.Conv2d)):
        nn.init.kaiming_normal_(m.weight)
        if m.bias is not None:
            nn.init.zeros_(m.bias)
    elif(isinstance(m,nn.Linear)):
        nn.init.kaiming_uniform_(m.weight)
        if m.bias is not None:
            nn.init.zeros_(m.bias)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(10,10),
            nn.Dropout(0.3),
            nn.ReLU(),
            nn.Linear(10,256),
            nn.ReLU(),
            nn.Linear(256,10)
        )
        # 将模型加载进这个函数里面去
        self.apply(weight_init)
    def forward(self,x):
        return self.layer(x)

net = Net()
print(net)
print(net.layer[0].weight)

torch.optim.Adam(net.parameters(),weight_decay=0.3)

net.eval()
