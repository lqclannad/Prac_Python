# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/04 11:23
# 平台: PyCharm
# 文件名: test03.py
# 生成验证码
import random

from PIL import Image, ImageDraw, ImageFont


class GenerateCode:
    # 生成随机的内容（A~Z）
    def getcode(self):
        return chr(random.randint(65,90))

    # 生成随机的背景颜色
    def bgcolor(self):
        return (random.randint(90,160),
                random.randint(90,160),
                random.randint(90,160))

    # 生成字体颜色
    def fontcolor(self):
        return (random.randint(60, 120),
                random.randint(60, 120),
                random.randint(60, 120))

    #
    def gen_img(self):
        w, h = 240, 60
        # 画板
        panel = Image.new(size=(w,h),color=(255,255,255),mode="RGB")
        # 画笔
        draw = ImageDraw.Draw(panel)
        # 字体
        font = ImageFont.truetype("font/STLITI.TTF", size=40)
        for y in range(h):
            for x in range(w):
                draw.point((x, y),fill=self.bgcolor())
        for i in range(4):
            code = self.getcode()
            print(code)
            draw.text((60*i+20, 15),text=code, fill=self.fontcolor(), font=font)
        return panel

if __name__ == '__main__':
    genter = GenerateCode()
    img = genter.gen_img()
    img.show()


print(chr(90))
