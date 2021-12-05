# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/05 23:10
# 文件名称: test.py
# 开发工具: Pycharm
import os
import time

import numpy as np
import torch
from PIL import Image
from PIL.ImageDraw import Draw
from torch import optim, nn
from torch.utils.data import DataLoader
from net import Net
from data import MyDataset


test_dataset = MyDataset("E:/data/xiaohuangren/data", False)
test_loader = DataLoader(test_dataset,batch_size=100,shuffle=True)

DEVICE = "cuda"

if __name__ == '__main__':
    net = Net().to(DEVICE)
    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()

    for epoch in range(1000):
        if os.path.exists("param/max_iou.pt"):
            print("========加载预训练参数========")
            net.load_state_dict(torch.load("param/max_iou_0.3521.pt"))
        print(f"==========< epoch {epoch} >==========")
        for i, (img, tag) in enumerate(test_loader):
            img, tag = img.to(DEVICE), tag.to(DEVICE).float()
            img = img.permute(0,3,1,2)
            out = net(img)
            test_loss = loss_func(out, tag)
            print("test_loss:",test_loss)
            # img = img.permute(0,2,3,1).cpu().numpy()
            # imga = Image.fromarray(img[0],"RGB")
            # imga.show()
            # time.sleep(2)
            img = img.permute(0,2,3,1).cpu()
            img = np.array((img+0.5)*255,dtype=np.uint8)
            tag = tag.detach().cpu().numpy() * 300
            out = out.detach().cpu().numpy() * 300
            for i,j in enumerate(img):
                imga = Image.fromarray(img[i],"RGB")
                draw_img = Draw(imga)
                x1,y1,x2,y2 = tag[i][0],tag[i][1],tag[i][2],tag[i][3]
                a1,b1,a2,b2 = out[i][0],out[i][1],out[i][2],out[i][3]
                draw_img.rectangle(((x1,y1),(x2,y2)),outline='green')
                draw_img.rectangle(((a1,b1),(a2,b2)),outline='red')
                imga.show()
                time.sleep(3)
