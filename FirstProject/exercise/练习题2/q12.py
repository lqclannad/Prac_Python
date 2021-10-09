# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 17:25
# 文件名: q12.py
# 将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python 字典：{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }
a_str = "k:1|k1:2|k2:3|k3:4"
elements = a_str.split('|')
a_dict = {}
for kv in elements:
    k = kv.split(':')[0]
    v = kv.split(':')[1]
    a_dict[k] = v
print(a_dict)
