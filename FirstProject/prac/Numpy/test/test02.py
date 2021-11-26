import numpy as np
import PIL.Image as img

# a = np.arange(12).reshape(4, 3)
# b = 3
# c = a * b
# print(a)
# print(c)

# 形状不同，后缘维度不同
'''
a = np.arange(12).reshape(2, 2, 3)
print(a, '\n')
b = [3, 2, 1]
print(a+b)
'''
# 转置
'''
a = np.arange(24).reshape(2, 3, 4)
print(a)
b = a.T
print(b.shape)
print(b)
c = np.transpose(a, [1, 0, 2])
print(c)
print(c.shape)
'''

# 数组-图像
path = '../image/92307362_p0_master1200.jpg'
i = img.open(path)
arr = np.array(i)
# i.show()
# image_shape - (n), h, w, c
# transpose转置x,y轴
# c = np.transpose(arr, [1, 0, 2])
c = np.transpose(arr, [1, 2, 0])
print(c)
print(c.shape)
c = c.reshape(3, 1200, -1)
print(c.shape)

# 数组转图像
# t = img.fromarray(c)
# t.show()

# 求和 中间值
'''
a = np.arange(24).reshape(2, 3, 4)
print(a, '\n')
# sum求和
b = np.sum(a, axis=1)
print(b, '\n')
# mean中间量的值
c = np.mean(a, axis=1)
print(c, '\n')
'''

# 矩阵相乘
# a = np.arange(12).reshape(4, 3)
# b = np.arange(12).reshape(3, 4)
# print(f'a:\n{a}\n')
# print()
# print(f'b:\n{b}\n')
# print()
# # dot 点乘
# print(f'a*b:\n{np.dot(a, b)}')
