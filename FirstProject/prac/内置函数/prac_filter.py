# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 15:51
# 文件名: prac_filter.py
# filter 过滤序列
f = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(f))
