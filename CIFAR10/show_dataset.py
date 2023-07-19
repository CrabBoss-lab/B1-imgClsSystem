# -*- codeing = utf-8 -*-
# @Time :2023/4/12 8:46
# @Author :yujunyu
# @Site :
# @File :show_dataset.py
# @software: PyCharm

import torchvision
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np


def Load_data(batch_size, num_workers):
    '''
    加载数据，并对数据集进行数据增强，，封装成批处理的迭代器
    :param batch_size:
    :param num_workers:
    :return:
    '''
    # 训练集数据增强
    transform_train = transforms.Compose([
        # transforms.RandomCrop(32, padding=4),
        # transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        # CIFAR10数据集的均值和标准差为： mean = tensor([0.4914, 0.4821, 0.4465]), std = tensor([0.2470, 0.2435, 0.2616])
        # transforms.Normalize(mean=(0.4914, 0.4821, 0.4465), std=(0.2470, 0.2435, 0.2616))
    ])
    # 测试集不处理
    transform_test = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        # transforms.Normalize(mean=(0.4914, 0.4821, 0.4465), std=(0.2470, 0.2435, 0.2616))
    ])

    # 加载数据
    train_data = datasets.CIFAR10('./datasets', train=True, transform=transform_train, download=False)
    test_data = datasets.CIFAR10('./datasets', train=False, transform=transform_test, download=False)

    # 封装批处理的迭代器
    train_loader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    test_loader = DataLoader(dataset=test_data, batch_size=batch_size, shuffle=False, num_workers=num_workers)

    return train_loader, test_loader


if __name__ == '__main__':
    # 测试
    train_loader, test_loader = Load_data(batch_size=32, num_workers=0)


    # 按batch_size可视化
    def imshow(img):
        # img = img / 2 + 0.5  # unnormalize
        img = img.numpy().transpose(1, 2, 0)
        plt.imshow(img)
        # plt.savefig('random_train_image')
        plt.show()


    # 获取随机数据
    dataiter = iter(test_loader)
    images, labels = dataiter.next()
    # print(images, labels)

    # 展示图像
    imshow(torchvision.utils.make_grid(images))
