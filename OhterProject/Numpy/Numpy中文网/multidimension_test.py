# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/21 14:50
# 平台: PyCharm
# 文件名: multidimension_test.py
import numpy as np


def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(f'b:{b}')
print(f'b[2, 3]:{b[2, 3]}')
print(b[0:5, 1], b[:, 1])
print(f'b[1:3, :]:{b[1:3, :]}')
print(f'b[-1]:{b[-1]}')    # 当提供的索引少于轴的数量时，缺失的索引被认为是完整的切片

print("——————————————————————————")
c = np.array([[[0, 1, 2],
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(f'c.shape:{c.shape}')
print(f'c[1,...]:\n{c[1,...]} same as c[1,:,:] or c[1]')
print(f'c[...,2]:\n{c[...,2]} same as c[:,:,2]')

print("——————————————————————————")
# 对多维数组进行迭代(iterating)相对于第一个轴完成
for row in b:
    print(row)

# 对每个元素进行迭代
for element in b.flat:
    print(element)
