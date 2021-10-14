# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/14 11:29
# 平台: PyCharm
# 文件名: test04.py
import numpy as np


# 二维切片
'''
a = np.arange(12).reshape(4, 3)
# 切片
b = a[:]
# 俩c一样
c = a[:1]
c = a[:1][:1]
d = a[:1,:1]
print(a)
e = a[1:,:2]
print(e)
'''

# 三维切片
'''
a = np.arange(24).reshape(2, 3, 4)
print(a)
b = a[:1,:,2:]
print(b)
'''

# 拷贝
'''
a = np.arange(12).reshape(4,3)
# copy只拷贝值
b = a.copy()
c = a
a[0,1] = 10
print(b)    # [0,1]处没变，说明copy只拷贝值
print(c)    # [0,1]处变了，说明c和a共用一块地址
'''

# 拼接
'''
a = np.arange(12).reshape(3, 4)
b = np.array([4,5,6,7])
print(a)
print(b)
c = a.tolist()
d = b.tolist()
print(c)
print(d)
# c.append(d)
# print(c)
c.extend([d])
print(c)
'''

a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(3,4)
print(a)
print(b)
# 形状相同才可以拼接
c = np.vstack((a,b))
print(c)
d = np.hstack((a,b))
print(d)
