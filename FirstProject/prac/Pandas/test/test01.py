# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/14 15:15
# 平台: PyCharm
# 文件名: test01.py
import numpy as np
import pandas
from pandas import Series, DataFrame

# 左边索引，右边数据
a = Series([1, 2, 3, 4], dtype=np.float32)
print(a)
print(a.values)
print(a.index)
'''
0    1.0
1    2.0
2    3.0
3    4.0
dtype: float32
[1. 2. 3. 4.]
RangeIndex(start=0, stop=4, step=1)
'''
print()
# 自定义(行)索引
# b = Series([4, 5, 6, 7], index=["a", "b", "c", "d"])
b = Series({"a":1, "b":2, "c":3, "d":4})
print(b)
# b["a"] = 8  # 可以根据索引赋值
'''
a    4
b    5
c    6
d    7
dtype: int64
4
'''
print()
# index-行索引 columns-列索引
c = DataFrame(data=[[2, 4, 6], [7, 8, 3], [4, 7, 5]], index=["d","e","f"],columns=["a","b","c"])
print(c)
'''
   a  b  c
d  2  4  6
e  7  8  3
f  4  7  5
'''

