# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 15:12
# 文件名: q4.py
# 删除列表中的重复元素
a_list = ['a', 'b', 'c', 'b']
a_list = list(set(a_list))  # set()去重
print(f'经过set()去重后的列表:{a_list}')
