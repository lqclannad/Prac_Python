# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/17 21:03
# 文件名称: re_test.py
# 开发工具: Pycharm
import re

# 简单应用
'''
str = "It's good"
part1 = "good"
part2 = "bad"
print(re.search(part1, str))
print(re.search(part2, str))
'''

# 灵活匹配
'''
str = "you run to cat"
part = r"r[au]n"
print(re.search(part, str))
'''

# 按类型匹配
'''
print(re.search(r"r\dn", "run r4n"))
print(re.search(r"r\Dn", "run r4n"))
print(re.search(r"r\sn", "r\nn r4n"))
'''

string = """dog runs to cat.
I run to dog."""
# re.M - 每行都进行一次匹配
print(re.search(r"^I", string, flags=re.M))
