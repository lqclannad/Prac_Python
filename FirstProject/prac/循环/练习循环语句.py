# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/08 18:04
# 文件名: 练习循环语句.py

# 跳过遍历中的8
# a = 0
# while a <= 10:
#     if a == 8:
#         a += 1
#         continue
#     print(a)
#     a += 1

# 循环打印A~Z、a~z
i = 65
print('A~Z:', end=' ')
while i < 91:
    print(chr(i), end=' ')
    i += 1
print()
print('a~z:', end=' ')
i = 97
while i < 123:
    print(chr(i), end=' ')
    i += 1
