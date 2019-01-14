from PyQt5 import QtCore, QtGui, QtWidgets

from style import *
from ut import *


class MainWindow(object):

    def setupUi(self, MainWindow, auth):
        self.auth = auth
        login, _  = auth
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 672)
        center(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)

        self.theme = Theme(dark=False)
        self.style = Style().style
        MainWindow.setStyleSheet(self.style)

        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1051, 621))
        font = QtGui.QFont()
        font.setPointSize(18)

        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")

        #######################################
        ############## tab ##############
        #######################################

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 190, 1051, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.ships_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.font = QtGui.QFont()
        self.font.setPointSize(18)
        # font.setBold(True)

        self.ships_label.setFont(self.font)
        # self.ships_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ships_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ships_label.setObjectName("ships_label")
        self.verticalLayout.addWidget(self.ships_label)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.ship_list = get_ship_list(auth=auth)
        self.ships_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ships_line_edit.setFont(font)
        completer = QtWidgets.QCompleter(self.ship_list, self.ships_line_edit)
        self.ships_line_edit.setCompleter(completer)        # Set QCompleter in the input field
        self.ships_line_edit.setFocus()
        self.ships_line_edit.setObjectName("ships_line_edit")
        self.horizontalLayout.addWidget(self.ships_line_edit)

        self.ships_ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ships_line_edit.returnPressed.connect(self.ships_ok.click)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ships_ok.setFont(font)
        self.ships_ok.setObjectName("ships_ok")
        self.horizontalLayout.addWidget(self.ships_ok)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        #######################################
        ############## ports_tab ##############
        #######################################

        self.tabWidget.addTab(self.tab, "")
        self.ports_tab = QtWidgets.QWidget()
        self.ports_tab.setObjectName("ports_tab")

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.ports_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 1051, 591))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem5)
        spacerLabel = QtWidgets.QLabel()
        self.horizontalLayout_2.addWidget(spacerLabel)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.ports_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ports_label.setFont(font)
        self.ports_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ports_label.setObjectName("ports_label")
        self.verticalLayout_5.addWidget(self.ports_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem7)

        self.port_list = get_port_list(auth=auth)
        self.ports_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ports_line_edit.setFont(font)
        completer = QtWidgets.QCompleter(self.port_list, self.ports_line_edit)
        self.ports_line_edit.setCompleter(completer)        # Set QCompleter in the input field
        self.ports_line_edit.setObjectName("self.ports_line_edit")
        self.horizontalLayout_3.addWidget(self.ports_line_edit)

        # spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem8)

        self.ports_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ports_line_edit.returnPressed.connect(self.ports_ok.click)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ports_ok.setFont(font)
        self.ports_ok.setObjectName("ports_ok")
        self.horizontalLayout_3.addWidget(self.ports_ok)

        # spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        # spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem11)
        self.horizontalLayout_2.addWidget(spacerLabel)

        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setAutoFillBackground(False)
        # self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setStyleSheet("color: " + self.theme.accent + ";")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.ports_label_top_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)

        self.ports_label_top_10.setFont(font)
        self.ports_label_top_10.setAlignment(QtCore.Qt.AlignCenter)
        self.ports_label_top_10.setObjectName("ports_label_top_10")
        self.verticalLayout_4.addWidget(self.ports_label_top_10)

        self.ports_top_10_list = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.ports_top_10_list.setLineWidth(-7)
        self.ports_top_10_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ports_top_10_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ports_top_10_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.ports_top_10_list.setAutoScroll(False)
        self.ports_top_10_list.setAutoScrollMargin(21)
        self.ports_top_10_list.setObjectName("ports_top_10_list")

        self.add_top_10()

        self.verticalLayout_4.addWidget(self.ports_top_10_list)

        # spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout_4.addItem(spacerItem12)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.ports_tab, "")

        if login not in ["admin", "oberon", "manager"]:
            self.tabWidget.setTabEnabled(1, False)
            # self.tab.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.ports_top_10_list.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "alpha 0.6"))
        self.ships_label.setText(_translate("MainWindow", "Enter vessel name"))
        self.ships_ok.setText(_translate("MainWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Vessels"))
        self.ports_label.setText(_translate("MainWindow", "Enter port name"))
        self.ports_ok.setText(_translate("MainWindow", "OK"))
        self.ports_label_top_10.setText(_translate("MainWindow", "Busiest ports"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ports_tab), _translate("MainWindow", "Ports"))

    def add_top_10(self):

        font = QtGui.QFont()
        font.setPointSize(14)

        self.topPBs = []

        it = []
        wd = []
        hl = []
        pb = []
        lb = []

        for i in range(0, 10):
            it.append(QtWidgets.QListWidgetItem())
            wd.append(QtWidgets.QWidget())
            hl.append(QtWidgets.QHBoxLayout())
            pb.append(QtWidgets.QPushButton())
            lb.append(QtWidgets.QLabel())

        top_10 = get_top_10(auth=self.auth)

        for i in range(0, 10):
            pb[i].setFont(font)
            lb[i].setFont(font)

            pb[i].setText(top_10[i]["name"])
            self.topPBs.append(pb[i])
            lb[i].setText(top_10[i]["amount"])
            sp = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

            hl[i].addWidget(pb[i])
            hl[i].addItem(sp)
            hl[i].addWidget(lb[i])
            # hl[i].addStretch()

            wd[i].setLayout(hl[i])
            it[i].setSizeHint(wd[i].sizeHint())

            self.ports_top_10_list.addItem(it[i])
            self.ports_top_10_list.setItemWidget(it[i], wd[i])

        # for pb in self.topPBs:
        #     print(pb.text())

        return
