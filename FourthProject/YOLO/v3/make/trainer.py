# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/13 14:19
# 文件名称: trainer.py
# 开发工具: Pycharm
from torch import nn
from torch.utils.tensorboard import SummaryWriter

import dataset
from module import *
import torch
from tensorboard.summary import Writer


def loss_fn(output, target, alpha):
    output = output.permute(0, 2, 3, 1)#N,45,13,13==>N,13,13,45
    output = output.reshape(output.size(0), output.size(1), output.size(2), 3, -1)#N,13,13,3,15
    # print("output:",output.shape)
    mask_obj = target[..., 0] > 0#N,13,13,3
    # print("mask_obj:",mask_obj.shape)
    # mask_noobj = target[..., 0] == 0
    # print("mask_noobj:",mask_noobj.shape)
    # print("output[mask_obj]:",output[mask_obj].shape)
    # print("output[mask_noobj]:", output[mask_noobj].shape)
    #置信度损失：需要的是正负样本的置信度。
    # loss_obj = torch.mean((output[mask_obj] - target[mask_obj]) ** 2)#N,15
    # loss_noobj = torch.mean((output[mask_noobj] - target[mask_noobj]) ** 2)
    # loss = alpha * loss_obj + (1 - alpha) * loss_noobj
    # return loss
    c_loss_func = nn.BCEWithLogitsLoss()
    off_loss_func = nn.MSELoss()
    cls_loss_func = nn.CrossEntropyLoss()
    #置信度损失：
    c_loss = c_loss_func(output[...,0],target[...,0])
    #偏移量损失
    # print(output.shape)
    # print(output[mask_obj].shape)
    # print(output[mask_obj][:,1:5])
    off_loss = off_loss_func(output[mask_obj][:,1:5].float(),target[mask_obj][:,1:5].float())
    #多分类损失
    # print(target[mask_obj][:,5:])
    # print(torch.argmax(target[mask_obj][:,5:],dim=1))
    # print(output.shape) # torch.Size([2, 13, 13, 3, 5])
    # print(target.shape) # torch.Size([2, 13, 13, 3, 9])
    # print(mask_obj.shape)   # torch.Size([2, 13, 13, 3])
    # print(output[mask_obj].shape)   # torch.Size([27, 5])
    # print(target[mask_obj].shape)   # torch.Size([36, 9])
    cls_loss = cls_loss_func(output[mask_obj][:,5:],torch.argmax(target[mask_obj][:,5:],dim=1))
    loss = alpha * c_loss+(1-alpha)*(off_loss+cls_loss)
    return loss


if __name__ == '__main__':
    if not os.path.exists("log2"):
        os.mkdir("log2")
    summaryWriter = SummaryWriter("log2")

    myDataset = dataset.MyDataset()
    train_loader = torch.utils.data.DataLoader(myDataset, batch_size=10, shuffle=True)

    net = Darknet53()
    net.train()

    opt = torch.optim.Adam(net.parameters())

    step = 0
    epoch = 0
    min_loss = 100
    while True:
        sum_loss = 0
        for target_13, target_26, target_52, img_data in train_loader:
            output_13, output_26, output_52 = net(img_data)
            loss_13 = loss_fn(output_13, target_13, 0.7)
            loss_26 = loss_fn(output_26, target_26, 0.7)
            loss_52 = loss_fn(output_52, target_52, 0.7)

            loss = loss_13 + loss_26 + loss_52
            opt.zero_grad()
            loss.backward()
            opt.step()

            print(epoch, loss.item())
            sum_loss = sum_loss + loss.item()
            summaryWriter.add_scalar("loss", loss.item(), step)
            step += 1
        # 保存最后的
        torch.save(net.state_dict(), "weight/lastest_weight.pt")
        epoch += 1

        avg_loss = sum_loss / len(train_loader)
        # 保存最好的
        if avg_loss < min_loss:
            min_loss = avg_loss
            torch.save(net.state_dict(), "weight/best_weight.pt")

