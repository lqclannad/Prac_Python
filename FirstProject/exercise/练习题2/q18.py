# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/09 22:53
# 文件名称: q18.py
# 开发工具: Pycharm
# 将你自己的信息封装成一个类Student，包括姓名、性别、年龄、家庭地址。并在display()方法中显示这些信息。
class Student():
    def __init__(self, name, sex, age, adr):
        self.name = name
        self.sex = sex
        self.age = age
        self.adr = adr

    def display(self):
        print(f'姓名: {self.name}', end='\n')
        print(f'性别: {self.sex}', end='\n')
        print(f'年龄: {self.age}', end='\n')
        print(f'地址: {self.adr}', end='\n')


if __name__ == '__main__':
    stu = Student('刘泉', '男', 21, '英郡一期')
    stu.display()
