# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/17 22:03
# 文件名称: test01.py
# 开发工具: Pycharm
from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen("https://www.jueshitangmen.info/27/684381.html").read().decode("utf-8")
print(html)
print("==========================================================")
soup = BeautifulSoup(html, features="lxml")
# 寻找p标签
all_p = soup.find_all('p')
print(all_p)
print("==========================================================")
for i in all_p:
    print(i.get_text())
