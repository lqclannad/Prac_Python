# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/02 9:50
# 平台: PyCharm
# 文件名: test11.py
import numpy as np

# b=np.arange(720)
# a=b.reshape(2,3,4,5,6)

# print(a)
# print('--------------------')
# print(a[0:1])
# print('--------------------')
# print(a[:, 0:2])
# print('--------------------')
# print(a[:,:,0:2])
# print('--------------------')
# print(a[1:2,0:2,0:2,0:2])

a = np.arange(24).reshape(2,3,4)
print(a[:])
print(a[:,:1])
