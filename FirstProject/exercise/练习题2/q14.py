# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 17:36
# 文件名: q14.py
# 定义一个学生类。有下面的类属性：
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:
# zm = Student('zhangming',20,[69,88,100])
# 返回结果：
# zhangming
# 20
# 100
class Student():
    def __init__(self, name: str, age: int, grade: list):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.grade)


if __name__ == '__main__':
    zm = Student('zhangming', 20, [69, 88, 100])
    mz = Student('mingzhang', 30, [73, 62, 89])
    print(zm.get_name())
    print(zm.get_age())
    print(zm.get_course())
    print(mz.get_name())
    print(mz.get_age())
    print(mz.get_course())
