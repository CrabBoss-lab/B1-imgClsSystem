# -*- codeing = utf-8 -*-
# @Time :2023/4/11 9:26
# @Author :yujunyu
# @Site :
# @File :cnn_net.py
# @software: PyCharm

import torch
from torch import nn
from torchsummary import summary


class cifar10_net(nn.Module):
    def __init__(self):
        super(cifar10_net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, stride=1, padding=2)
        self.maxpool1 = nn.MaxPool2d(kernel_size=2)

        self.conv2 = nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, stride=1, padding=2)
        self.maxpool2 = nn.MaxPool2d(kernel_size=2)

        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, stride=1, padding=2)
        self.maxpool3 = nn.MaxPool2d(kernel_size=2)

        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(1024, 64)
        self.linear2 = nn.Linear(64, 10)
        # self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.conv1(x)
        x = torch.nn.functional.relu(x)
        x = self.maxpool1(x)

        x = self.conv2(x)
        x = torch.nn.functional.relu(x)
        x = self.maxpool2(x)

        x = self.conv3(x)
        x = torch.nn.functional.relu(x)
        x = self.maxpool3(x)

        x = self.flatten(x)
        x = self.linear1(x)
        x = torch.nn.functional.relu(x)

        x = torch.nn.functional.dropout(x, p=0.5, training=self.training)


        x = self.linear2(x)
        # x = self.softmax(x)

        return x


if __name__ == '__main__':
    # 打印网络结构
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = cifar10_net().to(device)
    summary(model=net, input_size=(3, 32, 32))

    print(net)

    # 模拟输入输出
    x = torch.randn(1, 3, 32, 32)
    net = cifar10_net()
    y = net(x)
    print(y)
    pre = torch.nn.functional.softmax(y, 1)
    print(pre)
    # 10类对应的概率
    # tensor([[ 0.1539,  0.0251, -0.0499, -0.0770,  0.0322,  0.0069,  0.0025, -0.0355,
    #          -0.0230, -0.0166]], grad_fn=<AddmmBackward0>)
    # tensor([[0.1162, 0.1022, 0.0948, 0.0922, 0.1029, 0.1003, 0.0999, 0.0962, 0.0974,
    #          0.0980]], grad_fn=<SoftmaxBackward0>)
