from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Signal
from qt_material import apply_stylesheet
import sys
sys.path.append("../GUI_pyside2(终版)")
from CloudAPI import COS
from regist import regist
from forgetpwd import forgetpwd
from Ui_Login import Ui_Login
from main import MainWindow
class Login(Ui_Login):
    signal = Signal(str)
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.bind()
        self.COS = COS()

    def bind(self):
        self.Btnlogin.clicked.connect(self.login)
        self.Btnregister.clicked.connect(self.register)
        self.Btnforgetpwd.clicked.connect(self.forgetpwd)


    def login(self):
        if self.COS.judge_database_if_exist(self.editaccount.text()):
            pwd = self.editpassword.text()
            df = self.COS.read_user_from_dataset()
            confirmpwd = str(df.loc[df['phoneNumber'] == int(self.editaccount.text()), 'password'].values[0])
            if pwd == confirmpwd:
                self.lblogin.setText("欢迎您,{}".format(self.editaccount.text()))
                QMessageBox.information(self, "提示", "登录成功！",
                                        QMessageBox.StandardButton.Yes)
                # 切换到主窗口
                self.mainwindow = MainWindow()
                self.mainwindow.show()
                self.close()
            else:
                self.lblogin.setText("账号或密码错误")
                self.lblogin.setStyleSheet("color:red;")
        else:
            self.lblogin.setText("账号或密码错误")
            self.lblogin.setStyleSheet("color:red;")
    def register(self):
        #切换到注册窗口
        self.regist = regist()
        self.regist.show()
        self.close()

    def forgetpwd(self):
        #切换到忘记密码窗口
        self.forgetpwdwd = forgetpwd()
        self.forgetpwdwd.show()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
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
    apply_stylesheet(app, theme='light_cyan_500.xml')
    ui = Login()
    ui.show()
    sys.exit(app.exec_())