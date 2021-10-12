class Person:
    def __init__(self):
        self.__age = 0  # 只能在当前类内部进行访问

    def pr(self):
        print("你的年龄是:", self.__age)

    def change_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("年龄不合法!")


p1 = Person()
p1.change_age(21)
# p1.age = 21  # 私有类属性值改变不了
p1.pr()
