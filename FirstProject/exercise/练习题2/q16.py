# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/09 21:05
# 文件名称: q16.py
# 开发工具: Pycharm
# 定义一个列表的操作类：Listinfo
# 包括的方法:
# 1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
# 2 列表元素取值：get_key(num) [num:整数类型]
# 3 列表合并：update_list(list)      [list:列表类型]
# 4 删除并且返回最后一个元素：del_key()
# list_info = Listinfo([44,222,111,333,454,'sss','333'])
class Listinfo():
    def __init__(self, l: list):
        self.l = l

    def add_key(self, keyname: str or int):
        self.l.append(keyname)

    def get_key(self, num: int):
        return self.l[num]

    def update_list(self, l2: list):
        self.l.extend(l2)

    def del_key(self):
        self.l.pop()


if __name__ == '__main__':
    list_info = Listinfo([44, 222, 111, 333, 454, 'sss', '333'])
    print(list_info.l)
    list_info.add_key('add_key')
    print(list_info.l)
    print(list_info.get_key(4))
    list_info.update_list([True, '123'])
    print(list_info.l)
    list_info.del_key()
    print(list_info.l)
