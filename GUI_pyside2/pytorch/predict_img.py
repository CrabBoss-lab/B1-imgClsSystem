# -*- codeing = utf-8 -*-
# @Time :2023/4/11 20:02
# @Author :yujunyu
# @Site :
# @File :predict1.py
# @software: PyCharm

import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import time

import cifar10_net_02


class Predict():
    def __init__(self, net, model):
        super(Predict, self).__init__()
        self.model = model
        self.CUDA = torch.cuda.is_available()
        self.net = net
        if self.CUDA:
            self.net.cuda()
            device = 'cuda'
        else:
            device = 'cpu'
        state = torch.load(self.model, map_location=device)
        self.net.load_state_dict(state)
        print('模型加载完成！')
        self.net.eval()

    @torch.no_grad()
    def recognize(self, img):
        with torch.no_grad():
            if self.CUDA:
                img = img.cuda()
            img = img.view(-1, 3, 32, 32)  # 等于reshape
            y = self.net(img)
            p_y = torch.nn.functional.softmax(y, dim=1)
            # print(p_y)
            p, cls_index = torch.max(p_y, dim=1)
            return cls_index.cpu(), p.cpu()


if __name__ == '__main__':
    # 网络结构
    net = cifar10_net_02.cifar10_net()
    # 模型权重
    model = 'model.pth'
    recognizer = Predict(net, model)

    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.4914, 0.4821, 0.4465), std=(0.2470, 0.2435, 0.2616))
    ])

    classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    # 预测单张图片
    img_file = 'cat.png'
    print(f'预测单张图片:{img_file}')
    img = Image.open(img_file)
    img = Image.fromarray(np.uint8(img))
    img = transform(img)
    # img = torch.reshape(img, (1, 3, 32, 32))
    st = time.time()
    cls, p = recognizer.recognize(img)
    print(f'推理时间:{time.time() - st}')
    print('{} {:.2%}'.format(classes[cls], p.numpy()[0]))

    # 预测多张图片
    # folder_path = './testimages'
    # files = os.listdir(folder_path)
    # # 得到每个img文件地址
    # images_files = [os.path.join(folder_path, f) for f in files]
    # for img in images_files:
    #     true_label = img.split('\\')[-1].split('.')[0]
    #     # print(img,true_label)
    #     image = Image.open(img)
    #     image = Image.fromarray(np.uint8(image))
    #     image = transform(image)
    #     st = time.time()
    #     cls, p = recognizer.recognize(image)
    #     print(f'time:{time.time() - st}\t真实标签:{true_label}\t 预测标签:{classes[cls]}\t 预测概率:{p.numpy()[0]}')
