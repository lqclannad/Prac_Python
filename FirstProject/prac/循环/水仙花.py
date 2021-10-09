# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/08 12:51
# 文件名: 水仙花.py
x = 0
y = 0
z = 0
print('水仙花数:', end=' ')
for x in range(10):
    for y in range(10):
        for z in range(10):
            sum1 = x**3 + y**3 + z**3
            sum2 = x*100 + y*10 + z
            if sum1 == sum2 > 99:
                print(sum1, end='、')