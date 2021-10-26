# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/26 16:58
# 平台: PyCharm
# 文件名: torch_test01.py
import numpy as np
import torch

# 判断对象是否是张量类型 torch.is_tensor(obj)
print(torch.is_tensor(torch.tensor([1])))
print(torch.is_tensor([1]))

# 将ndarray转换为tensor
n1 = np.array([[1,2,3],[4,5,6]])
print(n1, type(n1))
t1 = torch.from_numpy(n1)
print(t1, type(t1))

print(torch.linspace(1, 2, 100))
