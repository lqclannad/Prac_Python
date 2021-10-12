def mul(a, b):
    try:
        c = a / b
        d = 'a' + 1
        print(c, d)
    except TypeError:
        print("类型不统一")
    except ZeroDivisionError:
        print("除数不能为0！")
    except:
        print("未知错误")
    else:
        print("没有捕获到异常")


mul(2, 3)
mul(2, 0)
