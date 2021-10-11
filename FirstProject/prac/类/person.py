# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/11 23:02
# 文件名称: person.py
# 开发工具: Pycharm
class person:
    def open_door(self, door):
        door.opened()


class door:
    def opened(self):
        print("门开了")


p1 = person()
d1 = door()

p1.open_door(d1)
