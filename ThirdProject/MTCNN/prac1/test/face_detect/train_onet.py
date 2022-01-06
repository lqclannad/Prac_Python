# O网络训练

import nets
import train

if __name__ == '__main__':
    net = nets.ONet()

    trainer = train.Trainer(net, 'param/onet.pt', 'param/olnet.pt', r"H:\img\48") # 网络，保存参数，训练数据；创建训器
    trainer.train()                                                     # 调用训练器中的train方法
