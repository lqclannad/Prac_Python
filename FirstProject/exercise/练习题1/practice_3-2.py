# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/07 19:15
# 文件名称: practice_3-2.py
# 开发工具: Pycharm
# 3-2  问候语：
# 继续使用练习 3-1 中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
names = ['李智宇', '杨霖萱', '阳涛', '马涛', '吴世超', '文怡轩']
for name in names:
    message = f'''Dear {name}:
    Long time no see, I'm miss you.'''
    print(message)
