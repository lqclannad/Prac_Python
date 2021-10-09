# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 15:00
# 文件名: q2.py
# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 分母denominator 分子molecular
denominator, molecular = 1, 2
i = 0
sum20 = 0
while i < 20:
    fraction = molecular / denominator
    sum20 += fraction
    denominator, molecular = molecular, denominator+molecular
    i += 1

print(f'2/1，3/2，5/3，8/5，13/8，21/13...前20项之和为{sum20}')
