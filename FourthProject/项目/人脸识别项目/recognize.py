# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/29 23:20
# 文件名称: recognize.py
# 开发工具: Pycharm
import time

import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw
from torchvision import transforms

from FourthProject.项目.人脸识别项目.detect import Detector
from FourthProject.项目.人脸识别项目.nets import FaceNet
from FourthProject.项目.人脸识别项目.utils import compare

tf = transforms.Compose([
    transforms.Resize(112),
    transforms.ToTensor(),
])


if __name__ == '__main__':
    video = cv2.VideoCapture(0)
    detector = Detector()
    face_net = FaceNet().cuda()
    # 记录帧数
    frame_num = 0
    # 记录识别到的人脸帧数
    recognize_frame_num = 0
    font = ImageFont.truetype("font/SIMLI.TTF",size=28)
    while True:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        if ret:
            start = time.time()

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(img)
            im2 = Image.fromarray(img[80:380,160:460])
            draw = ImageDraw.Draw(im)
            # 注册框大小 280 * 280  正中间
            draw.rectangle(((160, 80), (460, 380)), outline='blue', width=2)
            # 判断注册框中是否有一个完整的人脸
            boxes = detector.detect(im2)
            print(boxes.shape[0])
            # 如果框中没有人脸
            if boxes.shape[0] == 0:
                draw.text((180,50),"请将人脸贴近蓝色框内", fill='yellow', font=font)
                print("请将人脸贴近蓝色框内")
            # 当蓝色框中只检测到一个人脸
            elif boxes.shape[0] == 1:
                x1, y1, x2, y2, cls = boxes[0, 0].item()+160, boxes[0, 1].item()+80, boxes[0, 2].item()+160, boxes[0, 3].item()+80, boxes[0, 4].item()
                # 当侦测到的人脸框处于蓝色框外时显示警告
                if x1 < 160 or y1 < 80 or x2 > 460 or y2 > 380:
                    draw.text((180, 50), "请将人脸贴近蓝色框内", fill='yellow', font=font)
                    print("请将人脸贴近蓝色框内")
                # 当检测到的人脸置信度小于0.99时显示警告
                elif cls < 0.99:
                    draw.text((250, 50), "人脸识别度不足", fill='yellow', font=font)
                    print("人脸识别度不足")
                # 人脸识别
                else:
                    recognize_frame_num += 1
                    recognize_img = Image.fromarray(img[int(y1):int(y2),int(x1):int(x2)]).convert("RGB")
                    # 计算一次人脸特征
                    recognize_img = tf(recognize_img).cuda()
                    recognize_img = recognize_img[None, ...]
                    face_feature = face_net.encode(recognize_img)
                    # 将提取到的人脸特征拿到注册表里与所有注册过的人脸进行比对
                    name, rate = compare(face_feature, 0.04)
                    if rate > 0:
                        draw.text((x1,y1-30),name,fill='green',font=font)
                        draw.rectangle(((x1,y1),(x2,y2)),outline='red',width=2)
                    else:
                        draw.text((x1, y1-30), name, fill='yellow', font=font)
                        draw.rectangle(((x1, y1), (x2, y2)), outline='red', width=2)
            # 有多个人脸出现于蓝色框内
            else:
                draw.text((170, 50), "框中最多只能出现一个人脸", fill='yellow', font=font)
                print("框中最多只能出现一个人脸")

            img = np.array(im)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imshow("frame",img)

            end = time.time()
            print(f"第{frame_num}帧耗时{end-start}s")
            frame_num += 1
            if cv2.waitKey(1000//24) & 0xFF == ord('q'):
                break
    video.release()
    cv2.destroyAllWindows()
