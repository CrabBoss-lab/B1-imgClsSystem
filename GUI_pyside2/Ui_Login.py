# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import needs_rc

class Ui_Login(QWidget):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(960, 515)
        Login.setMinimumSize(QSize(960, 360))
        icon = QIcon()
        icon.addFile(u":/images/images/title_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        self.setFixedSize(self.width(),self.height())
        self.gridLayout_2 = QGridLayout(Login)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setContextMenuPolicy(Qt.PreventContextMenu)
        self.widget.setStyleSheet(u"border-style: solid;\n"
"border-width: 0.1px;\n"
"border-color: black;")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.editaccount = QLineEdit(self.widget)
        self.editaccount.setObjectName(u"editaccount")

        self.gridLayout.addWidget(self.editaccount, 2, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 2)

        self.Btnforgetpwd = QPushButton(self.widget)
        self.Btnforgetpwd.setObjectName(u"Btnforgetpwd")
        self.Btnforgetpwd.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"	color:blue;\n"
"}")

        self.gridLayout.addWidget(self.Btnforgetpwd, 4, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 1, 2, 2)

        self.Btnregister = QPushButton(self.widget)
        self.Btnregister.setObjectName(u"Btnregister")
        self.Btnregister.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"	color:blue;\n"
"}")

        self.gridLayout.addWidget(self.Btnregister, 8, 2, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 8, 0, 1, 2)

        self.lblogin = QLabel(self.widget)
        self.lblogin.setObjectName(u"lblogin")

        self.gridLayout.addWidget(self.lblogin, 4, 1, 1, 2)

        self.editpassword = QLineEdit(self.widget)
        self.editpassword.setObjectName(u"editpassword")
        self.editpassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.editpassword, 3, 1, 1, 3)

        self.password = QLabel(self.widget)
        self.password.setObjectName(u"password")
        self.password.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.password, 3, 0, 1, 1)

        self.Btnlogin = QPushButton(self.widget)
        self.Btnlogin.setObjectName(u"Btnlogin")
        self.Btnlogin.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color:white;")

        self.gridLayout.addWidget(self.Btnlogin, 7, 0, 1, 4)

        self.account = QLabel(self.widget)
        self.account.setObjectName(u"account")
        self.account.setMinimumSize(QSize(10, 40))
        self.account.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.account, 2, 0, 1, 1)

        self.welcome = QLabel(self.widget)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setStyleSheet(u"font-size:30px")
        self.welcome.setAlignment(Qt.AlignCenter)
        self.welcome.setWordWrap(False)

        self.gridLayout.addWidget(self.welcome, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget, 0, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 2, 1, 1)

        self.imglabel = QLabel(Login)
        self.imglabel.setObjectName(u"imglabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imglabel.sizePolicy().hasHeightForWidth())
        self.imglabel.setSizePolicy(sizePolicy)
        self.imglabel.setPixmap(QPixmap(u"images/image.jpg"))
        self.imglabel.setScaledContents(True)
        self.imglabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.imglabel, 0, 1, 2, 1)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"\u57fa\u4e8e\u9f99\u82af\u5e73\u53f0\u7684\u56fe\u50cf\u5206\u7c7b\u7cfb\u7edf", None))
        self.Btnforgetpwd.setText(QCoreApplication.translate("Login", u"\u5fd8\u8bb0\u5bc6\u7801\uff1f", None))
        self.Btnregister.setText(QCoreApplication.translate("Login", u"\u6ca1\u6709\u8d26\u53f7\uff1f\u7acb\u5373\u6ce8\u518c", None))
        self.lblogin.setText("")
        self.password.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801\uff1a", None))
        self.Btnlogin.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.account.setText(QCoreApplication.translate("Login", u"\u8d26\u53f7\uff1a", None))
        self.welcome.setText(QCoreApplication.translate("Login", u"\u6b22\u8fce\u767b\u5f55", None))
        self.imglabel.setText("")
    # retranslateUi

