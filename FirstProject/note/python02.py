# _*_ coding:utf-8 _*_
# 我的名字: liev-LQ
# 创建时间: 2021/10/06 23:44
# 文件名称: python02.py
# 开发工具: Pycharm
# Python基础课程(第一部分3、第二部分1)
# print(4.0e2)
# print(4e210)
# print(True*2)
# print(3j)
# print(type(3j))
'''
python3 - 六个标准数据类型
> Number
    > int/float/bool/complex(复数)
    int > (-∞,+∞)整型
    float > 科学技术标志e/E
    bool > True/1 False/0 (可当作值进行运算)
    complex > 虚部以j/J结尾 (eg: 3+4j)
    二进制 > b > 0b11
    八进制 > o > 0o11
    十进制 > 11
    十六进制 > x > 0x11
        > bin(n) 10进制的n -> 2进制
        > oct(n) 10进制的n -> 8进制
        > int('n', m) -> m进制的n -> 10进制
        > hex(n) 10进制的n -> 16进制
> String
    's',"t",'''r''',"""i"""，定义字符串的四种方式
    # 单行注释
    ''' ''' 多行注释
    """ """ 多行注释
    print('xxx is {n}'.format(a, b, c, d)).  {n}可转义为format内部下标为n的变量或常量
    print('xxx is %i, yyy is %i' % (1+2, 3-1)).  i是类型
    * 切片
    序列名[起始索引:终末位置]
    [:] 左边默认为0,右边默认为序列长度
    'a'+'b' => 'ab' -> +表示字符串连接符 (+两边都为字符串时表示字符串连接符)
    'a'* 2 => 'aa' -> *表示将前一字符串重复2遍 (字符串 * 数字)
    r'D:\Code\Pycharm\Python_Base' -> r表示抑制转义字符，后面跟的字符串内的\将不起作用
    不可变性 - 数字、字符串、元组
> List
> Tuple
> Sets
> Dictionary
'''
# print(int('0xd9', 16))
# print('xxx is {2}'.format(0, 1, 2))
# print('xxx is %i' % (1+2))
# print(help('str'))
# print('abc joker'.title())  # title() 首字符大写
# print("mnsdfads".__len__())
# print(len("mnsdfads"))
grades = [22, 33, 44]
print(grades)
grades.pop(0)
print(grades)
grades.insert(1, 66)
print(grades)
grades.append(77)
print(grades)
grades.sort()
print(grades)
# a = -3
# print(a)
# a = abs(a)
# print(a)
# a = a.__sub__(2)
# print(a)
