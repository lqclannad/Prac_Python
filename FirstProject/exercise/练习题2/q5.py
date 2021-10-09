# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 15:17
# 文件名: q5.py
# 定义函数实现字符串反转 例如：输入str="string"输出'gnirts'
def reverse(s: str):
    a = list(s)
    a.reverse()
    t = ''
    for i in a:
        t += i
    return t


print(reverse('string'))
