# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/11 23:41
# 文件名称: extends.py
# 开发工具: Pycharm
class A:
    a = 1

    def pr(self):
        print('A')


class B(A):
    a = 2

    def pr(self):   # 子类覆盖父类方法
        print('B')

    def __init__(self, name):
        self.name = name
        print(self.name)


class C(B, A):  # 多继承
    a = 3

    def __init__(self, name):
        super().__init__(name)  # 通过超类将name传至父类

    def pr(self):   # 子类覆盖父类方法
        print('C')


c = C("张三")
c.pr()
