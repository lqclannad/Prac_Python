# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 15:50
# 文件名: prac_map.py
# map 集合
def square(x):
    return x ** 2


a_list = [1, 2, 3, 4, 5]
a_list = list(map(square, a_list))  # 返回的是迭代器，需转换为列表
print(a_list)
a_list = [1, 2, 3, 4, 5]
a_list = list(map(lambda x: x ** 2, a_list))  # 使用lambda匿名函数
print(a_list)
