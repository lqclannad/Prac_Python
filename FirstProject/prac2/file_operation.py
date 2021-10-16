# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/14 16:37
# 平台: PyCharm
# 文件名: file_operation1.py
import os.path

# mode- r读 w写 w+读写 a追加
# 读写不能同时进行
filename = "test.txt"

file = open(filename, "r")
# file.write("\nHELLO！")
str = file.read()
print(str)
file.close()

# 判断文件夹是否存在，不存在就创建
path = r"G:\code\python\Prac_Python\FirstProject\prac2\test.txt"
file_path, file_name = os.path.split(path)
if not os.path.exists(file_path):
    os.mkdir(file_path)

file = open(path, "w")
file.write("Python 是一门很好的语言！")
file.close()

# ★read() 返回一个包装好的字符内容
# readline() 返回第一行内容
# ★readlines() 返回一个列表，以行为元素
path = r"D:\Code\Pycharm\Prac_Python\FirstProject\prac2\test.txt"
file = open(path, "r")
# str = file.read()
# str = file.readline()
# str = file.readlines()
for line in file.readlines():
    print(line)
# in后面跟的是一个序列，列表是序列，序列不一定是列表
for line in file:
    print(line, end='')
file.close()
