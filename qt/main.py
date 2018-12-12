# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QMainWindow
import loginwindow as lw
import mainwindow as mw
import sys
from ut import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiLogin = lw.LoginWindow()
        self.uiMain = mw.MainWindow()
        self.startLogin()

    def startMain(self, auth):
        self.uiMain.setupUi(self, auth)
        self.show()

    def startLogin(self):

        self.uiLogin.setupUi(self)
        self.uiLogin.okPB.clicked.connect(self.checkLogin)
        self.show()

    def checkLogin(self):
        from time import sleep

        login = self.uiLogin.loginLE.text()
        pwd = self.uiLogin.pwdLE.text()

        if try_login(login=login, password=pwd):
            self.uiLogin.loginLE.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            self.uiLogin.pwdLE.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            # sleep(1)
            self.startMain(auth=(login, pwd))
        else:
            self.uiLogin.loginLE.setStyleSheet("border-bottom: 2px solid #D72638;")
            self.uiLogin.pwdLE.setStyleSheet("border-bottom: 2px solid #D72638;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

