# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Forgetpwd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import needs_rc

class Ui_Forgetpwd(QWidget):
    def setupUi(self, Forgetpwd):
        if not Forgetpwd.objectName():
            Forgetpwd.setObjectName(u"Forgetpwd")
        self.timer = QTimer()
        Forgetpwd.resize(509, 316)
        icon = QIcon()
        icon.addFile(u":/images/images/title_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Forgetpwd.setWindowIcon(icon)
        self.setFixedSize(self.width(),self.height())
        self.verticalLayout = QVBoxLayout(Forgetpwd)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.widget = QWidget(Forgetpwd)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbphonenumber = QLabel(self.widget)
        self.lbphonenumber.setObjectName(u"lbphonenumber")

        self.gridLayout.addWidget(self.lbphonenumber, 1, 1, 1, 3)

        self.backward = QPushButton(self.widget)
        self.backward.setObjectName(u"backward")

        self.gridLayout.addWidget(self.backward, 9, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.confirmnewpwd = QLineEdit(self.widget)
        self.confirmnewpwd.setObjectName(u"confirmnewpwd")
        self.confirmnewpwd.setEchoMode(QLineEdit.Password)
        self.gridLayout.addWidget(self.confirmnewpwd, 6, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 4, 1, 1)

        self.verificationcode = QLineEdit(self.widget)
        self.verificationcode.setObjectName(u"verificationcode")

        self.gridLayout.addWidget(self.verificationcode, 2, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 2, 1, 1)

        self.lbnewpwd = QLabel(self.widget)
        self.lbnewpwd.setObjectName(u"lbnewpwd")

        self.gridLayout.addWidget(self.lbnewpwd, 5, 1, 1, 3)

        self.lbverificationcode = QLabel(self.widget)
        self.lbverificationcode.setObjectName(u"lbverificationcode")

        self.gridLayout.addWidget(self.lbverificationcode, 3, 1, 1, 3)

        self.confirmreset = QPushButton(self.widget)
        self.confirmreset.setObjectName(u"confirmreset")
        self.confirmreset.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color:white;")

        self.gridLayout.addWidget(self.confirmreset, 9, 3, 1, 1)

        self.phonenumber = QLineEdit(self.widget)
        self.phonenumber.setObjectName(u"phonenumber")

        self.gridLayout.addWidget(self.phonenumber, 0, 1, 1, 3)

        self.getverificationcode = QPushButton(self.widget)
        self.getverificationcode.setObjectName(u"getverificationcode")

        self.gridLayout.addWidget(self.getverificationcode, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 9, 2, 1, 1)

        self.setnewpwd = QLineEdit(self.widget)
        self.setnewpwd.setObjectName(u"setnewpwd")
        self.setnewpwd.setEchoMode(QLineEdit.Password)
        self.gridLayout.addWidget(self.setnewpwd, 4, 1, 1, 3)

        self.lbconfirmpwd = QLabel(self.widget)
        self.lbconfirmpwd.setObjectName(u"lbconfirmpwd")

        self.gridLayout.addWidget(self.lbconfirmpwd, 7, 1, 1, 3)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Forgetpwd)

        QMetaObject.connectSlotsByName(Forgetpwd)
    # setupUi

    def retranslateUi(self, Forgetpwd):
        Forgetpwd.setWindowTitle(QCoreApplication.translate("Forgetpwd", u"\u5fd8\u8bb0\u5bc6\u7801", None))
        self.lbphonenumber.setText("")
        self.backward.setText(QCoreApplication.translate("Forgetpwd", u"\u53d6\u6d88", None))
        self.confirmnewpwd.setText("")
        self.confirmnewpwd.setPlaceholderText(QCoreApplication.translate("Forgetpwd", u"\u8bf7\u518d\u6b21\u8f93\u5165\u65b0\u5bc6\u7801", None))
        self.verificationcode.setText("")
        self.verificationcode.setPlaceholderText(QCoreApplication.translate("Forgetpwd", u"\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801", None))
        self.lbnewpwd.setText("")
        self.lbverificationcode.setText("")
        self.confirmreset.setText(QCoreApplication.translate("Forgetpwd", u"\u91cd\u7f6e", None))
        self.phonenumber.setPlaceholderText(QCoreApplication.translate("Forgetpwd", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7", None))
        self.getverificationcode.setText(QCoreApplication.translate("Forgetpwd", u"\u83b7\u53d6\u9a8c\u8bc1\u7801", None))
        self.setnewpwd.setText("")
        self.setnewpwd.setPlaceholderText(QCoreApplication.translate("Forgetpwd", u"\u8bf7\u8f93\u5165\u65b0\u5bc6\u7801", None))
        self.lbconfirmpwd.setText("")
    # retranslateUi

