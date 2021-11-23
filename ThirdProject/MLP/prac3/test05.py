# 全局取消证书验证 参考：https://blog.csdn.net/mouday/article/details/86441234
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from torchvision import datasets,transforms

train_data = datasets.CIFAR10("E:\data\CIFAR10_data",train=True,transform=transforms.ToTensor(),download=True)
test_data = datasets.CIFAR10("E:\data\CIFAR10_data",train=False,transform=transforms.ToTensor(),download=True)

print(train_data)
print(test_data)
print(train_data.data.shape)
print(train_data.targets)
print(train_data.data[3].shape)
print(train_data.targets[3])
print(type(train_data.classes))
print(train_data.classes)
print(train_data.class_to_idx)

unloader = transforms.ToPILImage()
img = unloader(train_data.data[3])
img.show()
