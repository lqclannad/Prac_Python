# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 10:11
# 文件名: 练习函数.py
def add(x: int, y: int):
    return x + y


def triangle(length: int):
    for i in range(1, length + 1):
        for j in range(i):
            print("* ", end="")
        print()


def sort(a_list: list, flag: bool):
    for i in range(len(a_list)):
        for j in range(i):
            if flag:
                if a_list[i] < a_list[j]:
                    a_list[i], a_list[j] = a_list[j], a_list[i]
            else:
                if a_list[j] < a_list[i]:
                    a_list[i], a_list[j] = a_list[j], a_list[i]
    return a_list


def change1(a: int):
    a = 3


def change2(b: str):
    b = b.upper()
    return b


def change3(c: list):
    c.append(12)
    return c


def super_add(a, *b):   # *b -> list
    for i in b:
        a += i
    return a


# a=1
def outer():
    # global a
    a = 3  # 闭包

    def inner():
        # nonlocal a
        # global a
        a = 2  # 局部
        print(a)
    inner()
    print(a)


if __name__ == '__main__':
    # print(add(-1, -4))
    # print(triangle(4))
    # list_a = [4, 2, 1, 3, 5]
    # print(sort(list_a, False))  # 升降序排序
    # a = 5
    # change1(a)  # 仅传不可变对象的值进去
    # print(a)
    # b = "add"
    # change2(b)  # 仅传不可变对象的值进去
    # print(b)
    # print(change2(b))
    # c = [12, 42, 133]
    # change3(c)
    # print(change3(c))  # 传入可变对象list的地址
    # print(super_add(3, 34, 423))
    # func_add = lambda a, b: a + b   # lamdba表达式
    # print(func_add(1, 43))
    outer()
