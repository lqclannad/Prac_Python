# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 16:50
# 文件名: q9.py
# 1)什么是lambda函数？2)它有什么好处？3)另外python在函数编程方面提供了些什么函数和语法？
even = lambda x: x % 2 == 0

'''
--初识lambda
最初接触lambda是在学习Android studio做软件开发，调用一些函数时，系统提示用lambda表达式进行替换
替换后的那块函数调用代码变得异常简洁，对lambda表达式留下了好感。
有些函数在有带参的情况下，直接将参数列出，然后"->"指向内部代码块就行了。

--1)什么是lambda函数？
匿名函数

--2)它有什么好处？
我觉得lambda函数最大的好处就是极大程度上减轻了代码的臃肿程度以及美化了代码的观赏性。

--3)python在函数编程方面提供了些什么函数和语法？
这个达不来...我去搜搜

参考：https://blog.csdn.net/weixin_30655569/article/details/95835752
1) lambda是Python中的匿名函数。
2) 它语法简单，简化代码，不会产生命名冲突，污染命名空间。
3) Python提供了map，reduce，filter等函数方法，提供了装饰器，闭包等语法
'''
