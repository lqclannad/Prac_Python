class Student:
    # 初始化时调用此方法
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 打印自身时调用此方法
    def __str__(self):
        return "姓名:{0},性别:{1},年龄:{2}".format(self.name, self.sex, self.age)


s1 = Student("刘泉", 21, "男")
print(s1)
