# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/01 17:35
# 平台: PyCharm
# 文件名: test01.py

import numpy as np

# a = np.arange(6).reshape(3,2)
# print(a)
# print(a.shape)
# print(a[[0,0]])     # 取2次第0行
# print(a[[0,1]][:,[0,0]])
# print(a[[0,1],0])
# print(a[[0,1],[0,1]])
# print(a[[0,1]])
# print(a[[0,1]][:,1])
# print(a[[0,1]][[1]])

a = np.arange(1,49).reshape(2,2,3,2,2)
print(a)
print(a.shape)
print("=======================")
print(a[:,:,[0,2]].shape)
print("=======================")
print(a[:,:,:-1].shape)
print("=======================")
print(a[:,:,[0,2],[0,1]].shape)
print("=======================")
print(a[:,:,[0,2],[0,1],[1,0]].shape)
print("=======================")
print(a[:,:,[0,2],[0,1],[[1,0]]].shape)
print("=======================")
print(a[:,:,[0,2],[[0,1],[1,0]]].shape)
