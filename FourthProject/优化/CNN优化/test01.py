# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/06 10:19
# 文件名称: test01.py
# 开发工具: Pycharm
from torch import nn

if __name__ == '__main__':
    conv = nn.Conv2d(3,1,3,1)
    print(conv.weight.shape)
    print(conv.weight)
    nn.init.zeros_(conv.bias)
    print(conv.bias)
    print(conv.weight)
