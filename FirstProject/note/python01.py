# _*_ coding:utf-8 _*_
# 我的名字: liev-LQ
# 创建时间: 2021/10/06 22:36
# 文件名称: python01.py
# 开发工具: Pycharm
# Python基础课程(第一部分) - 2
print('1', end='')
print('2')
'''
print('', end='')
print()函数中追加"end="，末尾不加"\n"换行符
'''
print("\"\\")
'''
\ - 转义字符
\a - 音量
\\ - \
\n - 换行
'''
a = 3
b = 4
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)
'''
转换a,b的值
1) c = a; a = b; b = c;
2) a = a+b; b = a-b; a = a-b;
3) a,b = b,a;
4) a = a^b; b = a^b; a = a^b;
'''