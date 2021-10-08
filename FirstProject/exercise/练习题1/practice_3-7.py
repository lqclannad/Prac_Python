# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/07 19:57
# 文件名称: practice_3-7.py
# 开发工具: Pycharm
# 3-7  缩减名单
# 你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习 3-6 时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进
# 晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
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

print('——————————————————————————————————————————————————————————————————')

print("I'm sorry that I just can invite only two person now. Thanks for watching this.")

for i in range(len(guests)-2):
    message = f'''Dear {guests[0]}:
        I'm sorry for not being able to fulfill the previous agreement for some reason,
        thank you for watching.
        '''
    print(message)
    guests.pop(0)

print('——————————————————————————————————————————————————————————————————')

for guest in guests[:]:
    message = f'''Dear {guest}:
    Although I just only invite two person, can you receive it to take my dinner?
    '''
    print(message)
    guests.pop(0)

print(guests)
