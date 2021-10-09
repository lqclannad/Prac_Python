# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/08 9:07
# 文件名: python04.py
# 条件语句
# num = 9
#
# if num > 0:
#     print("a")
# elif num > 1:
#     print("b")
# elif num > 2:
#     print("c")
# elif num > 3:
#     print("d")
# elif num > 4:
#     print("e")
# else:
#     print("error")

# a = 'I am a little boy'
# for s in a:
#     print(s)
# for a in range(3):
#     print(a)
# for a in range(1, 3):
#     print(a)
# for a in range(1, 5, 2):
#     print(a)
a = {1, 5, 4, 3, 2, 6}
# a = a ^ {8, 2, 3}
a.symmetric_difference({8, 2, 3})
print(a)
a = a.intersection({4, 5, 6})   # 交集
print(a)


'''
条件语句 if 
    非0、非空(None)值为True，0或None值为False
    复合布尔表达式 if false and other , other表达式不会被执行.
    逻辑运算符优先级低于比较运算符
循环语句 while for
    for .. in range(num), range(num) -> (0, num)
    for .. in range(num,num2), range(num,num2) -> (num, num2)
    for .. in range(num,num2,num3), range(num,num2,num3) -> (num, num2) 每次叠加num3
'''


