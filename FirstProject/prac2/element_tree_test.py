# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/17 14:37
# 文件名称: element_tree_test.py
# 开发工具: Pycharm
import xml.etree.cElementTree as et

tree = et.parse("foods.xml")
foods = tree.getroot()
print(foods, foods.get("shelf"))

for food in foods.findall("annotation"):
    verified = food.get("verified")
    folder = food.find("folder").text
    filename = food.find("filename").text
    source = food.find("source").text
    size = food.find("size").text
    print(verified, folder, filename, source, size)
