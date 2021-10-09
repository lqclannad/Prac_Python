# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/08 8:45
# 文件名: python03.py
# 多目标赋值(序列赋值) 元组 - 长度要匹配
a, b = 3, 4
print(a, b)
a, b = 4, 3
print(a, b)
# 带星号作为列表
# *a, *b, *c = (1, 2, 3)  # 不清楚各个列表分别要带多少元素，报错SyntaxError
# print(a, b, c)
a = b = c = 2  # 多目标赋值
print(a, b, c)
