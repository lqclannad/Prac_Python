# _*_ coding:utf-8 _*_
# 我的名字: liev-LQ
# 创建时间: 2021/10/07 21:00
# 文件名称: practice_3-8.py
# 开发工具: Pycharm
# 3-8  放眼世界
# 想出至少 5 个你渴望去旅游的地方。
# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
sceneries = ["The People's Liberation Monument",
             "Dazu Rock Carvings",
             "The Great Hall of the People",
             "The natural bridges",
             "Furong Cave in Wulong",
             "Fishing Town/Fishing City",
             "Three Gorges",
             "China Three Gorges Museum"]
# 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始 Python 列表。
print('原来的顺序:', sceneries)
# 使用 sorted() 按字母顺序打印这个列表，同时不要修改它。
print('sorted()按字母顺序打印:', sorted(sceneries))
# 再次打印该列表，核实排列顺序未变。
print('原来的顺序:', sceneries)
# 使用 sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print('sorted()按与字母顺序相反的顺序打印:', sorted(sceneries, reverse=True))
# 再次打印该列表，核实排列顺序未变。
print('原来的顺序:', sceneries)
# 使用 reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
sceneries.reverse()
print('reverse()转置:', sceneries)
# 使用 reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
sceneries.reverse()
print('reverse()再转置:', sceneries)
# 使用 sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
sceneries.sort()
print('sort()按字母顺序排列:', sceneries)
# 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
sceneries.sort(reverse=True)
print('sort()与字母顺序相反的顺序排列:', sceneries)


'''
# 参考：https://zhidao.baidu.com/question/94875933.html
解放碑：The People's Liberation Monument
大足石刻：Dazu Rock Carvings
人民大礼堂：The Great Hall of the People
武隆天生三桥/芙蓉洞The natural bridges/Furong Cave in Wulong
钓鱼城：Fishing Town/Fishing City
长江三峡:Three Gorges
三峡博物馆:China Three Gorges Museum
'''