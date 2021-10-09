# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/09 21:19
# 文件名称: q17.py
# 开发工具: Pycharm
# 定义一个集合的操作类：Setinfo
# 包括的方法:
# 1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
# 2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
# 3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
# 4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
# set_info =  Setinfo(你要操作的集合)
class Setinfo():
    def __init__(self, s: set):
        self.s = s

    def add_setinfo(self, keyname: str or int):
        self.s.add(keyname)

    def get_intersection(self, unioninfo: set):
        return self.s.intersection(unioninfo)

    def get_union(self, unioninfo: set):
        return self.s.update(unioninfo)

    def del_difference(self, unioninfo: set):
        return self.s.difference(unioninfo)


if __name__ == '__main__':
    set_info = Setinfo({1, 4, 5, 7, 9})
    print('被运算set集合:', set_info.s)
    print('add 0, add 10:', set_info.s)
    set_info.add_setinfo(0)
    set_info.add_setinfo(10)
    set_var = {1, 2, 3, 4, 5}
    print('运算set集合:', set_var)
    print('交集:', set_info.get_intersection(set_var))
    set_info.get_union(set_var)
    print('并集:', set_info.s)
    print('差集:', set_info.del_difference(set_var))
