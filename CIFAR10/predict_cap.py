# -*- codeing = utf-8 -*-
# @Time :2023/4/13 19:16
# @Author :yujunyu
# @Site :
# @File :predict_cap.py
# @software: PyCharm

import torch
from torchvision import transforms
from PIL import Image
import numpy as np
import os
import time
import cv2

from models import cifar10_net, pretrain_resnet


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


def prob_viz(res, classes, input_frame):
    pass


if __name__ == '__main__':
    # 网络结构
    net = cifar10_net.cifar10_net()
    # 模型权重
    model = 'checkpoints/cifar10_net_e100.pth'
    recognizer = Predict(net, model)

    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.4914, 0.4821, 0.4465), std=(0.2470, 0.2435, 0.2616))
    ])

    classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    threshold = 0.3

    cap = cv2.VideoCapture(0)
    pTime = 0
    while cap.isOpened():
        ret, frame = cap.read()
        img = Image.fromarray(np.uint8(frame))
        img = transform(img)
        res = recognizer.recognize(img)
        # print(res)
        # print(res[0], res[1])
        label = classes[res[0]]
        probability = res[1].numpy()[0]
        print('{} {:.2%}'.format(label, probability))

        if probability >= threshold:
            # 可视化
            # cv2.putText(frame, text=f'cls:{label} p:{probability}', org=(0, 50),
            #             fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=(0, 255, 0), thickness=2)
            #
            colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245), (25, 202, 173), (140, 199, 181),
                      (160, 238, 225), (190, 231, 233), (190, 237, 199), (214, 213, 183), (209, 186, 116)]

            # cv2.rectangle(frame, pt1=(0, 0), pt2=(int(res[1].numpy()[0] * 100), 30), color=colors[res[0]], thickness=-1)
            cv2.putText(img=frame, text=classes[res[0]] + ' {:.2f}'.format(res[1].numpy()[0]), org=(0, 29),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, color=colors[res[0]], thickness=2, lineType=cv2.LINE_AA)

        # FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(frame, f'fps: {int(fps)}', (0, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (120, 117, 255), 2, cv2.LINE_AA)

        cv2.putText(frame, 'exit: esc', (0, 90), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (120, 117, 255), 2, cv2.LINE_AA)

        cv2.imshow("CIFAR10", frame)

        time.sleep(0.005)

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
