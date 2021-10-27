# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/27 17:38
# 平台: PyCharm
# 文件名: build_test02.py
import random

import torch
from torch import nn
import numpy as np


xs = torch.arange(0.01, 1, 100)
ys = [1/2*e-1 for e in xs]
w = random.random()
b = random.random()

class Net(nn.Module):
    def __init__(self):
        super().__init__()
print(xs)