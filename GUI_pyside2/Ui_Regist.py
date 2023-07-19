# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_Regist.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import needs_rc

class Ui_Register(QWidget):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        self.timer = QTimer()
        Register.resize(584, 346)
        icon = QIcon()
        icon.addFile(u":/images/images/title_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Register.setWindowIcon(icon)
        self.setFixedSize(self.width(),self.height())
        self.gridLayout_2 = QGridLayout(Register)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.widget = QWidget(Register)
        self.widget.setObjectName(u"widget")
        self.widget.setContextMenuPolicy(Qt.NoContextMenu)
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbcheckpwd = QLabel(self.widget)
        self.lbcheckpwd.setObjectName(u"lbcheckpwd")

        self.gridLayout.addWidget(self.lbcheckpwd, 7, 0, 1, 3)

        self.lbcheckconfirmpwd = QLabel(self.widget)
        self.lbcheckconfirmpwd.setObjectName(u"lbcheckconfirmpwd")

        self.gridLayout.addWidget(self.lbcheckconfirmpwd, 10, 0, 1, 1)

        self.lbcheckaccount = QLabel(self.widget)
        self.lbcheckaccount.setObjectName(u"lbcheckaccount")

        self.gridLayout.addWidget(self.lbcheckaccount, 1, 0, 1, 1)

        self.lbcheckverificationcode = QLabel(self.widget)
        self.lbcheckverificationcode.setObjectName(u"lbcheckverificationcode")

        self.gridLayout.addWidget(self.lbcheckverificationcode, 5, 0, 1, 3)

        self.confirmregist = QPushButton(self.widget)
        self.confirmregist.setObjectName(u"confirmregist")
        self.confirmregist.setStyleSheet(u"background-color: rgb(0, 0, 255);\n"
"color:white;")

        self.gridLayout.addWidget(self.confirmregist, 14, 2, 1, 1)

        self.confirmpwd = QLineEdit(self.widget)
        self.confirmpwd.setObjectName(u"confirmpwd")
        self.confirmpwd.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.confirmpwd, 8, 0, 1, 3)

        self.Btncancel = QPushButton(self.widget)
        self.Btncancel.setObjectName(u"Btncancel")
        self.Btncancel.setStyleSheet(u"")

        self.gridLayout.addWidget(self.Btncancel, 14, 0, 1, 1)

        self.getverificationcode = QPushButton(self.widget)
        self.getverificationcode.setObjectName(u"getverificationcode")

        self.gridLayout.addWidget(self.getverificationcode, 4, 2, 1, 1)

        self.setpwd = QLineEdit(self.widget)
        self.setpwd.setObjectName(u"setpwd")
        self.setpwd.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.setpwd, 6, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 14, 1, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 2)

        self.setphonenumber = QLineEdit(self.widget)
        self.setphonenumber.setObjectName(u"setphonenumber")

        self.gridLayout.addWidget(self.setphonenumber, 2, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 10, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 3)

        self.lbconfirmpwd = QLabel(self.widget)
        self.lbconfirmpwd.setObjectName(u"lbconfirmpwd")

        self.gridLayout.addWidget(self.lbconfirmpwd, 9, 0, 1, 3)

        self.lbcheckphonenumber = QLabel(self.widget)
        self.lbcheckphonenumber.setObjectName(u"lbcheckphonenumber")

        self.gridLayout.addWidget(self.lbcheckphonenumber, 3, 0, 1, 3)


        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"\u6ce8\u518c\u8d26\u53f7", None))
        self.lbcheckpwd.setText("")
        self.lbcheckconfirmpwd.setText("")
        self.lbcheckaccount.setText("")
        self.lbcheckverificationcode.setText("")
        self.confirmregist.setText(QCoreApplication.translate("Register", u"\u6ce8\u518c", None))
        self.confirmpwd.setText("")
        self.confirmpwd.setPlaceholderText(QCoreApplication.translate("Register", u"\u8bf7\u518d\u6b21\u8bbe\u7f6e\u767b\u5f55\u5bc6\u7801", None))
        self.Btncancel.setText(QCoreApplication.translate("Register", u"\u53d6\u6d88", None))
        self.getverificationcode.setText(QCoreApplication.translate("Register", u"\u83b7\u53d6\u9a8c\u8bc1\u7801", None))
        self.setpwd.setText("")
        self.setpwd.setPlaceholderText(QCoreApplication.translate("Register", u"\u8bf7\u8bbe\u7f6e\u767b\u5f55\u5bc6\u7801", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801", None))
        self.setphonenumber.setText("")
        self.setphonenumber.setPlaceholderText(QCoreApplication.translate("Register", u"\u8bf7\u8f93\u5165\u624b\u673a\u53f7", None))
        self.lbconfirmpwd.setText("")
        self.lbcheckphonenumber.setText("")
    # retranslateUi

