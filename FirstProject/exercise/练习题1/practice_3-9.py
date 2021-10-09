# _*_ coding:utf-8 _*_
# 我的名字: liev-LQ
# 创建时间: 2021/10/07 21:26
# 文件名称: practice_3-9.py
# 开发工具: Pycharm
# 3-9  晚餐嘉宾
# 在完成练习 3-4~ 练习 3-7 时编写的程序之一中，使用 len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
# 练习3-4
guests = ['李智宇', '杨霖萱', '阳涛', '马涛', '吴世超', '文怡轩']
for guest in guests:
    message = f'''Dear {guest}:
    I will hold a dinner tomorrow. Would you want to come on?
    '''
    print(message)
print('邀请了{}位嘉宾与吾共度晚餐'.format(len(guests)))
