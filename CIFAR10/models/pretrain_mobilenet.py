# -*- codeing = utf-8 -*-
# @Time :2023/4/12 17:13
# @Author :yujunyu
# @Site :
# @File :pretrain_mobilenet.py
# @software: PyCharm

"""mobilenet系列预训练模型"""

import torch
from torchvision.models import mobilenet_v3_small
from torchsummary import summary


def mobilenet_v3_small_net():
    net = mobilenet_v3_small(pretrained=True)
    num_ftrs = net.classifier[3].in_features
    net.classifier[3] = torch.nn.Linear(num_ftrs, 10)
    return net


if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = mobilenet_v3_small_net().to(device)
    summary(model=net, input_size=(3, 32, 32))
    print(net)
