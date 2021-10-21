# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/21 10:16
# 平台: PyCharm
# 文件名: ndarray_test.py
import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
# ndarray.ndim - 数组的轴(维度)的个数。
print(a.ndim)  # 2
# ndarray.shape - 数组的维度。这是一个整数的元组，表示每个维度中数组的大小
print(a.shape)  # （3，5）
# ndarray.dtype - 一个描述数组中元素类型的对象。numpy.int32、numpy.int16和numpy.float64
print(a.dtype.name)  # int32
# ndarray.itemsize - 数组中每个元素的字节大小。
print(a.dtype.itemsize)  # 4
# ndarray.data - 该缓冲区包含数组的实际元素
print(a.data)   # <memory at 0x000002BDBE7FBE10>
