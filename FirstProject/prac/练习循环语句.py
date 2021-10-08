# coding=utf-8
# 用户: liev
# 时间: 2021/10/08 18:04
# 文件名: 练习循环语句.py
# 直角三角形
# for i in range(1, 5):
#     for j in range(i):
#         print("* ", end="")
#     print()

# 等腰三角形
# for i in range(1, 6):
#     print(" " * 2 * (5 - i), end="")
#     for j in range(2*i-1):
#         print("* ", end="")
#     print()

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i}*{j}={i*j} ', end='')
    print()
