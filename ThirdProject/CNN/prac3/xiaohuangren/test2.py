# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/06 21:52
# 文件名称: test2.py
# 开发工具: Pycharm
import os
import time

import numpy as np
import torch
from PIL import Image
from torch import optim, nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from data2 import MyDataset
from net2 import Net_v2


train_dataset = MyDataset("E:/data/xiaohuangren/data", True)
test_dataset = MyDataset("E:/data/xiaohuangren/data", False)
train_loader = DataLoader(train_dataset,batch_size=50,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=10,shuffle=True)

DEVICE = "cuda"

# summarywriter = SummaryWriter("logs1")

if __name__ == '__main__':
    net = Net_v2().to(DEVICE)
    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    loss_func2 = nn.MSELoss()
    min_loss = 1
    step=0

    for epoch in range(1000):
        start = time.time()
        if os.path.exists("param/classification.pt"):
            print("========加载预训练参数========")
            net.load_state_dict(torch.load("param/classification.pt"))
        print(f"==========< epoch {epoch} >==========")
        test_sum_loss = 0
        for i,(img, tag, tag2) in enumerate(test_loader):
            img, tag, tag2 = img.to(DEVICE), tag.to(DEVICE).float(), tag2
            img = img.permute(0,3,1,2)
            out = net(img)
            test_loss = loss_func(out, tag)
            print(test_loss)
            test_sum_loss = test_sum_loss + test_loss
            img = img.permute(0,2,3,1).cpu()
            out = out.detach().cpu().numpy()
            tag = tag.detach().cpu().numpy()
            print("out:",out)
            print("tag:",tag)
            imga = np.array((img[0]+0.5)*255,dtype=np.uint8)
            imga = Image.fromarray(imga,"RGB")
            imga.show()
            time.sleep(5)
        end = time.time()
        print(f"轮次{epoch}花时{(end-start)/60}分钟")

