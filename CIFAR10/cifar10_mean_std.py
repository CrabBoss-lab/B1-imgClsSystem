# -*- codeing = utf-8 -*-
# @Time :2023/4/11 9:03
# @Author :yujunyu
# @Site :
# @File :cifar10_mean_std.py
# @software: PyCharm

# https://blog.csdn.net/weixin_43821559/article/details/123459085


import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader


def get_mean_std_value(loader):
    '''
    求数据集的均值和标准差
    :param loader:
    :return:
    '''
    data_sum, data_squared_sum, num_batches = 0, 0, 0

    for data, _ in loader:
        # data: [batch_size,channels,height,width]
        # 计算dim=0,2,3维度的均值和，dim=1为通道数量，不用参与计算
        data_sum += torch.mean(data, dim=[0, 2, 3])  # [batch_size,channels,height,width]
        # 计算dim=0,2,3维度的平方均值和，dim=1为通道数量，不用参与计算
        data_squared_sum += torch.mean(data ** 2, dim=[0, 2, 3])  # [batch_size,channels,height,width]
        # 统计batch的数量
        num_batches += 1
    # 计算均值
    mean = data_sum / num_batches
    # 计算标准差
    std = (data_squared_sum / num_batches - mean ** 2) ** 0.5
    return mean, std


if __name__ == '__main__':
    batch_size = 128

    # 训练集(以CIFAR-10数据集为例)
    train_dataset = datasets.CIFAR10(root='./data', train=True, download=False, transform=transforms.ToTensor())
    train_loader = DataLoader(train_dataset, shuffle=True, batch_size=batch_size)

    mean, std = get_mean_std_value(train_loader)

    print('mean = {},std = {}'.format(mean, std))
    # mean = tensor([0.4914, 0.4822, 0.4465]),std = tensor([0.2470, 0.2435, 0.2616])
