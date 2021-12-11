# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/08 23:32
# 文件名称: utils.py
# 开发工具: Pycharm
import numpy as np


def iou(box,boxes,isMin=False):
    # 计算面积
    box_area = (box[2]-box[0]) * (box[3]-box[1])
    area = (boxes[:,2]-boxes[:,0]) * (boxes[:,3]-boxes[:,1])
    # 找交集
    xx1 = np.maximum(box[0],boxes[:,0])
    yy1 = np.maximum(box[1],boxes[:,1])
    xx2 = np.minimum(box[2],boxes[:,2])
    yy2 = np.minimum(box[3],boxes[:,3])
    # 判断是否有交集
    w = np.maximum(0,xx2-xx1)
    h = np.maximum(0,yy2-yy1)
    # 交集的面积
    inter = w * h
    if isMin:
        ovr = np.true_divide(inter,np.minimum(box_area,area))
    else:
        ovr = np.true_divide(inter,(box_area+area-inter))
    return ovr


def nms(boxes, thresh=0.3, isMin=False):
    if boxes.shape[0] == 0:
        return np.array([])
    _boxes = boxes[(-boxes[:,4]).argsort()]
    r_boxes = []
    while _boxes.shape[0] > 1:
        a_box = _boxes[0]
        b_boxes = _boxes[1:]
        r_boxes.append(a_box)
        index = np.where(iou(a_box,b_boxes,isMin) < thresh)
        _boxes = b_boxes[index]
    if _boxes.shape[0] == 1:
        r_boxes.append(_boxes[0])
    return np.stack(r_boxes)


if __name__ == '__main__':
    bs = np.array([[1, 1, 10, 10, 40], [1, 1, 9, 9, 10], [9, 8, 13, 20, 15], [6, 11, 18, 17, 13]])
    print(nms(bs, thresh=0.1))