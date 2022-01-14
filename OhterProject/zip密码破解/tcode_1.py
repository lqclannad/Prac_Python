# 我的名字: Administrator-LQ
# 创建时间: 2022/01/11 11:01
# 文件名称: tcode.py
# 开发工具: Pycharm
import base64
import zipfile
import sys
import chardet


print('╫╩╘┤╜Γ╤╣├▄┬δ'.isascii())
print(chardet.detect())
print(sys.getdefaultencoding())     # utf-8
z = zipfile.ZipFile("zip_file/tst.zip", 'r')
detected = z.namelist()[0][:-4]
# print(detected)     # ╫╩╘┤╜Γ╤╣├▄┬δ
# print(detected.encode("utf-8"))     # b'\xe2\x95\xab\xe2\x95...'
# print(str.encode(detected))   # b'\xe2\x95\xab\xe2\x95...'
print(bytes(detected))
detected = str.encode(detected)
print(detected)
a = chardet.detect(detected)    # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
print(a)
# print(str("b'â«â©ââ¤âÎâ¤â£âââ¬Î´.txt'".encode("utf-8"),encoding="utf-8"))
# print(str(a[0].encode("utf-8")))
exit()
print(z.namelist()[0])
for i in z.infolist():
    print(i.file_size, i.header_offset)
