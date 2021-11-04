# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/04 12:38
# 平台: PyCharm
# 文件名: test05.py
import numpy as np
from PIL import Image

# 将图像转为矩阵
img = Image.open("img/OIP-C (3).jpg")
img_data = np.array(img)
# print(img_data)
# print(img.size)
# print(img_data.dtype)
# print(img_data.shape)

# img = Image.fromarray(img_data,"RGB")
# img.show()

# img2 = img.copy()
# img2.show()

# 思考题1：将图片均分为4张图片
w, h = img.size
# img11 = img.crop(box=(0, 0, w // 2, h // 2))
# img12 = img.crop(box=(w // 2, 0, w, h // 2))
# img13 = img.crop(box=(0, h // 2, w // 2, h))
# img14 = img.crop(box=(w // 2, h // 2, w, h))
# img11.show()
# img12.show()
# img13.show()
# img14.show()
print(img_data.shape)
img_data = img_data.reshape((2,h//2,2,w//2,3))
print("切分之后的形状：",img_data.shape)
img_data = img_data.transpose(0,2,1,3,4)
print("转置之后的形状：",img_data.shape)
img_data = img_data.reshape(-1,h//2,w//2,3)
print("分割之后的形状：",img_data.shape)


# 思考题2：将RGB三通道分为单通道的R、G、B三张图片
img_data1 = img_data.copy()
img_data2 = img_data.copy()
img_data3 = img_data.copy()
img_data1[:, :, [1, 2]] = 0
img_data2[:, :, [0, 2]] = 0
img_data3[:, :, [0, 1]] = 0
img21 = Image.fromarray(img_data1)
img22 = Image.fromarray(img_data2)
img23 = Image.fromarray(img_data3)
img21.show()
img22.show()
img23.show()

# print("=============================")
# print(img_data.size)
# print(img_data)
# print("===============")
# img21 = Image.fromarray(img_data[:,:,0])
# a = np.array(np.arange(12)).reshape(1,4,3)
# print(a)
# a[:,:,[0,1]]=0
# print(a)
