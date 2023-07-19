# -*- codeing = utf-8 -*-
# @Time :2023/4/11 8:50
# @Author :yujunyu
# @Site :
# @File :download_data.py
# @software: PyCharm

import torchvision

# download cifar-10 datasets
train_dataset = torchvision.datasets.CIFAR10('./data', train=True, download=True)
test_dataset = torchvision.datasets.CIFAR10('./data', train=False, download=True)

# print(train_dataset)
# print()
# print(train_dataset[0])
