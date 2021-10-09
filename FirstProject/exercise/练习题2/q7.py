# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 16:46
# 文件名: q7.py
# List = [-2, 1, 3, -6]，如何实现以绝对值大小从小到大将 List 中内容排序
List = [-2, 1, 3, -6]
for i in range(len(List)):
    for j in range(i):
        if abs(List[i]) < abs(List[j]):
            List[i], List[j] = List[j], List[i]
print(List)
