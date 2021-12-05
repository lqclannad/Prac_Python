# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/03 21:41
# 文件名称: sample.py
# 开发工具: Pycharm
import os

x = 0
root = "E:/data/xiaohuangren/bg_pic"
for sub_dir in os.listdir(root):
    if sub_dir.startswith("bg_pic"):
        for file_name in os.listdir(f"{root}/{sub_dir}"):
            print(file_name)