# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/21 10:31
# 平台: PyCharm
# 文件名: array_test.py
import numpy as np
import matplotlib.pyplot as plt

''' list、tuple  ->  array
# a = np.array(1, 2, 3, 4)    # WRONG - TypeError
a = np.array([1, 2, 3, 4])  # RIGHT
b = np.array([(1.5, 2, 3), (4, 5, 6)])
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(a)
print(b)
print(c)
'''

''' numpy内置array
zero_array = np.zeros((3, 4))
one_array = np.ones((2, 3, 4), dtype=np.int16)
empty_array = np.empty((2, 3))
print(zero_array)
print(one_array)
print(empty_array)
'''

''' range
range1 = np.arange(10, 30, 5)
range2 = np.arange(0, 2, 0.3)
print(range1)
print(range2)
'''

''' linspace - 接受元素数量的函数
receive = np.linspace(0, 2, 9)
print(receive)  # [0.   0.25 0.5  0.75 1.   1.25 1.5  1.75 2.  ]
x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x)
print(x)
print(f)
'''

''' 打印一二三维数组
a = np.arange(6)
b = np.arange(12).reshape(4, 3)
c = np.arange(24).reshape(2, 3, 4)
print(a)
print(b)
print(c)
'''

