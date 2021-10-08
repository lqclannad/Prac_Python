# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/07 19:40
# 文件名称: practice_3-5.py
# 开发工具: Pycharm
# 3-5  修改嘉宾名单
# 你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习 3-4 时编写的程序为基础，在程序末尾添加一条 print 语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
guests = ['李智宇', '杨霖萱', '阳涛', '马涛', '吴世超', '文怡轩']
guests[5] = '李顺'
for guest in guests:
    message = f'''Dear {guest}:
    I will hold a dinner tomorrow. Would you want to come on?
    '''
    print(message)
