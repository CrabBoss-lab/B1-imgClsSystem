# -*- codeing = utf-8 -*-
# @Time :2023/4/11 19:20
# @Author :yujunyu
# @Site :
# @File :test.py
# @software: PyCharm

# sum = 0
# for e in range(0 + 1, 200 + 1):
#     sum += 1
#     print(e)
# print(sum)


# import torch
#
# print(torch.cuda.is_available())


import cv2

cap = cv2.VideoCapture(0)    # VideoCapture()中参数是1，表示打开外接usb摄像头
cv2.namedWindow('camera')

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('camera', frame)
        cv2.waitKey(1)
