# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/13 20:56
# 文件名称: test01.py
# 开发工具: Pycharm
import numpy as np

# 生成numpy数组的几种方法
# 列表之间的转换
'''
x = [[1, 2], [3, 4], [5, 6]]    # 列表 不能运算
print(x)
a = np.array(x)  # 生成矩阵 可以运算
print(a)
b = a.tolist()  # 矩阵转列表
print(b)
# a = np.ndarray([12]).reshape(3, 4)  # reshape() 轴变换
# b = np.ndarray([12]).reshape(2, 2, 3)
# b = np.arange(12).reshape(2, 2, 3)
# dtype=np.float32 指定数据类型为float32
# b = np.arange((12), dtype=np.float32).reshape(2, 2, 3)
# c = np.arange(0, 12, 2)
# print(a)
# shape查看形状
# ndim - 查看维度
# size - 查看大小
# dtype - 查看数据类型
# print(b, np.shape(b), b.shape, b.size, b.ndim, b.dtype)
# print(c)
'''

# 生成零数组、1数组、空数组
'''
a = np.zeros(shape=[4, 10],dtype=np.float32)
b = np.ones(shape=[4, 10],dtype=np.float32)
c = np.empty(shape=[4, 10],dtype=np.float32)
print(a)
print(b)
print(c)
'''

a = np.zeros(shape=[4, 10],dtype=np.float32)  # 8,5,2,6(one-hot)
# b = a[:,8]
# print(b)
for i, k in enumerate(a):
    if i == 0:
        k[8] = 1
    elif i == 1:
        k[5] = 1
    elif i == 2:
        k[2] = 1
    else:
        k[6] = 1
print(a)

c = np.argmax(a, axis=1)
print(c)
d = np.argmin(a, axis=1)
print(d)
e = np.min(a, axis=1)
print(e)
f = np.max(a, axis=1)
print(f)
