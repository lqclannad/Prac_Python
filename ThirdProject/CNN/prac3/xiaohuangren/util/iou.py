# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/04 0:11
# 文件名称: iou.py
# 开发工具: Pycharm
import numpy as np

def iou(arr_1,arr_2):
    area_1 = (arr_1[2]-arr_1[0]) * (arr_1[3]-arr_1[1])
    area_2 = (arr_2[2] - arr_2[0]) * (arr_2[3] - arr_2[1])
    #交集面积
    x_1 = np.maximum(arr_1[0],arr_2[0])
    y_1 = np.maximum(arr_1[1], arr_2[1])
    x_2 = np.minimum(arr_1[2], arr_2[2])
    y_2 = np.minimum(arr_1[3], arr_2[3])

    inv = (x_2-x_1)*(y_2-y_1)
    iou = inv/(area_1+area_2-inv)
    return iou


if __name__ == '__main__':
    arr1 = np.array([44,44,100,100])
    arr2 = np.array([55,55,111,111])
    print(iou(arr1,arr2))
