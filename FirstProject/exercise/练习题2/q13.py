# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 17:30
# 文件名: q13.py
# 用代码体现斐波那契数列
i, j = 0, 1
arr = [i, j]
for k in range(10):
    i, j = j, i+j
    arr.append(j)
print(arr)
