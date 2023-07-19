# -*- codeing = utf-8 -*-
# @Time :2023/4/11 14:19
# @Author :yujunyu
# @Site :
# @File :pretrain_resnet.py
# @software: PyCharm

"""resnet系列预训练模型"""
import torch
from torchvision.models import resnet18, resnet34, resnet50, resnet101
from torchsummary import summary


def resnet_18():
    net = resnet18(pretrained=True)
    fc_features = net.fc.in_features
    net.fc = torch.nn.Linear(in_features=fc_features, out_features=10)

    return net


def resnet_34():
    net = resnet34(pretrained=True)
    fc_features = net.fc.in_features
    net.fc = torch.nn.Linear(in_features=fc_features, out_features=10)

    return net


def resnet_50():
    net = resnet50(pretrained=True)
    fc_features = net.fc.in_features
    net.fc = torch.nn.Linear(in_features=fc_features, out_features=10)

    return net


def resnet_101():
    net = resnet101(pretrained=True)
    fc_features = net.fc.in_features
    net.fc = torch.nn.Linear(in_features=fc_features, out_features=10)

    return net


if __name__ == '__main__':
    # resnet18
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = resnet_50().to(device)
    summary(model=net, input_size=(3, 32, 32))
    print(net)
