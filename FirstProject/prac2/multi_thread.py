# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/17 16:26
# 文件名称: multi_thread.py
# 开发工具: Pycharm
import threading
import time


def fun1():
    for i in range(10):
        print(threading.currentThread().getName(), i)
        if i == 5:
            thread = threading.Thread(target=fun2, name="线程二")
            thread.start()
            thread.join()


def fun2():
    for i in range(65,76):
        print(threading.currentThread().getName(), chr(i))


thread1 = threading.Thread(target=fun1, name="线程一")
thread1.start()
