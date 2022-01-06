# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/12/29 20:05
# 文件名称: register.py
# 开发工具: Pycharm
import time

import cv2
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont
from torchvision import transforms

from FourthProject.项目.人脸识别项目.detect import Detector
from FourthProject.项目.人脸识别项目.nets import FaceNet

tf = transforms.Compose([
    transforms.Resize(112),
    transforms.ToTensor(),
])


if __name__ == '__main__':
    name = input("请输入要注册人脸的名字：")
    detector = Detector()
    face_net = FaceNet().cuda()
    video = cv2.VideoCapture(0)
    # 记录帧数
    frame_num = 0
    # 记录注册帧数
    regist_frame_num = 0
    # 存放注册特征
    features = []
    font = ImageFont.truetype("font/SIMLI.TTF",size=28)
    # 判断注册是否已完成
    register_ok = False
    while True:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        # print(frame.shape)      # (480, 640, 3)
        if ret:
            start = time.time()

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(img)
            draw = ImageDraw.Draw(im)
            # 注册框大小 280 * 280  正中间
            draw.rectangle(((160, 80), (460, 380)), outline='blue', width=2)
            # 判断注册框中是否有一个完整的人脸
            boxes = detector.detect(im)
            # 如果框中没有人脸
            if boxes.shape[0] == 0:
                draw.text((180,50),"请将人脸贴近蓝色框内", fill='yellow', font=font)
            # 当蓝色框中只检测到一个人脸
            elif boxes.shape[0] == 1:
                x1, y1, x2, y2, cls = boxes[0,0].item(), boxes[0,1].item(), boxes[0,2].item(), boxes[0,3].item(), boxes[0,4].item()
                draw.rectangle(((x1,y1),(x2,y2)),outline='green', width=2)
                font.size = 20
                draw.text((x1,y1-20),name,fill='green', font=font)
                font.size = 28
                # 当侦测到的人脸框处于蓝色框外时显示警告
                if x1<160 or y1<80 or x2>460 or y2 > 380:
                    draw.text((180,50),"请将人脸贴近蓝色框内",fill='yellow', font=font)
                # 当检测到的人脸置信度小于0.99时显示警告
                elif cls<0.99:
                    draw.text((250, 50), "未检测到人脸", fill='yellow', font=font)
                else:
                    # 注册人脸
                    regist_frame_num += 1
                    register_crop = Image.fromarray(img[int(y1):int(y2), int(x1):int(x2)]).convert("RGB")
                    register_crop = tf(register_crop).cuda()
                    register_crop = register_crop[None, ...]  # [1, 3, 112, 112]
                    # 提取人脸特征
                    feature = face_net.encode(register_crop)
                    # 将特征添加到注册库
                    features.append(feature)
                    if regist_frame_num < 30:
                        draw.text((250, 50), "请左右摇摇头", fill='red', font=font)
                    elif regist_frame_num < 60:
                        draw.text((250, 50), "请上下摆摆头", fill='red', font=font)
                    else:
                        torch.save(features, f"register/{name}.pt")
                        draw.text((160, 50), "人脸注册成功", fill='red', font=font)
                        draw.text((360, 50), "按q键退出", fill='red', font=font)
                        register_ok = True
            # 有多个人脸出现于蓝色框内
            else:
                draw.text((170,50),"框中最多只能出现一个人脸", fill='yellow', font=font)

            img = np.array(im)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imshow("face_register", img)

            end = time.time()
            print(f"第{frame_num}帧，耗时{end-start}")
            frame_num += 1
            if register_ok:
                cv2.waitKey(1000//24)
                break
            if cv2.waitKey(1000//24) & 0xFF == ord('q'):
                break
        else:
            print("读取摄像头失败....")
            break
    video.release()
    cv2.destroyAllWindows()

