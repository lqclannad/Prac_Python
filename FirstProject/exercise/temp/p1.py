# coding=utf-8
# 用户: liev-LQ
# 时间: 2021/10/09 14:22
# 文件名: p1.py
def make_album(singer: str, album: str, song_count=0):
    dic = {'singer': singer, 'album': album}
    if song_count > 0:
        dic['song_count'] = song_count
    return dic


if __name__ == '__main__':
    print(make_album('周华健', '永远陪伴你'))
    print(make_album('林志炫', '蒙娜丽莎的眼泪'))
    print(make_album('齐秦', '狼的专辑', 10))
    # ————————————————————————————————————————
    temp = 'jiang xin yi'
    for i in iter(temp):
        if i == ' ':
            print('此处有空格')
    # ————————————————————————————————————————
    i, j, k = 0, 1, 0
    ten = [i, j]
    while k < 8:
        if k % 2 == 0:
            j += i
        else:
            i += j
        ten.append(i + j)
        k += 1
    print('裴波拉契: ', ten)
