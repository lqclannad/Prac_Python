# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/17 22:23
# 文件名称: test01.py
# 开发工具: Pycharm
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        # 客户端上传过来的文件
        f = request.files["file"]
        # 当前文件所在的路径
        basepath = os.path.dirname(__file__)
        # secure_filename(f.filename) 使用上传文件的文件名
        upload_path = os.path.join(basepath, "static/upload", secure_filename(f.filename))
        # 将上传的文件保存到本地
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(port=9001, debug=True)
