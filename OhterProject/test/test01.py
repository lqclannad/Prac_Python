# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/01 19:56
# 文件名称: test01.py
# 开发工具: Pycharm
import os


cur_path = os.getcwd()  # 获取此脚本所处目录地址信息

# for i in range(18):
    # if not os.path.exists(str(i+1)):
    #     os.mkdir(str(i+1))
for filename in os.listdir(fr"{cur_path}"):
    # 判断遍历的文件是否以特定后缀类型结尾
    if filename.endswith(".txt"):
        # os.replace(filename, str(i+1) + "/" + filename)
        # 获取文件名信息
        fname = filename.title().split(".")[0]
        # 将文件名转为int类型用于后续分类提取
        fname = int(fname)
        # 根据文件名的序号大小放入不同的文件夹中
        if fname < 11:
            os.replace(filename,"1/"+filename)
        elif fname < 21:
            os.replace(filename,"2/"+filename)
        elif fname < 31:
            os.replace(filename,"3/"+filename)


