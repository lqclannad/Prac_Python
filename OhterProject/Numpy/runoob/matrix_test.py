# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/19 21:14
# 文件名称: matrix_test.py
# 开发工具: Pycharm
import numpy.matlib
import numpy as np

a = np.arange(12).reshape(3, 4)

print('原数组: ')
print(a)
print('\n')

print('转置数组: ')
print(a.T)
'''
原数组: 
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]


转置数组: 
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]

Process finished with exit code 0
'''
print()
print(np.matlib.empty((2, 2)))  # 填充为随机数据
print(np.matlib.zeros((2, 2)))  # 创建一个以 0 填充的矩阵
print(np.matlib.ones((2, 2)))   # 创建一个以 1 填充的矩阵
print(np.matlib.eye(n=3, M=4, k=0, dtype=float))    # 返回一个矩阵，对角线元素为 1，其他位置为零
print(np.matlib.identity(5, dtype=float))   # 单位矩阵
print(np.matlib.rand(3, 3))  # 创建一个给定大小的矩阵，数据是随机填充的。
'''
[[2.28725472e-308 3.38460762e+125]
 [7.20091312e+252 1.33360328e+241]]
 
 [[0. 0.]
 [0. 0.]]
 
 [[1. 1.]
 [1. 1.]]
 
 [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]]
 
 [[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
 
 [[0.48632401 0.86802991 0.49995734]
 [0.27167993 0.9922422  0.98925029]
 [0.56603638 0.01727101 0.09495207]]
 '''

# 矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。
i = np.matrix('1, 2; 3, 4')
print(i)
# [[1 2]
#  [3 4]]

j = np.asarray(i)
print(j)
# [[1 2]
#  [3 4]]

k = np.asmatrix(j)
print(k)
# [[1 2]
#  [3 4]]
