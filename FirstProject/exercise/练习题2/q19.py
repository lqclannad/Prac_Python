# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/09 23:00
# 文件名称: q19.py
# 开发工具: Pycharm
# 用代码体现继承的特点。
class Animal():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def display(self):
        print(f'大家好，我是{self.name}, 我今年{self.age}岁了，我是{self.sex}的。')


class Cat(Animal):
    def __init__(self, name, age, sex, func):
        super(Cat, self).__init__(name, age, sex)
        self.func = func

    # 覆盖父类的方法
    def display(self):
        print('子类重构，覆盖了父类的方法。')

    def show_me(self):
        print(f'大家好，我是{self.name}, 我今年{self.age}岁了，我是{self.sex}的，我会{self.func}。')


if __name__ == '__main__':
    cat = Cat('小猫', 5, '男', '抓老鼠')
    cat.display()
    cat.show_me()
