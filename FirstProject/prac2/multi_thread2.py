# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/17 17:44
# 文件名称: multi_thread2.py
# 开发工具: Pycharm
# 锁 - threading.Lock()
import threading

lock = threading.Lock()
ticket = 100


def seal():
    global lock
    global ticket
    lock.acquire()
    while ticket >= 0:
        print(threading.currentThread().getName(), ticket)
        ticket -= 1
    lock.release()


for i in range(3):
    thread = threading.Thread(target=seal, name=f"线程{i + 1}==>")
    thread.start()
