# coding: utf-8
# 用户: 刘泉
# 时间: 2021/11/04 12:35
# 平台: PyCharm
# 文件名: test04.py
from PIL import Image

img1 = Image.open("img/92307362_p0_master1200.jpg")
img2 = Image.open("img/90983974_p0_master1200.jpg")

# img1 粘贴到 img2上面
img2.paste(img1,(0,400))
img2.show()
