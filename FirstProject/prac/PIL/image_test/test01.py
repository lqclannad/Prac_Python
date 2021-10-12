import PIL.Image as image
import PIL.ImageDraw as draw
import PIL.ImageFont as imgfont
import PIL.ImageFilter as ifr
import numpy

font = imgfont.truetype("../font/msyh.ttc", 30)
# img1 = image.open("../image/93271202_p0_master1200.jpg")
img1 = image.open("../image/img.png")
image = numpy.array(img1)
print(image)
# img1.show()  # 默认工具打开
# w, h = img1.size
# print(w, h)
# img2 = img1.resize((275, 375))  # 缩放
# img2.show()
# img3 = img2.rotate(45)  # 旋转
# img3.show()
# img2.save("../image/1.jpg")  # 保存图像

# img = draw.Draw(img1)
# img.point((300, 400), fill="red")   # 画点
# # fill-填充，outline-边线
# # img.rectangle(((30, 30), (100, 100)), fill="blue")
# img.rectangle(((30, 30), (100, 100)), outline="red")    # 画矩形
# # img.line((20, 10, 100, 120), fill="red", width=2)
# img.text((330, 530), text="lqclannad", fill="purple", font=font)    # 文本
# # img.arc((100, 100, 500, 500), 0, 300, fill="red")
# img.chord((100, 100, 500, 500), start=200, end=400, outline="red")
#
# img4 = img1.convert("L")
# img1.paste(img4, (320, 320))
# # imge = img1.filter(ifr.BLUR())    # 变模糊
# imge = img1.filter(ifr.CONTOUR())   # 变素描
# imge.show()
