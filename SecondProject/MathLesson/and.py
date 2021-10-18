# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/18 16:11
# 平台: PyCharm
# 文件名: and.py
import random

xs = [[0, 0], [0, 1], [1, 0], [1, 1]]
ys = [0, 0, 0, 1]

gamma = 0.02

ws = [random.random() for i in range(3)]
print(ws)

for _ in range(400):
    for x,y in zip(xs, ys):
        _y = x[0] * ws[0] + x[1] * ws[1] + ws[2]
        e = _y - y
        # s = 2 * e * x[0]
        ws[0] = ws[0] - 2 * e * x[0]
        ws[1] = ws[1] - 2 * e * x[1]
        ws[2] = ws[2] - 2 * e
        print(e ** 2)
