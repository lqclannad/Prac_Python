# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 17:36
# 文件名: q15.py
# 定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})
class DictClass():
    def __init__(self, dic: dict):
        self.dic = dic

    def del_dict(self, key):
        del self.dic[key]

    def get_dict(self, key):
        if key in self.dic.keys():
            return self.dic[key]
        else:
            return 'not found'

    def get_key(self):
        return self.dic.keys()

    def update_dict(self, merge_dic: dict):
        self.dic.update(merge_dic)
        return list(self.dic.values()).extend(list(merge_dic.values()))


if __name__ == '__main__':
    t_dict = DictClass({'k1': 'v1', 'k2': 'v2'})
    print("t_dict.dic    :", t_dict.dic)
    t_dict.del_dict('k2')
    print("del_dict('k2'):", t_dict.dic)
    print("get_dict('k1'):", t_dict.get_dict('k1'))
    print("get_key()     :", t_dict.get_key())
    t_dict.update_dict({'k3': 'v3', 'k4': 'v4'})
    print("update_dict   :", t_dict.dic)
