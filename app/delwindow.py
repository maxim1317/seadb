from PyQt5 import QtCore, QtGui, QtWidgets
from ut import *


class DelWindow(object):
    def setupUi(self, DelWindow, auth, name):

        self.auth = auth

        login, password = auth
        client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
        db = client[DB_NAME]

        self.db = db

        DelWindow.setObjectName("DelWindow")
        DelWindow.resize(647, 349)

        center(DelWindow)

        self.ship  = db.ships.find_one({"name": name})
        self.tasks = list(db.tasks.find({"ship_id": self.ship["_id"]}))
        self.task_str = [i["name"] for i in self.tasks]

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DelWindow.sizePolicy().hasHeightForWidth())
        DelWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        DelWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DelWindow.setWindowIcon(icon)
        DelWindow.setAutoFillBackground(False)

        self.theme = Theme(dark=False)
        self.style = Style().style
        DelWindow.setStyleSheet(self.style)

        DelWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(DelWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 29, 570, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(self.task_str)

        self.verticalLayout.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        DelWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DelWindow)
        self.statusbar.setObjectName("statusbar")
        DelWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DelWindow)
        QtCore.QMetaObject.connectSlotsByName(DelWindow)

    def retranslateUi(self, DelWindow):
        _translate = QtCore.QCoreApplication.translate
        DelWindow.setWindowTitle(_translate("DelWindow", "DelWindow"))
        self.label.setText(_translate("DelWindow", "Choose a task to delete"))
        self.pushButton_2.setText(_translate("DelWindow", "Cancel"))
        self.pushButton.setText(_translate("DelWindow", "Delete"))
