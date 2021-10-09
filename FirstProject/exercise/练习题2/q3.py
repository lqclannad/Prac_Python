# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 15:07
# 文件名: q3.py
# 求1+2!+3!+...+20!的和。
sum20 = 0
for i in range(1, 21):
    temp = i
    for j in range(1, i):
        temp *= j
    sum20 += temp
print(f'1+2!+3!+...+20!的和为{sum20}')
