# _*_ coding:utf-8 _*_
# 我的名字: liev-LQ
# 创建时间: 2021/10/07 19:31
# 文件名称: practice_3-4.py
# 开发工具: Pycharm
# 3-4  嘉宾名单
# 如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少 3 个你想邀请的人；然后，使用
# 这个列表打印消息，邀请这些人来与你共进晚餐。
guests = ['李智宇', '杨霖萱', '阳涛', '马涛', '吴世超', '文怡轩']
for guest in guests:
    message = f'''Dear {guest}:
    I will hold a dinner tomorrow. Would you want to come on?
    '''
    print(message)
