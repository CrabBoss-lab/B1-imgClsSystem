# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import needs_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1106, 619)
        icon = QIcon()
        icon.addFile(u":/images/images/title_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionopen_video = QAction(MainWindow)
        self.actionopen_video.setObjectName(u"actionopen_video")
        self.actionopen_capture = QAction(MainWindow)
        self.actionopen_capture.setObjectName(u"actionopen_capture")
        self.actionpredict = QAction(MainWindow)
        self.actionpredict.setObjectName(u"actionpredict")
        self.actionclear = QAction(MainWindow)
        self.actionclear.setObjectName(u"actionclear")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.uploadImgBtn = QPushButton(self.centralwidget)
        self.uploadImgBtn.setObjectName(u"uploadImgBtn")
        self.uploadImgBtn.setGeometry(QRect(10, 20, 71, 41))
        self.capBtn = QPushButton(self.centralwidget)
        self.capBtn.setObjectName(u"capBtn")
        self.capBtn.setGeometry(QRect(10, 160, 71, 41))
        self.predictBtn = QPushButton(self.centralwidget)
        self.predictBtn.setObjectName(u"predictBtn")
        self.predictBtn.setGeometry(QRect(10, 230, 71, 41))
        self.logText = QTextEdit(self.centralwidget)
        self.logText.setObjectName(u"logText")
        self.logText.setGeometry(QRect(130, 520, 771, 61))
        self.clearBtn = QPushButton(self.centralwidget)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setGeometry(QRect(10, 300, 71, 41))
        self.uploadVideoBtn = QPushButton(self.centralwidget)
        self.uploadVideoBtn.setObjectName(u"uploadVideoBtn")
        self.uploadVideoBtn.setGeometry(QRect(10, 90, 71, 41))
        self.restartBtn = QPushButton(self.centralwidget)
        self.restartBtn.setObjectName(u"restartBtn")
        self.restartBtn.setGeometry(QRect(10, 370, 71, 41))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(919, 20, 181, 561))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: 1px solid gray;")

        self.verticalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.modelCbox = QComboBox(self.verticalLayoutWidget)
        self.modelCbox.setObjectName(u"modelCbox")

        self.verticalLayout.addWidget(self.modelCbox)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.thresholdSlider = QSlider(self.verticalLayoutWidget)
        self.thresholdSlider.setObjectName(u"thresholdSlider")
        self.thresholdSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.thresholdSlider)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.delaySlider = QSlider(self.verticalLayoutWidget)
        self.delaySlider.setObjectName(u"delaySlider")
        self.delaySlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.delaySlider)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.CpuradioButton = QRadioButton(self.verticalLayoutWidget)
        self.CpuradioButton.setObjectName(u"CpuradioButton")

        self.verticalLayout.addWidget(self.CpuradioButton)

        self.GpuradioButton = QRadioButton(self.verticalLayoutWidget)
        self.GpuradioButton.setObjectName(u"GpuradioButton")

        self.verticalLayout.addWidget(self.GpuradioButton)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border: 1px solid gray;")

        self.verticalLayout.addWidget(self.label_4)

        self.outText = QPlainTextEdit(self.verticalLayoutWidget)
        self.outText.setObjectName(u"outText")

        self.verticalLayout.addWidget(self.outText)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 20, 771, 491))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.oriLabel = QLabel(self.layoutWidget)
        self.oriLabel.setObjectName(u"oriLabel")

        self.horizontalLayout.addWidget(self.oriLabel)

        self.preLabel = QLabel(self.layoutWidget)
        self.preLabel.setObjectName(u"preLabel")

        self.horizontalLayout.addWidget(self.preLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"基于龙芯平台的图像分类系统", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open image", None))
        self.actionopen_video.setText(QCoreApplication.translate("MainWindow", u"open video", None))
        self.actionopen_capture.setText(QCoreApplication.translate("MainWindow", u"open capture", None))
        self.actionpredict.setText(QCoreApplication.translate("MainWindow", u"predict", None))
        self.actionclear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.uploadImgBtn.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247", None))
        self.capBtn.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6", None))
        self.predictBtn.setText(QCoreApplication.translate("MainWindow", u"\u9884\u6d4b", None))
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.uploadVideoBtn.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891", None))
        self.restartBtn.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u542f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"自定义设置", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"模型", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"阈值", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"延迟(秒)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"设备", None))
        self.CpuradioButton.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.GpuradioButton.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"结果输出", None))
        self.oriLabel.setText("")
        self.preLabel.setText("")
    # retranslateUi

