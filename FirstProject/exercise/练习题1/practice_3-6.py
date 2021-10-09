# _*_ coding:utf-8 _*_
# 我的名字: liev-LQ
# 创建时间: 2021/10/07 19:42
# 文件名称: practice_3-6.py
# 开发工具: Pycharm
# 3-6  添加嘉宾
# 你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# 以完成练习 3-4 或练习 3-5 时编写的程序为基础，在程序末尾添加一条 print 语句，指出你找到了一个更大的餐桌。
# 使用 insert() 将一位新嘉宾添加到名单开头。
# 使用 insert() 将另一位新嘉宾添加到名单中间。
# 使用 append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。
guests = ['李智宇', '杨霖萱', '阳涛', '马涛', '吴世超', '文怡轩']
guests[5] = '李顺'
print('I have found a big dining table!')
guests.insert(0, '罗艺')
guests.insert(len(guests)//2, '唐文昊')
guests.append('梁泷瀚')
for guest in guests:
    message = f'''Dear {guest}:
    I will hold a dinner tomorrow. Would you want to come on?
    '''
    print(message)
