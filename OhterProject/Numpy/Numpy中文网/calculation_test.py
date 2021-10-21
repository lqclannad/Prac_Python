# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/21 13:07
# 平台: PyCharm
# 文件名: calculation_test.py
# 常数运算(Constant arithmetic)和矩阵运算(Matrix Operations)
import numpy as np

''' 基本操作
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(f'{a} - {b} = {a-b}')
print(f'{b}**2 = {b**2}')
print(f'10*sin([20 29 38 47]) = {10 * np.sin(a)}')
print(a<25)
A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A * B)    # 数乘
print(A @ B)    # 点乘
print(A.dot(B))  # 点乘

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi, 3)
c = a+b
print(b.dtype.name)  # 元素数据类型
print(a, b, c)
d = np.exp(c*1j)
print(d, d.dtype.name)
'''

''' axis
a = np.random.random(size=(2, 3))
print(a, a.sum(), a.min(), a.max())
b = np.arange(12).reshape(3, 4)
# axis - 指定轴
print(b, b.sum(axis=0), b.min(axis=0), b.min(axis=0))
print(b, b.sum(axis=1), b.min(axis=1), b.min(axis=1))
# cumsum - cumulative sum along each row
print(b.cumsum(axis=0))
print(b.cumsum(axis=1))
'''

''' 索引、切片、迭代
a = np.arange(10)**3
print(a)
print(a[2:5])
a[:5:2] = -1
print(a)
print(a[::-1])  # 倒序
for i in a:
    print(i**(1/3.))
'''
