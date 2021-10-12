import PIL.Image as image
import PIL.ImageDraw as draw
import PIL.ImageFont as imgfont
import PIL.ImageFilter as ifr
import random
font = imgfont.truetype("../font/msyh.ttc", 60)


def randchar():
    # 生成随机字母
    return chr(random.randint(65, 90))


def b_color():
    # 生成随机背景色
    return (random.randint(64, 255),
            random.randint(64, 255),
            random.randint(64, 255))

def f_color():
    # 生成随机背景色
    return (random.randint(32, 128),
            random.randint(32, 128),
            random.randint(32, 128))


w = 240
h = 120
def img():
    return image.new("RGB", (w, h), (255,255,255))


if __name__ == '__main__':
    img = img()
    image = draw.Draw(img)
    for x in range(w):
        for y in range(h):
            image.point((x, y), fill=b_color())
    for i in range(4):
        image.text((60*i+10, 30), text=randchar(), fill=f_color(), font=font)
    img.show()
