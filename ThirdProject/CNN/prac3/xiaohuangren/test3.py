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
from PIL.ImageDraw import Draw
from torch import optim, nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from ThirdProject.CNN.prac4.test1.net2 import Net_v2
from ThirdProject.CNN.prac3.xiaohuangren.util.iou import iou
from data2 import MyDataset
from net3 import Net_v3


train_dataset = MyDataset("E:/data/xiaohuangren/data", True)
test_dataset = MyDataset("E:/data/xiaohuangren/data", False)
train_loader = DataLoader(train_dataset,batch_size=50,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=10,shuffle=True)

DEVICE = "cuda"

summarywriter = SummaryWriter("logs3")

if __name__ == '__main__':
    net = Net_v2().to(DEVICE)
    net2 = Net_v3().to(DEVICE)
    opt = optim.Adam(net.parameters())
    opt2 = optim.Adam(net2.parameters())
    loss_func = nn.MSELoss()
    loss_func2 = nn.MSELoss()
    step = 0

    for epoch in range(1000):
        start = time.time()
        if os.path.exists("param/classification3.pt"):
            print("========加载分类预训练参数========")
            net.load_state_dict(torch.load("param/classification3.pt"))
        if os.path.exists("param/regression3.pt"):
            print("========加载回归预训练参数========")
            net2.load_state_dict(torch.load("param/regression3.pt"))
        print(f"==========< epoch {epoch} >==========")
        test_sum_loss = 0
        iou1 = 0
        x = 0
        for i, (img, tag, tag2) in enumerate(test_loader):
            img, tag, tag2 = img.to(DEVICE), tag.to(DEVICE).float(), tag2.to(DEVICE)
            img = img.permute(0, 3, 1, 2)
            out = net(img)
            out2 = net2(img)
            test_loss = loss_func(out, tag)
            test_loss2 = loss_func2(out2, tag2)
            out = out.detach().cpu().numpy()
            for i in range(10):
                if out[i] > 0.5 and tag[i] > 0.5:
                    iou1 = iou1 + iou(out2[i].detach().cpu(),tag2[i].detach().cpu())
                    x += 1
        if x > 0:
            avg_iou = iou1 / x
            print(f"{epoch},avg_iou:{avg_iou}")
            summarywriter.add_scalar("avg_iou", avg_iou, step)
            step += 1
            if out[0] > 0.5:
                print("out1:", out[0])
                print("tag1:", tag[0])
                out2 = out2.detach().cpu().numpy() * 300
                tag2 = tag2.detach().cpu().numpy() * 300
                print("out2:",out2)
                print("tag2:",tag2)
                print("iou=", iou(out2[0], tag2[0]))
                test_sum_loss = test_sum_loss + test_loss2

                img = img.permute(0, 2, 3, 1).cpu()

                imga = np.array((img[0] + 0.5) * 255, dtype=np.uint8)
                imga = Image.fromarray(imga, "RGB")
                draw = Draw(imga)
                draw.rectangle(tag2[0],outline="green",width=1)
                draw.rectangle(out2[0],outline="red",width=2)
                imga.show()
                time.sleep(3)
        end = time.time()
        print(f"轮次{epoch}花时{(end - start) / 60}分钟")
