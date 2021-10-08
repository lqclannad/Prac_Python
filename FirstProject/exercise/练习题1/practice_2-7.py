# _*_ coding:utf-8 _*_
# 我的名字: Administrator
# 创建时间: 2021/10/07 18:02
# 文件名称: practice_2-7.py
# 开发工具: Pycharm
# 2-7  剔除人名中的空白：
# 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合 "\t" 和 "\n" 各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数 lstrip() 、 rstrip() 和 strip() 对人名进行处理，并将结果打印出来。
name = ' \tFaust\n '
print(name.lstrip())
print(name.rstrip())
print(name.strip())