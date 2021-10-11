# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/11 23:10
# 文件名称: car.py
# 开发工具: Pycharm
class car:
    color = "白色"
    name = "特斯拉"
    speed = "360km/h"

    def run(self):
        print("车跑起来了：颜色：{0}，型号：{1}，时速：{2}".format(self.color, self.name, self.speed))


c1 = car()  # 创建对象
c1.run()
c1.color = "红色"
c1.run()


class car2():

    def __init__(self):
        self.color = "白色"
        self.name = "特斯拉"
        self.speed = "360km/h"

    def run(self):
        print("车跑起来了：颜色：{0}，型号：{1}，时速：{2}".format(self.color, self.name, self.speed))


c2 = car2()
c2.color = "蓝色"
c2.run()
