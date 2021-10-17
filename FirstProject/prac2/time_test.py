# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/17 19:25
# 文件名称: time_test.py
# 开发工具: Pycharm
import time

# Sun Oct 17 20:01:37 2021
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 固定格式 2021-10-17 19:26:38
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 时间戳 1634470040.737892
print(time.time())

# 字符串转换为时间戳 Sun Oct 17 20:01:37 2021 -> 1634472097.0
print(time.mktime(time.strptime("Sun Oct 17 20:01:37 2021", "%a %b %d %H:%M:%S %Y")))


# calendar
import calendar

# 2020年 1月 日历
cal = calendar.month(2020, 1)
print(cal)
# 2020年 日历
cal = calendar.calendar(2020, w=2, l=1, c=6)
print(cal)
