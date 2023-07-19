from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget,QMessageBox
from PySide2.QtCore import QTimer
import sys
sys.path.append("../GUI_pyside2(终版)")
from CloudAPI import COS
from Ui_Forgetpwd import Ui_Forgetpwd

class forgetpwd(Ui_Forgetpwd):
    def __init__(self):
        super(forgetpwd, self).__init__()
        self.setupUi(self)
        self.bind()
        self.COS = COS()
        self.code = ''
        self.confirmregistflag = False
        self.countdown = 60

    def bind(self):
        self.verificationcode.editingFinished.connect(self.checkverificationcode)
        self.getverificationcode.clicked.connect(self.Getverificationcode)
        self.getverificationcode.clicked.connect(self.on_button_clicked)
        self.getverificationcode.clicked.connect(self.update_label)
        self.setnewpwd.editingFinished.connect(self.checkpwd)
        self.phonenumber.editingFinished.connect(self.checkphonenumber)
        self.confirmreset.clicked.connect(self.resetpwd)
        self.backward.clicked.connect(self.backwardlast)
        self.timer.timeout.connect(self.update_label)

    #检测密码输入是否合规
    def checkpwd(self):
        pwd = self.setnewpwd.text()
        if len(pwd) == 0:
            self.lbnewpwd.setText("请输入密码")
            self.lbnewpwd.setStyleSheet("color:red")
        elif len(pwd) < 6 or len(pwd) > 20:
            self.lbnewpwd.setText("密码长度在6-20个字符,请输入符合要求的密码")
            self.lbnewpwd.setStyleSheet("color:red")
        else:
            self.lbnewpwd.setText("")

    #检测输入信息是否正确
    def checkmessage(self):
        phonenumber = self.phonenumber.text()
        pwd = self.setnewpwd.text()
        confirmpwd = self.confirmnewpwd.text()
        verifycode = self.verificationcode.text()
        confirmverifycode = str(self.code)
        if len(phonenumber) != 11 or len(pwd) < 6 or len(pwd) > 20 or len(verifycode) != 6:
            return False
        if pwd == confirmpwd:
            if verifycode == confirmverifycode:
                return True
            else:
                QMessageBox.warning(self, "提示", "验证码或密码错误，请确认一下")
                return False
        else:
            QMessageBox.warning(self,"提示","验证码或密码错误，请确认一下")
            return False

    # 检测手机号输入是否合规
    def checkphonenumber(self):
        phonenumber = self.phonenumber.text()
        if self.COS.judge_database_if_exist(phonenumber):
            self.confirmregistflag = True
            self.lbphonenumber.setText("")
            self.lbphonenumber.setStyleSheet("color:red")
        elif len(phonenumber) == 0:
            self.lbphonenumber.setText("请输入手机号")
            self.lbphonenumber.setStyleSheet("color:red")
        elif len(phonenumber) != 11:
            self.lbphonenumber.setText("请输入有效的手机号")
            self.lbphonenumber.setStyleSheet("color:red")
        else:
            self.confirmregistflag = False
            self.lbphonenumber.setText("该手机号未注册")
            self.lbphonenumber.setStyleSheet("color:red")

    #获取验证码
    def Getverificationcode(self):
        if not self.confirmregistflag:
            return None
        phonenumber = self.phonenumber.text()
        if len(phonenumber) != 11:
            pass
        else:
            phonenumber, self.code = self.COS.send_code(phonenumber)
            return self.code

    #检测验证码输入是否有效
    def checkverificationcode(self):
        verificationcode = self.verificationcode.text()
        if len(verificationcode) == 0:
            self.lbverificationcode.setText("请输入手机短信验证码")
            self.lbverificationcode.setStyleSheet("color:red")
        elif len(verificationcode) != 6:
            self.lbverificationcode.setText("验证码格式错误")
            self.lbverificationcode.setStyleSheet("color:red")
        else:
            self.lbverificationcode.setText("")

    def on_button_clicked(self):
        if self.confirmregistflag:
            if len(self.phonenumber.text()) == 11:
                # 禁用按钮并启动定时器
                self.getverificationcode.setEnabled(False)
                self.timer.start(1000)

    def update_label(self):
        # 更新按钮上的文本
        if self.confirmregistflag:
            if self.countdown > 0:
                self.getverificationcode.setText(f"{self.countdown}s后重新获取验证码")
                self.countdown -= 1
            else:
                self.getverificationcode.setText("获取验证码")
                self.getverificationcode.setEnabled(True)
                self.timer.stop()
                self.countdown = 60

    #重置密码
    def resetpwd(self):
        if self.checkmessage():
        #重置信息
            phonenumber = self.phonenumber.text()
            confirmpwd = self.confirmnewpwd.text()
            self.COS.reset_user_pwd(int(phonenumber), confirmpwd)

            QMessageBox.information(self, "提示", "重置成功！",
                                QMessageBox.StandardButton.Yes)
            # print("密码重置完毕")
            self.clear()
            self.backwardlast()

    def clear(self):
        self.phonenumber.clear()
        self.setnewpwd.clear()
        self.confirmnewpwd.clear()
        self.verificationcode.clear()

    #切换回登录界面
    def backwardlast(self):
        from login import Login
        self.parent = Login()
        self.parent.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ui = forgetpwd()
    ui.show()
    sys.exit(app.exec_())