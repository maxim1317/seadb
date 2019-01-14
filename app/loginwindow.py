# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow as mw
from style import *
from ut import *


class LoginWindow(QtWidgets.QWidget):

    def setupUi(self, LoginWindow):

        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(680, 448)
        center(LoginWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        LoginWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setAutoFillBackground(False)

        self.theme = Theme(dark=False)
        self.style = Style().style
        LoginWindow.setStyleSheet(self.style)

        LoginWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 621, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.loginLE = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.loginLE.setFont(font)
        self.loginLE.setObjectName("loginLE")
        self.verticalLayout_2.addWidget(self.loginLE)
        self.pwdLE = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pwdLE.setFont(font)
        self.pwdLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdLE.setObjectName("pwdLE")
        self.verticalLayout_2.addWidget(self.pwdLE)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.okPB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loginLE.returnPressed.connect(self.okPB.click)
        self.pwdLE.returnPressed.connect(self.okPB.click)
        # self.okPB.clicked.connect(self.ok_call)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.okPB.setFont(font)
        self.okPB.setObjectName("okPB")
        self.horizontalLayout.addWidget(self.okPB)

        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Log in"))
        self.label_4.setText(_translate("LoginWindow", "<html><head/><body><p><img src=\"./images/icon.png\"/></p></body></html>"))
        self.label_2.setText(_translate("LoginWindow", "Login"))
        self.label_3.setText(_translate("LoginWindow", "Password"))
        self.okPB.setText(_translate("LoginWindow", "OK"))

    def ok_call(self):
        from time import sleep

        login = self.loginLE.text().lower()
        # print('Login: ' + login)
        pwd = self.pwdLE.text()
        # print('Password: ' + pwd)

        # login_list = get_login_list()
        # print(try_login(login=login, password=pwd))

        if try_login(login=login, password=pwd):
            self.loginLE.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            self.pwdLE.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            sleep(0.5)
            MainWindow = QtWidgets.QMainWindow()
            ui = mw.Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            self.close()
        else:
            self.loginLE.setStyleSheet("border-bottom: 2px solid #D72638;")
            self.pwdLE.setStyleSheet("border-bottom: 2px solid #D72638;")
