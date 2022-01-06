import os

import cv2
import torchvision.models as models
from torch import nn
import torch
from torch.nn import functional as F
from torch import optim
from torch.utils.data import DataLoader
import torch.jit as jit
from PIL import Image
from torchvision import transforms

tf = transforms.Compose([
    transforms.Resize(112),
    transforms.ToTensor(),
])

class Arcsoftmax(nn.Module):
    def __init__(self, feature_num, cls_num):
        super().__init__()
        self.w = nn.Parameter(torch.randn((feature_num, cls_num)))
        self.func = nn.Softmax()

    def forward(self, x, s=1, m=0.2):
        x_norm = F.normalize(x, dim=1)
        w_norm = F.normalize(self.w, dim=0)

        cosa = torch.matmul(x_norm, w_norm) / 10
        a = torch.acos(cosa)

        arcsoftmax = torch.exp(
            s * torch.cos(a + m) * 10) / (torch.sum(torch.exp(s * cosa * 10), dim=1, keepdim=True) - torch.exp(
            s * cosa * 10) + torch.exp(s * torch.cos(a + m) * 10))

        return arcsoftmax


class FaceNet(nn.Module):

    def __init__(self):
        super(FaceNet, self).__init__()
        self.sub_net = nn.Sequential(
            models.densenet121(pretrained=True),

        )
        self.feature_net = nn.Sequential(
            nn.LeakyReLU(0.1),
            nn.Linear(1000, 512, bias=False),
        )
        self.arc_softmax = Arcsoftmax(512, 12)

    def forward(self, x):
        y = self.sub_net(x)
        feature = self.feature_net(y)
        return feature, self.arc_softmax(feature, 1, 1)

    def encode(self, x):
        return self.feature_net(self.sub_net(x))


def compare(face1, face2):
    face1_norm = F.normalize(face1)
    face2_norm = F.normalize(face2)
    print(face1_norm.shape)
    print(face2_norm.shape)
    cosa = torch.matmul(face1_norm, face2_norm.t())
    return cosa


class Face_recognize():
    def __init__(self):
        self.net = FaceNet().cuda()
        self.net.load_state_dict(torch.load("params/face.pt"))
        self.net.eval()

        # self.register_table = torch.load("params/weight_face.pt")
        self.register_table = {}
        self.max_cosa = [0, ...]
        self.key_name = [0, ...]
        registed_name = ["刘泉", "杨霖萱", "侯捷", "鲁思炜", "钟静"]
        path = "register"
        for face_index in os.listdir(path):
            name = registed_name[int(face_index)]
            registed_feature = []
            for face_img in os.listdir(f"{path}/{face_index}"):
                img = Image.open(f"{path}/{face_index}/{face_img}")
                img = tf(img).cuda()
                feature = self.net.encode(img[None, ...])
                feature = F.normalize(feature)
                registed_feature.append((feature,f"{path}/{face_index}/{face_img}"))
            self.register_table[name] = registed_feature

    def compare(self, face, index):
        self.max_cosa[index] = 0.9
        self.key_name[index] = "陌生人"
        face2 = tf(face).cuda()
        face_feature = self.net.encode(face2[None, ...])
        face_norm = F.normalize(face_feature).t()
        for key_name in self.register_table:
            for j in self.register_table[key_name]:
                cosa = torch.matmul(j[0], face_norm)
                # if cosa > 0.9:
                if cosa > self.max_cosa[index]:
                    self.max_cosa[index] = cosa
                    self.key_name[index] = key_name
                    # print(j[1])
                    return key_name, cosa
        return self.key_name[index], self.max_cosa[index]
        # return "陌生人", 0


loss_fn = nn.NLLLoss()

if __name__ == '__main__':

    # 训练过程
    # net = FaceNet().cuda()
    #
    # optimizer = optim.Adam(net.parameters())
    #
    # dataset = MyDataset("face_data")
    # dataloader = DataLoader(dataset=dataset, batch_size=85, shuffle=True)
    #
    # for epoch in range(10000):
    #     for xs, ys in dataloader:
    #         feature, cls = net(xs.cuda())
    #
    #         loss = loss_fn(torch.log(cls), ys.cuda())
    #         optimizer.zero_grad()
    #         loss.backward()
    #         optimizer.step()
    #     # print(torch.argmax(cls, dim=1), ys)
    #     print(str(epoch)+"Loss====>"+str(loss.item()))
    #     if epoch%100==0:
    #         torch.save(net.state_dict(), "params/face.pt")
    #         print(str(epoch)+"参数保存成功")

    # 使用
    net = FaceNet().cuda()
    for i in range(2):
        if i == 0:
            net.load_state_dict(torch.load("param/face.pt"))
        else:
            break
            # net.load_state_dict(torch.load("params/face_3000.pt"))
        net.eval()

        person1 = tf(Image.open("img/img.png").convert("RGB")).cuda()
        person1_feature = net.encode(person1[None, ...])

        person2 = tf(Image.open("register/img_1.png").convert("RGB")).cuda()
        person2_feature = net.encode(person2[None, ...])

        siam = compare(person1_feature, person2_feature)
        print(i, siam)

    # 保存权重
    # net = FaceNet().cuda()
    # net.load_state_dict(torch.load("params/face.pt"))
    # registed_name = ["刘泉", "杨霖萱", "侯捷", "鲁思炜", "钟静"]
    # path = "register"
    # register_table = {}
    # weight_list = []
    # for key_name in os.listdir(path):
    #     name = registed_name[int(key_name)]
    #     registed_feature = []
    #     for img in os.listdir(f"{path}/{key_name}"):
    #         img = Image.open(f"{path}/{key_name}/{img}")
    #         img = tf(img).cuda()
    #         feature = F.normalize(net.encode(img[None, ...]))
    #         registed_feature.append(feature)
    #     register_table[name] = registed_feature
    # torch.save(register_table, "params/weight_face.pt")

    # 调用权重
    # net = FaceNet().cuda()
    # net.load_state_dict(torch.load("params/face.pt"))
    # register_table = torch.load("params/weight_face.pt")
    # person1 = tf(Image.open("register/0/img.png").convert("RGB")).cuda()
    # person1_feature = net.encode(person1[None, ...])
    # print(person1_feature)
    # a = register_table["刘泉"][0]
    # b = register_table["鲁思炜"][0].t()
    # print(torch.matmul(a,b))
    # print(register_table["刘泉"][0])
    # print(type(torch.load("params/weight_face.pt")))

    # 把模型和参数进行打包，以便C++或PYTHON调用
    # x = torch.Tensor(1, 3, 112, 112)
    # traced_script_module = jit.trace(net, x)
    # traced_script_module.save("model.cpt")
