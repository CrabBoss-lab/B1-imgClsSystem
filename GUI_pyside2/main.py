# 导入依赖包
import os

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2 import QtCore, QtGui
import sys
import torch
from torch import nn
from torchvision import transforms
import cv2
import numpy as np
from PIL import Image
import time
import random

from qt_material import apply_stylesheet

from Ui_Main import Ui_MainWindow

class cifar10_net(nn.Module):
    def __init__(self):
        super(cifar10_net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5, stride=1, padding=2)
        self.maxpool1 = nn.MaxPool2d(kernel_size=2)

        self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=5, stride=1, padding=2)
        self.maxpool2 = nn.MaxPool2d(kernel_size=2)

        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=5, stride=1, padding=2)
        self.maxpool3 = nn.MaxPool2d(kernel_size=2)

        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(2048, 512)
        self.linear2 = nn.Linear(512, 10)
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
        x = torch.nn.functional.dropout(x, p=0.25, training=self.training)



        x = self.flatten(x)
        x = self.linear1(x)
        x = torch.nn.functional.relu(x)

        x = torch.nn.functional.dropout(x, p=0.25, training=self.training)


        x = self.linear2(x)
        # x = self.softmax(x)

        return x


class Predict():
    def __init__(self, net, model, device):
        super(Predict, self).__init__()
        self.model = model
        self.CUDA = torch.cuda.is_available()
        self.net = net

        self.device = device
        if self.device == 'cuda':
            self.net.cuda()
        state = torch.load(self.model, map_location=self.device)
        self.net.load_state_dict(state)
        # print('模型加载完成！')
        self.net.eval()

    @torch.no_grad()
    def recognize(self, img):
        with torch.no_grad():
            if self.device == 'cuda':
                img = img.cuda()
            img = img.view(-1, 3, 32, 32)  # 等于reshape
            y = self.net(img)
            p_y = torch.nn.functional.softmax(y, dim=1)
            # print(p_y)
            p, cls_index = torch.max(p_y, dim=1)
            return cls_index.cpu(), p.cpu()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.signal = Signal()
        # 加载页面
        self.setupUi(self)

        # 设置lineEdit的只读状态
        self.logText.setReadOnly(True)
        self.outText.setReadOnly(True)

        # 设置窗口不能缩放
        self.setFixedSize(self.width(), self.height())

        # 状态栏设置信息
        self.statusBar().showMessage('By:CabbageStudio{}Version:1.0'.format(' '*282))

        # 设置按钮提示
        self.uploadImgBtn.setToolTip('上传图片文件')
        self.uploadVideoBtn.setToolTip('上传视频文件')
        self.capBtn.setToolTip('接入摄像头')
        self.predictBtn.setToolTip('开始预测')
        self.clearBtn.setToolTip('清空所有')
        self.restartBtn.setToolTip('重启CIFAR10-GUI程序')

        # 设置Label的边框样式
        self.oriLabel.setStyleSheet(
            'QLabel {border: 1px solid gray;}'
        )
        self.preLabel.setStyleSheet(
            'QLabel {border: 1px solid gray;}'
        )
        # 设置按钮样式
        for i in [self.uploadImgBtn, self.uploadVideoBtn, self.capBtn, self.predictBtn, self.clearBtn]:
            i.setStyleSheet(
                # 圆角按钮
                'QPushButton {border-radius: 5px;}'
            )

        # 设置thresholdSlider滑动条的取值范围
        self.thresholdSlider.setMinimum(0)
        self.thresholdSlider.setMaximum(100)
        # 设置delaySlider滑动条的取值范围
        self.delaySlider.setMinimum(0)
        self.delaySlider.setMaximum(100)

        # 设置默认选中CpuradioButton按钮
        self.CpuradioButton.setChecked(True)

        # 设置modelCbox的选项
        self.net_list = ['cifar10_net', 'resnet18']
        self.modelCbox.addItems(self.net_list)
        self.current_net = self.net_list[0]

        # 初始化文件路径
        self.filepath = ''

        # 初始化推理设备
        self.device = 'cpu'

        # 优化1：预先加载模型并执行第一次预测
        # 原因：第一次预测耗时约2~3s，经预先处理后之后的预测耗时仅约0.002~0.003s
        net = cifar10_net()
        model = './pytorch/model.pth'
        self.recognizer = Predict(net, model, self.device)
        self.predict_img('./pytorch/cat.png')

        # 绑定信号与槽
        self.uploadImgBtn.clicked.connect(self.upload_img)
        self.uploadVideoBtn.clicked.connect(self.upload_video)
        self.capBtn.clicked.connect(self.capture)
        self.predictBtn.clicked.connect(self.predict)
        self.clearBtn.clicked.connect(self.clear)
        self.restartBtn.clicked.connect(self.restart)
        self.thresholdSlider.valueChanged.connect(self.threshold_change)
        self.delaySlider.valueChanged.connect(self.delay_change)
        self.CpuradioButton.clicked.connect(self.change_cpu)
        self.GpuradioButton.clicked.connect(self.change_gpu)
        self.modelCbox.currentIndexChanged.connect(self.change_model)

        # 初始化摄像头
        self.cap = None
        self.pTime = 0

        # 初始化定时器
        self.oriTimer = QTimer(self)
        self.preTimer = QTimer(self)
        self.capTimer = QTimer(self)

        # 初始化threshold、delay
        self.threshold = 0.0
        self.delay = 0.0

    # 预测图片
    def predict_img(self, img):
        """
        功能：预测单张图片
        :param img:待预测图片
        :return:推理时间，预测类别，预测概率
        """
        transform = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize(mean=(0.4914, 0.4821, 0.4465), std=(0.2470, 0.2435, 0.2616))
        ])

        classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        image = Image.open(img)
        image = Image.fromarray(np.uint8(image))
        image = transform(image)
        start_time = time.time()
        index, prob = self.recognizer.recognize(image)
        # print('推理时间:{}'.format(time.time() - start_time))
        # print('预测类别:{} 概率:{:.2%}'.format(classes[index], prob.numpy()[0]))

        return time.time() - start_time, index, classes[index], prob.numpy()[0]

    def predict_video(self):
        transform = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
            transforms.Normalize(mean=(0.4914, 0.4821, 0.4465), std=(0.2470, 0.2435, 0.2616))
        ])

        classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        # threshold = 0.3

        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # 预测
                img = Image.fromarray(np.uint8(frame))
                img = transform(img)
                res = self.recognizer.recognize(img)
                # print(res)
                # print(res[0], res[1])
                label = classes[res[0]]
                probability = res[1].numpy()[0]
                # print('{} {:.2%}'.format(label, probability))

                if probability >= self.threshold:
                    # 可视化
                    colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245), (25, 202, 173), (140, 199, 181),
                              (160, 238, 225), (190, 231, 233), (190, 237, 199), (214, 213, 183), (209, 186, 116)]
                    # cls
                    cv2.putText(img=frame, text='cls:{}'.format(classes[res[0]]), org=(0, 100),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=1.5, color=colors[res[0]], thickness=2, lineType=cv2.LINE_AA)
                    # # prob
                    cv2.putText(img=frame, text='prob:{:.2%}'.format(res[1].numpy()[0]), org=(0, 150),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                fontScale=1.5, color=colors[res[0]], thickness=2, lineType=cv2.LINE_AA)

                # FPS
                cTime = time.time()
                fps = 1 / (cTime - self.pTime)
                self.pTime = cTime
                # cv2.putText(frame, f'fps: {int(fps)}', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (120, 117, 255), 2, cv2.LINE_AA)

                # 0~1
                # time.sleep(0)
                time.sleep(self.delay)

                # 将 OpenCV 图像转换为 QImage
                image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()

                # 将 QImage 显示在 QLabel 中
                self.preLabel.setPixmap(QPixmap.fromImage(image).scaled(383, 431, Qt.KeepAspectRatio))

                # 将 fps、预测类别、预测概率显示在 logText 中
                self.outText.setPlainText(
                    'fps:{}\n预测类别:{}\n预测概率:{:.2%}\n{}\n设置信息:\n模型:{}\n阈值:{}\n延迟:{}\n设备:{}'.format(
                        int(fps), label, probability, '-' * 20, self.current_net, self.threshold, self.delay, self.device))

    # 读取文件
    def readFile(self, filename):
        self.img_src = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), 1)
        # self.img_src = cv2.imread(filename)
        h, w, c = self.img_src.shape
        return h, w, c, self.img_src

    # 显示图像
    def images_show(self, h, w, c, data, Label):
        image = QImage(data, w, h, c * w, QImage.Format_RGB888)
        pix = QPixmap.fromImage(image)
        # 获取QLabel的大小
        width = self.oriLabel.width()
        height = self.oriLabel.height()
        # print(width, height)
        # 383 431
        # 等比例放缩图片
        scaledPixmap = pix.scaled(width, height, Qt.KeepAspectRatio)
        Label.setPixmap(scaledPixmap)

    def update_frame(self):
        if self.cap is not None and self.cap.isOpened():
            ret, frame = self.cap.read()

            if ret:
                # 将 OpenCV 图像转换为 QImage
                image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888).rgbSwapped()

                # 将 QImage 显示在 QLabel 中
                self.oriLabel.setPixmap(QPixmap.fromImage(image).scaled(383, 431, Qt.KeepAspectRatio))

    # 上传图片按钮-槽
    def upload_img(self):
        # print('uploadImgBtn被点击了!')
        image_format = ['jpg', 'png', 'bmp', 'jpeg', 'tif', 'tiff', 'gif', 'ico']
        file_dialog = QFileDialog(self, "选择图片文件", "", "图片(*.jpg *.png *.bmp *.jpeg *.tif *.tiff *.gif *.ico)")
        file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        if file_dialog.exec_() == QFileDialog.Accepted:
            self.filepath = file_dialog.selectedFiles()[0]
            if not self.filepath:
                QMessageBox.information(self, "提示", "请加载需要识别的图片！", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            else:
                ext = self.filepath.split(".")[-1]
                if ext.lower() not in image_format:
                    QMessageBox.information(self, "提示", "请加载正确的图片！", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                else:
                    self.preLabel.clear()
                    self.logText.setText("文件位置:" + self.filepath)
                    data = self.readFile(self.filepath)
                    img_data = data[3]
                    img_data = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)
                    h, w, c = img_data.shape
                    self.images_show(h, w, c, img_data.tobytes(), self.oriLabel)


    # 上传视频按钮-槽
    def upload_video(self):
        # print('uploadVideoBtn被点击了!')
        video_format = ['avi', 'mp4', 'mov', 'mkv']
        file_dialog = QFileDialog(self, "选择视频文件", "", "视频(*.avi *.mp4 *.mov *.mkv)")
        file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        if file_dialog.exec_() == QFileDialog.Accepted:
            self.filepath = file_dialog.selectedFiles()[0]
            if not self.filepath:
                QMessageBox.information(self, "提示", "请加载需要识别的视频！", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            else:
                ext = self.filepath.split(".")[-1]
                if ext.lower() not in video_format:
                    QMessageBox.information(self, "提示", "请加载正确的视频！", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                else:
                    self.preLabel.clear()
                    self.logText.setText("文件位置:" + self.filepath)
                    self.cap = cv2.VideoCapture(self.filepath)


                    # Convert the frame to a QImage and display it in the GUI
                    ret, frame = self.cap.read()
                    if ret:
                        height, width, channel = frame.shape
                        bytesPerLine = 3 * width
                        qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                        self.oriLabel.setPixmap(QPixmap.fromImage(qImg).scaled(383, 431, Qt.KeepAspectRatio))

                    # Create a timer to control the video playback
                    self.oriTimer.timeout.connect(self.update_frame)
                    self.oriTimer.stop()

    # 摄像头按钮-槽
    def capture(self):
        # print('capBtn被点击了!')
        self.filepath = '0'
        self.logText.setText(f"接入实时摄像头...\n文件位置:{self.filepath}")
        self.preLabel.clear()
        # ip摄像头
        # self.cap=cv2.VideoCapture('http://admin:admin@10.41.0.206:8081')
        # 笔记本内置摄像头
        self.cap = cv2.VideoCapture(0)
        self.capTimer.timeout.connect(self.update_frame)

        self.capTimer.start(30)

    # 预测按钮-槽
    def predict(self):
        # print('predictBtn被点击了!')
        filepath = (self.filepath)
        if filepath == '':
            QMessageBox.information(self, "提示", "请加载需要识别的图片！", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        elif filepath.split('/')[-1].split('.')[-1] in ['jpg', 'png', 'bmp', 'jpeg', 'tif', 'tiff', 'gif', 'ico']:
            # print('预测图片')
            preTime, cls, preCls, preProb = self.predict_img(filepath)

            self.outText.setPlainText('\n推理时间:{}\n预测类别:{}\n预测概率:{:.2%}'.format(preTime, preCls, preProb))

            data = self.readFile(self.filepath)
            img_data = data[3]
            img_data = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)
            colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245), (25, 202, 173), (140, 199, 181),
                      (160, 238, 225), (190, 231, 233), (190, 237, 199), (214, 213, 183), (209, 186, 116)]
            cv2.putText(img=img_data, text=preCls + ' {:.2f}'.format(preProb), org=(0, 29),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1, color=colors[cls], thickness=2, lineType=cv2.LINE_AA)
            h, w, c = img_data.shape
            self.images_show(h, w, c, img_data.tobytes(), self.preLabel)
        elif filepath.split('/')[-1].split('.')[-1] in ['mp4', 'mov', 'mkv']:
            # print('预测视频')
            self.oriTimer.start(30)
            self.preTimer.timeout.connect(self.predict_video)
            self.preTimer.start(30)
        elif filepath == '0':
            # print('预测实时摄像头')
            self.capTimer.timeout.connect(self.predict_video)
            self.capTimer.start(30)
        else:
            QMessageBox.information(self, "提示", "请加载需要识别的图片！", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    # 改变模型按钮-槽
    def change_model(self, value):
        # print('选择模型下拉框,{}'.format(self.net_list[value]))
        self.current_net = self.net_list[value]

    # 阈值滑动条-槽
    def threshold_change(self, value):
        # print(f'thresholdSilder被移动了,值为{value * 0.01}!')
        self.threshold = value * 0.01

    # delay滑动条-槽
    def delay_change(self, value):
        # print(f'delaySilder被移动了,值为{value * 0.01}')
        self.delay = value * 0.01

    # gpu按钮-槽
    def change_gpu(self):
        # print('选中gpu')
        if torch.cuda.is_available():
            self.device = 'gpu'
        else:
            self.device = 'cpu'

    # cpu按钮-槽
    def change_cpu(self):
        # print('选中cpu')
        self.device = 'cpu'

    # 清空按钮-槽
    def clear(self):
        # print('clearBtn被点击了!')
        self.logText.clear()
        self.oriLabel.clear()
        self.preLabel.clear()
        self.filepath = ''
        for _ in [self.oriTimer, self.preTimer, self.capTimer]:
            _.stop()
        try:
            self.cap.release()
        except:
            pass
        self.cap = None
        self.outText.clear()

    # 重启按钮-槽
    def restart(self):
        # print('restartBtn被点击了!')
        windows = MainWindow()
        windows.show()
        self.close()
        # program = QtCore.QCoreApplication.applicationFilePath()
        # arguments = QtCore.QCoreApplication.arguments()

        # 重启应用程序
        # QtCore.QProcess.startDetached(program, arguments)
        # QApplication.quit()

    def closeEvent(self, event):
        event.accept()



if __name__ == '__main__':

    app = QApplication([])
    theme_list = ['dark_amber.xml',
                  'dark_blue.xml',
                  'dark_cyan.xml',
                  'dark_lightgreen.xml',
                  'dark_pink.xml',
                  'dark_purple.xml',
                  'dark_red.xml',
                  'dark_teal.xml',
                  'dark_yellow.xml',
                  'light_amber.xml',
                  'light_blue.xml',
                  'light_cyan.xml',
                  'light_cyan_500.xml',
                  'light_lightgreen.xml',
                  'light_pink.xml',
                  'light_purple.xml',
                  'light_red.xml',
                  'light_teal.xml',
                  'light_yellow.xml']
    # apply_stylesheet(app, theme=random.choice(theme_list))
    apply_stylesheet(app, theme='dark_cyan.xml')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
