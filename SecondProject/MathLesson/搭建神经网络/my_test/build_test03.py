# _*_ coding:utf-8 _*_
# 我的名字: Administrator-LQ
# 创建时间: 2021/10/29 22:52
# 文件名称: build_test03.py
# 开发工具: Pycharm
# 参考: https://blog.csdn.net/weixin_38468077/article/details/106592690
# 卷积神经网络(Convolutional Neural Network,CNN)是一种具有局部连接、权重共享等特征的深层前馈神经网络。
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import torch
from torch import nn
from torch.autograd import Variable
from torch.utils import data as Data
from matplotlib import pyplot as plt
import torchvision

# Hyper prameters
EPOCH = 1
BATCH_SIZE = 50
LR = 0.001
DOWNLOAD_MNIST = False

train_data = torchvision.datasets.MNIST(
    root='./mnist',
    train=True,
    transform=torchvision.transforms.ToTensor(),
    download=DOWNLOAD_MNIST
)

# 显示图片5 - 是从MNIST网站获取的数据集
# print(train_data.data.size())
# print(train_data.targets.size())
# plt.imshow(train_data.data[0].numpy(), cmap='gray')
# plt.title('%i' % train_data.targets[0])
# plt.show()

train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)

test_data = torchvision.datasets.MNIST(
    root='./mnist',
    train=False,
)
with torch.no_grad():
    test_x = Variable(torch.unsqueeze(test_data.data, dim=1)).type(torch.FloatTensor)[:2000]/255
    test_y = test_data.targets[:2000]

'''开始建立CNN网络'''
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        '''
        卷积网络一般包括以下内容:
            1、卷积层
            2、神经网络
            3、池化层
        '''
        self.conv1 = nn.Sequential(
            nn.Conv2d(              # -->(1,28,28)
                in_channels=1,      # 传入的图片是几层的，灰色为1层，RGB为三层
                out_channels=16,    # 输出的图片是几层
                kernel_size=5,      # 代表扫描的区域点为5*5
                stride=1,           # 每隔多少步跳一下
                padding=2,          # 边框补全，其计算公式=(kernel_size-1)/2=(5-1)/2=2
            ),   # 2d代表二维卷积      -->(16,28,28)
            nn.ReLU(),              # 激活
            nn.MaxPool2d(kernel_size=2),    # 设定这里的扫描区域为2*2，且取出该2*2中的最大值
        )

        self.conv2 = nn.Sequential(
            nn.Conv2d(              # -->(16,14,14)
                in_channels=16,     # 这里的输入是上层大多输出为16层
                out_channels=32,    # 在这里我们需要将其输出为32层
                kernel_size=5,      # 代表扫描的区域点为5*5
                stride=1,           # 每隔多少步跳一下
                padding=2,          # 边框补全，其计算公式=(kernel_size-1)/2=(5-1)/2=
            ),                      # -->(32,14,14)
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),    # 设定这里的扫描区域为2*2，且取出该2*2中的最大值
        )

        self.out = nn.Linear(32*7*7, 10)    # 这里的数据是二维数据

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)   # (batch,32,7,7)
        # 接下来进行扩展展平的操作，将三维数据转为二维的数据
        x = x.view(x.size(0), -1)   # (batch, 32*7*7)
        output = self.out(x)
        return output

cnn=CNN()
# print(cnn)

# 添加优化方法
optimizer = torch.optim.Adam(cnn.parameters(), lr=LR)
# 指定损失函数使用交叉信息熵
loss_fn = nn.CrossEntropyLoss()

'''训练模型'''
step = 0
for epoch in range(EPOCH):
    # 加载训练数据
    for step, data in enumerate(train_loader):
        x, y = data
        # 分别得到训练数据的x和y的取值
        b_x = Variable(x)
        b_y = Variable(y)

        output = cnn(b_x)           # 调用模型预测
        loss = loss_fn(output, b_y) # 计算损失值
        optimizer.zero_grad()       # 每次循环之前，将梯度清零
        loss.backward()             # 反向传播
        optimizer.step()            # 梯度下降

        # 每执行50次，输出一下当前epoch、loss、accuracy
        if (step%50==0):
            # 计算一下模型预测正确率
            test_output = cnn(test_x)
            y_pred = torch.max(test_output, 1)[1].data.squeeze()
            accuracy=sum(y_pred==test_y).item()/test_y.size(0)

            print('now epoch : ', epoch, '  |   loss : %.4f ' % loss.item(), '  |   accuracy :  ', accuracy)

'''
打印十个测试集的结果
'''
test_output=cnn(test_x[:10])
y_pred=torch.max(test_output,1)[1].data.squeeze()       #选取最大可能的数值所在的位置
print(y_pred.tolist(),'predecton Result')
print(test_y[:10].tolist(),'Real Result')
