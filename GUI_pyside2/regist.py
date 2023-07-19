import time
import pandas as pd
from PySide2.QtWidgets import QWidget,QApplication,QMessageBox
import sys
sys.path.append("../GUI_pyside2(终版)")
from CloudAPI import COS
from Ui_Regist import Ui_Register

class regist(Ui_Register):
    def __init__(self):
        super(Ui_Register, self).__init__()
        self.setupUi(self)
        self.bind()
        self.COS = COS()
        self.code = ''
        self.confirmregistflag = False
        self.countdown = 60

    def bind(self):
        self.setphonenumber.editingFinished.connect(self.checkphonenumber)
        self.lineEdit.editingFinished.connect(self.checkverificationcode)
        self.getverificationcode.clicked.connect(self.Getverificationcode)
        self.setpwd.editingFinished.connect(self.checkpwd)
        self.confirmpwd.editingFinished.connect(self.checkconfirmpwd)
        self.confirmregist.clicked.connect(self.register)
        self.Btncancel.clicked.connect(self.change2login)
        self.getverificationcode.clicked.connect(self.on_button_clicked)
        self.timer.timeout.connect(self.update_label)
    #检测手机号输入是否合规
    def checkphonenumber(self):
        phonenumber = self.setphonenumber.text()
        if self.COS.judge_database_if_exist(phonenumber):
            self.confirmregistflag = True
            self.lbcheckphonenumber.setText("该手机号已被注册")
            self.lbcheckphonenumber.setStyleSheet("color:red")
        elif len(phonenumber) == 0:
            self.lbcheckphonenumber.setText("请输入手机号")
            self.lbcheckphonenumber.setStyleSheet("color:red")
        elif len(phonenumber) != 11:
            self.lbcheckphonenumber.setText("请输入有效的手机号")
            self.lbcheckphonenumber.setStyleSheet("color:red")
        else:
            self.confirmregistflag = False
            self.lbcheckphonenumber.setText("")

    #检测验证码输入是否有效
    def checkverificationcode(self):
        verificationcode = self.lineEdit.text()
        if len(verificationcode) == 0:
            self.lbcheckverificationcode.setText("请输入手机短信验证码")
            self.lbcheckverificationcode.setStyleSheet("color:red")
        elif len(verificationcode) != 6:
            self.lbcheckverificationcode.setText("验证码格式错误")
            self.lbcheckverificationcode.setStyleSheet("color:red")
        else:
            self.lbcheckverificationcode.setText("")

    #检测密码输入是否合规
    def checkpwd(self):
        pwd = self.setpwd.text()
        if len(pwd) == 0:
            self.lbcheckpwd.setText("请输入密码")
            self.lbcheckpwd.setStyleSheet("color:red")
        elif len(pwd) < 6 or len(pwd) > 20:
            self.lbcheckpwd.setText("密码长度在6-20个字符,请输入符合要求的密码")
            self.lbcheckpwd.setStyleSheet("color:red")
        else:
            self.lbcheckpwd.setText("")
    #检测确认密码输入是否正确
    def checkconfirmpwd(self):
        confirm = self.confirmpwd.text()
        if len(confirm) == 0:
            self.lbcheckconfirmpwd.setText("请再次输入密码")
            self.lbcheckconfirmpwd.setStyleSheet("color:red")
        else:
            self.lbcheckconfirmpwd.setText("")

    #检测输入信息是否正确
    def checkmessage(self):
        phonenumber = self.setphonenumber.text()
        pwd = self.setpwd.text()
        confirmpwd = self.confirmpwd.text()
        verifycode = self.lineEdit.text()
        confirmverifycode = str(self.code)
        if len(phonenumber) != 11 or len(pwd) < 6 or len(pwd) > 20 or len(verifycode) != 6 or self.confirmregistflag == True:
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

    #获取验证码
    def Getverificationcode(self):
        if self.confirmregistflag:
            return None
        phonenumber = self.setphonenumber.text()
        if len(phonenumber) != 11:
            pass
        else:
            phonenumber, self.code = self.COS.send_code(phonenumber)
            return self.code


    def on_button_clicked(self):
        if not self.confirmregistflag:
            if len(self.setphonenumber.text()) == 11:
                # 禁用按钮并启动定时器
                self.getverificationcode.setEnabled(False)
                self.timer.start(1000)

    def update_label(self):
        # 更新按钮上的文本
        if self.countdown > 0:
            self.getverificationcode.setText(f"{self.countdown}s后重新获取验证码")
            self.countdown -= 1
        else:
            self.getverificationcode.setText("获取验证码")
            self.getverificationcode.setEnabled(True)
            self.timer.stop()
            self.countdown = 30

    #注册
    def register(self):
        if self.checkmessage():
            #注册
            user_name = self.setphonenumber.text()
            pwd = self.confirmpwd.text()
            self.COS.create_user_database(user_name)
            self.COS.write_user_to_dataset(pd.DataFrame({"phoneNumber": [user_name], "password": [pwd]}))
            self.clear()
            QMessageBox.information(self, "提示", "注册成功",
                                    QMessageBox.StandardButton.Yes)
            self.change2login()
        else:
            QMessageBox.warning(self, "提示", "请检查一下输入的信息")

    #切换回登录界面
    def change2login(self):
        from login import Login
        self.parent = Login()
        self.parent.show()
        self.close()

    def clear(self):
        self.setphonenumber.clear()
        self.setpwd.clear()
        self.confirmpwd.clear()
        self.lineEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = regist()
    ui.show()
    sys.exit(app.exec_())