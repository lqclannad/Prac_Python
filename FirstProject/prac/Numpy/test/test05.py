# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/14 12:40
# 平台: PyCharm
# 文件名: test05.py
import numpy as np
import os
import PIL.Image as img

path_image = "../image1"
# 神经网络训练的图像的像素值
class Sample:
    '''读取所有图像数据'''
    def read_data(self):
        self.img_arr = []
        # os.listdir(dir) 遍历dir路径最终目录下的所有文件
        for name in os.listdir(path_image):
            imgs = img.open(fr"{path_image}/{name}")
            images = np.array(imgs)
            # images = (np.array(imgs)/255-0.5)*2
            self.img_arr.append(images)
        return self.img_arr

    def get_batch(self, set):
        '''获取随机采样数据的批次'''
        img_ar = self.read_data()
        self.get_arr = []
        for i in range(set):
            # 生成图像个数长度内的一个随机数字
            num = np.random.randint(len(self.img_arr))
            # 将生成的随机数作为图像数据集的索引
            imge = self.img_arr[num]
            # 把得到的随机图像数据累加起来
            self.get_arr.append(imge)
        return self.get_arr


sample = Sample()
abc = sample.get_batch(4)
# 查看随机获得的图像数据
# print(abc)
# 查看随机图像批次形状, 装在的图片数组大小一定都要大
# print(np.shape(abc))
for i in range(len(abc)):
    img.fromarray(abc[i]).show()
