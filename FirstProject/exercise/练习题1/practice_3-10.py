# _*_ coding:utf-8 _*_
# 我的名字: liev-LQ
# 创建时间: 2021/10/07 21:29
# 文件名称: practice_3-10.py
# 开发工具: Pycharm
# 3-10  尝试使用各个函数
# 想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列
# 表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
languages = []
# 增加
languages.append('Chinese')
languages.insert(1, 'English')
languages.extend(['Russian', 'Japanese', 'Korean', 'French', 'German', 'Italian'])
print(languages)
# 删除
languages.pop()     # 默认弹出最后一个
languages.pop(5)    # 弹出指定索引
languages.remove('Korean')  # 删除指定值(若不存在报错ValueError)
del languages[3]    # 语句删除
print('删除完后:{}'.format(languages))
# 修改
languages[2] = 'Spanish'
print('修改完后:{}'.format(languages))
# 查询
print('当前列表languages的长度为{}'.format(len(languages)))
# 排序
languages.sort()
print('sort()默认升序{}'.format(languages))    # 升序
languages.sort(reverse=True)
print('sort(reverse=True)翻转后:{}'.format(languages))
print('当前序列:{}'.format(languages))
print('sorted():{}'.format(sorted(languages)))
print('当前序列:{}'.format(languages))
languages.reverse()
print('.reverse()翻转后:{}'.format(languages))
'''
List []
    添加
        .append(obj) 追加元素
        .insert(index, obj) 往索引index处插入一个元素
        .extend(list) 追加列表
    删除
        .pop(index) 删除索引index处的元素,不写默认最后一个
        .remove(x) 删除list列表里值为x的元素,如不存在报错ValueError(值不存在于列表中)
        (语句) del list[index] 删除list集合索引index
    修改
        list[index] = x 将list集合里索引index处的值修改为x
    查询
        len(list) 查看元素个数
    排序
        .sort() 升序排序
        .sort(reverse=True) 反转,降序排序;如果=False,则为升序排序
        sorted(list) 临时排序,不对原列表进行修改
        .reverse() 排序元素翻转
'''