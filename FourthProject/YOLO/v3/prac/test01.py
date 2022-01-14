# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2022/01/10 19:00
# 文件名称: test01.py
# 开发工具: Pycharm
import glob
import xml.etree.cElementTree as ET

import numpy as np

from kmeans import kmeans, avg_iou

# ANNOTATIONS_PATH = "D:\data\VOC\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\Annotations"
ANNOTATIONS_PATH = "E:\data\Yolo_20\outputs"
CLUSTERS = 9


def load_dataset(path):
    dataset = []
    for xml_file in glob.glob("{}/*xml".format(path)):
        tree = ET.parse(xml_file)

        height = int(tree.findtext("./size/height"))
        width = int(tree.findtext("./size/width"))

        try:
            for obj in tree.iter("object"):
                xmin = int(obj.findtext("item/bndbox/xmin")) / width
                ymin = int(obj.findtext("item/bndbox/ymin")) / height
                xmax = int(obj.findtext("item/bndbox/xmax")) / width
                ymax = int(obj.findtext("item/bndbox/ymax")) / height

                xmin = np.float64(xmin)
                ymin = np.float64(ymin)
                xmax = np.float64(xmax)
                ymax = np.float64(ymax)
                if xmax == xmin or ymax == ymin:
                    print("√ ",xml_file)
                dataset.append([xmax - xmin, ymax - ymin])
        except Exception as e:
            print(e, xml_file)
    return np.array(dataset)


if __name__ == '__main__':
    # print(__file__)
    data = load_dataset(ANNOTATIONS_PATH)
    out = kmeans(data, k=CLUSTERS)
    # clusters = [[10,13],[16,30],[33,23],[30,61],[62,45],[59,119],[116,90],[156,198],[373,326]]
    # out= np.array(clusters)/416.0
    # print(out)
    print("Accuracy: {:.2f}%".format(avg_iou(data, out) * 100))
    # print("Boxes:\n {}-{}".format(out[:, 0] * 416, out[:, 1] * 416))
    k = []
    [k.append((round(o[0]*416), round(o[1]*416))) for o in out]
    print(k)
    max_area = 0
    for i in range(9):
        for j in range(9):
            if k[i][0]*k[i][1] > k[j][0]*k[j][1]:
                temp = (k[i][0],k[i][1])
                k[i] = k[j]
                k[j] = temp
    print("1", k)
    for i in k:
        print(i[0]*i[1], end=' ')
    exit()


    # ratios = np.around(out[:, 0] / out[:, 1], decimals=2).tolist()
    # print("Ratios:\n {}".format(sorted(ratios)))
