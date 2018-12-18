# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QMainWindow
import loginwindow as lw
import mainwindow as mw
import vesselwindow as vw
import sys
from ut import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.uiLogin = lw.LoginWindow()
        self.uiMain = mw.MainWindow()
        self.uiVessel = vw.VesselWindow()
        self.startLogin()

    def startMain(self, auth):
        self.uiMain.setupUi(self, auth)
        self.uiMain.ports_ok.clicked.connect(self.checkPort)
        self.uiMain.ships_ok.clicked.connect(self.checkVessel)
        for PB in self.uiMain.topPBs:
            PB.clicked.connect(self.portFromTop)
        self.show()

    def startVessel(self, auth, name):
        self.uiVessel.setupUi(self, auth, name)
        self.uiVessel.backPB.clicked.connect(self.gotoMain)
        self.show

    def startLogin(self):

        self.uiLogin.setupUi(self)
        self.uiLogin.okPB.clicked.connect(self.checkLogin)
        self.show()

    def checkLogin(self):
        # from time import sleep

        self.login = self.uiLogin.loginLE.text()
        self.pwd = self.uiLogin.pwdLE.text()

        if try_login(login=self.login, password=self.pwd):
            self.uiLogin.loginLE.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            self.uiLogin.pwdLE.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            # sleep(1)
            self.startMain(auth=(self.login, self.pwd))
        else:
            self.uiLogin.loginLE.setStyleSheet("border-bottom: 2px solid #D72638;")
            self.uiLogin.pwdLE.setStyleSheet("border-bottom: 2px solid #D72638;")

    def checkPort(self):
        import abbreviate
        p_name = self.uiMain.ports_line_edit.text()
        print('Port name: ' + abbreviate.Abbreviate(self.uiMain.ports_line_edit.text()))
        if p_name not in self.uiMain.port_list:
            self.uiMain.ports_line_edit.setStyleSheet("border-bottom: 2px solid #D72638;")
        else:
            self.uiMain.ports_line_edit.setStyleSheet("border-bottom: 2px solid #53DD6C;")

    def checkVessel(self):
        p_name = self.uiMain.ships_line_edit.text()
        print('ship name: ' + self.uiMain.ships_line_edit.text())
        if p_name not in self.uiMain.ship_list:
            self.uiMain.ships_line_edit.setStyleSheet("border-bottom: 2px solid #D72638;")
        else:
            self.uiMain.ships_line_edit.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            self.startVessel(auth=(self.login, self.pwd), name=self.uiMain.ships_line_edit.text())

    def gotoMain(self):
        self.startMain(auth=(self.login, self.pwd))

    def portFromTop(self):
        print('Port name: ' + self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

