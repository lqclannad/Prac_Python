# coding: utf-8
# 用户: 刘泉
# 时间: 2021/10/28 9:55
# 平台: PyCharm
# 文件名: test05.py
from PIL import Image, ImageDraw, ImageFont, ImageFilter

font = ImageFont.truetype('../font/msyh.ttc',15)
img = Image.open('../image1/92307362_p0_master1200.jpg')
print(img)
# 基本形状操作
img1 = img.resize((152, 255))
img2 = img.rotate(90)
img3 = img.convert('L')
# 加入画图工具 Draw
d_img = ImageDraw.Draw(img)
d_img.point((200,200),fill='red')
d_img.rectangle((200,130,650,550), outline='red')
d_img.text((200,130),text='漫画少女',fill='blue',font=font)
# paste() 将一张图片粘贴到这张图上，后跟的参数指粘入的位置
img.paste(img3, (0,600))
# BLUR() - 模糊
# CONTOUR() - 素描
imge = img.filter(ImageFilter.CONTOUR())
imge.show()
# imge.save('../image/wawq.png')
