# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/28 18:35
# 文件名称: ex_conv.py
# 开发工具: Pycharm
import numpy as np
from torch import nn

a_conv = nn.Conv2d(1,3,3)
print(a_conv.weight)
print(np.array([[ 63.73006914 ,111.41876557 ,222.32064831 ,317.98118589,   0.99982709]]).shape[0])