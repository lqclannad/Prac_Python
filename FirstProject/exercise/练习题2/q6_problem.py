# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 15:22
# 文件名: q6_problem.py
# 一行代码实现对列表a中的偶数位置的元素进行加3后求和
print(sum(list(map(lambda x: [1, 2, 3, 4, 5, 6][x]+3, list(filter(lambda x: x % 2 == 0, range(len([1, 2, 3, 4, 5, 6]))))))))


'''
# 参考：https://blog.csdn.net/qq_37901820/article/details/83098143
# 1)取出偶数索引，2)取出对应值，3)对应值+3，4)求和
# 1)过滤索引 filter
arr = [1, 2, 3, 4, 5, 6]
filter_nums = list(filter(lambda x: x % 2 == 0, range(len(arr))))  # [0, 2, 4]
# 2)取值
get_values = list(map(lambda x: arr[x], filter_nums))  # [1, 3, 5]
# 3)值+3
add_3_values = list(map(lambda x: x+3, get_values))  # [4, 6, 8]
# 4)求和
print(sum(add_3_values))

map,lambda表达式还不是多了解，用得不多
'''
