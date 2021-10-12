from PIL import Image, ImageDraw, ImageFont

# 图片上绘制交叉线
'''
# with Image.open("../image/img.png") as im:
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    print((0, 0) + im.size)  # (0, 0, x_size, y_size)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)
    im.save("../image/img3.png")
'''
# 绘制部分不透明度文本
'''
# get an image
base = Image.open("../image/img.png").convert("RGBA")
# make a blank image for the text, initialized to transparent text color
txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
# get a font
fnt = ImageFont.truetype("../font/STXINGKA.TTF", 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((110, 210), "Hello", font=fnt, fill=(255, 255, 255, 128))
# draw text, full opacity
d.text((110, 260), "World", font=fnt, fill=(255, 255, 255, 255))

out = Image.alpha_composite(base, txt)

out.show()
out.save("../image/img3.png")
'''
# 绘制多行文本
'''
# create an image
out = Image.new("RGB", (225, 150), (255, 255, 255))

# get a font
fnt = ImageFont.truetype("../font/msyh.ttc", 40)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((5, 5), "Hello\nWorld\nLqclannad", font=fnt, fill=(0, 0, 0))

out.show()
out.save("../image/lqclannadText.png")
'''
# 画线
'''
# with Image.open("../image/img.png") as im:
    d = ImageDraw.Draw(im)
    d.getfont()
    # arc - 画弧线/圆
    d.arc((0,0,250,250), 0, 250, fill="red")
    # chord - 填充弧线/圆
    d.chord((100,100,250,250), 0, 250, fill="red")
    # ellipse - 画椭圆
    d.ellipse((100,400,600,650), fill="blue", outline="red")
    # line - 画线
    d.line((0,0,im.size[0],im.size[1]), fill="red")
    im.show()
'''

