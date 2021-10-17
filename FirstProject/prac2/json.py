# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/16 23:58
# 文件名称: json.py
# 开发工具: Pycharm
import json


'''字符串
data = {
    'no': 1,
    'name': '刘泉',
    'url': 'http://www.lqclannad.site/',
    None: True
}
# python 转 json
json_str = json.dumps(data)
print(f"Python 原始数据: {data} 类型: {type(data)}")
print(f"JSON 对象: {json_str} 类型: {type(json_str)}")

# json 转 python
str = json.loads(json_str)
print(f"Python 对象: {str} 类型: {type(str)}")
'''

data = (1, 2, 3, 4, 5)

with open('data.json', 'w') as f:
    json.dump(data, f)
