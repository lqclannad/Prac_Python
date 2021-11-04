# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/04 9:58
# 平台: PyCharm
# 文件名: test02.py
from PIL import Image, ImageFilter

img = Image.open('img/92307362_p0_master1200.jpg')
# print(img)
# pixel = img.getpixel((150,120))
# print(pixel)
# img.show()
#
# w, h = img.size
# print(w, h)
# mode = img.mode
# print(mode)
#
# # 转换图像的色彩模式
# img = img.convert('L')
# pixel = img.getpixel((150,120))
# print(pixel)
# img.show()
#
# # 转换图像的色彩模式
# img = img.convert('RGB')
# pixel = img.getpixel((150,120))
# print(pixel)
# img.show()

# # 缩放图片
# img.show()
# w, h = img.size
# # 重新采样 resample=Image.ANTIALIAS 消除锯齿
# img = img.resize((w//2,h//2), resample=Image.ANTIALIAS)
# print(img.size)
# img.show()
# # 旋转
# img = img.rotate(30)
# img.show()
# # 抠图
# img = img.crop((w//4,h//4,w//2,h//2))
# img.show()

# 滤波器
img.show()
img = img.filter(ImageFilter.CONTOUR) # 素描
# img = img.filter(ImageFilter.BLUR)    # 模糊
# img = img.filter(ImageFilter.DETAIL)  # 锐化
# img = img.filter(ImageFilter.EMBOSS)    # 浮雕
img.show()
# 保存图像
img.save("img/awsl.jpg")
