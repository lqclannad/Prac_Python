import numpy as np

# 随机数
# 生成一个包含n个随机数字的数组 ndarray
# 前两项是随机数生成范围，第三项指定生成数量
a = np.random.randint(0, 10, 10)
print(a)
print(type(a))

# 生成 0~1 的均匀分布
b = np.random.rand(40)
print(b)

# 标准正态分布 均值0 方差1
c = np.random.randn(10)
print(c)

# 自定义正态分布 - 参数(均值，方差，数量）
d = np.random.normal(4, 5, 100)
print(d)

# 生成 0~1 的均匀分布
e = np.random.random(20)
print(e)
f = np.random.ranf(20)
print(f)
g = np.random.uniform(-1, 1, 100)
print(g)

