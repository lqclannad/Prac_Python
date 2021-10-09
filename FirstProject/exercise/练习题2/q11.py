# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 17:14
# 文件名: q11.py
# list 对象 alist [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]，
# 请按 alist 中元素的age 由大到小排序；
alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
for i in range(len(alist)):
    for j in range(i):
        if alist[i]['age'] > alist[j]['age']:
            alist[i]['age'], alist[j]['age'] = alist[j]['age'], alist[i]['age']
print(alist)
