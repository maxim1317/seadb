# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 448)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QWidget:window {                    /* Borders around the code editor and debug window */\n"
"    border: 0px solid #263238;\n"
"    background-color: #263238;\n"
"}\n"
"\n"
"QToolTip {\n"
"    background-color: #80CBC4;\n"
"    color: black;\n"
"    padding: 5px;\n"
"    border-radius: 0;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* ==================== Dialog ==================== */\n"
"QLabel {\n"
"    background: transparent;\n"
"    color: #CFD8DC;                /* Not sure about this one */\n"
"}\n"
"\n"
"QDialog, QListView {\n"
"    background-color: #263238;\n"
"    color: #546E7A;\n"
"    outline: 0;\n"
"    border: 2px solid transparent;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    color: #AFBDC4;\n"
"    background: transparent;\n"
"}\n"
"\n"
"\n"
"QListView::item:selected {\n"
"    color: #ffffff;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* === QTabBar === */\n"
"QTabBar {\n"
"    background: #263238;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    background: transparent;    /* Only at the very bottom of the tabs */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    border: 0px solid transparent;\n"
"    border-bottom: 2px solid transparent;\n"
"    color: #546E7A;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: transparent;\n"
"    border: 0px solid transparent;\n"
"    border-bottom: 2px solid #80CBC4;\n"
"    color: #AFBDC4;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: transparent;\n"
"    border: 0px solid transparent;\n"
"    border-top: none;\n"
"    border-bottom: 2px solid #80CBC4;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background: #263238;    /* This covers a bunch of things, I was thinking about making it transparent, */\n"
"                            /* but I would have to find all the other elements... but QTabWidget::pane may be it */\n"
"}\n"
"\n"
"\n"
"/* === QGroupBox === */\n"
"QGroupBox {\n"
"    border: 1px solid transparent;\n"
"    margin-top: 1em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #80CBC4;\n"
"    subcontrol-origin: margin;\n"
"    left: 6px;\n"
"    padding: 0 3px 0 3px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: #546E7A;\n"
"    background-color: transparent;\n"
"    selection-background-color: transparent;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{    \n"
"    selection-background-color: transparent;\n"
"    outline: 0;\n"
"}\n"
"\n"
"/* === QCheckBox === */\n"
"QCheckBox, QRadioButton {\n"
"    color: #AFBDC4;\n"
"}\n"
"\n"
"QCheckBox::indicator::unchecked  {\n"
"    background-color: #263238;\n"
"    border: 1px solid #536D79;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    background-color: #263238;\n"
"    border: 1px solid #536D79;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked, QTreeView::indicator::checked {\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #80CBC4, stop:1 #263238);\n"
"    border: 1px solid #536D79;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #80CBC4, stop:1 #263238);\n"
"    border: 1px solid #536D79;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled, QTreeView::indicator:disabled {\n"
"    background-color: #444444;            /* Not sure what this looks like */\n"
"}\n"
"\n"
"QCheckBox::indicator::checked:disabled, QRadioButton::indicator::checked:disabled, QTreeView::indicator::checked:disabled {  \n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #BBBBBB, stop:1 #444444); /* Not sure what this looks like */\n"
"}\n"
"\n"
"QTreeView {\n"
"    background-color: transparent;\n"
"    color: #546E7A;\n"
"    outline: 0;\n"
"    border: 0;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background-color: transparent;\n"
"    color: #AFBDC4;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    background-color: transparent;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QTreeView QHeaderView:section {\n"
"    background-color: #263238;\n"
"    color: #CFD8DC;\n"
"    border: 0;\n"
"}\n"
"\n"
"QTreeView::indicator:checked {\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #80CBC4, stop:1 #263238);\n"
"    border: 1px solid #536D79;\n"
"    selection-background-color: transparent;\n"
"}\n"
"\n"
"QTreeView::indicator:unchecked {            /* This and the one above style the checkbox in the Options -> Keyboard */\n"
"    background-color: #263238;                /* This is still a hover over in blue I can\'t get rid of */\n"
"    border: 1px solid #536D79;\n"
"    selection-background-color: transparent;\n"
"}\n"
"\n"
"/*QTreeView QScrollBar {\n"
"    background-color: #263238\n"
"}*/\n"
"\n"
"QTreeView::branch {\n"
"    /* Skip - applies to everything */\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    /* Skip - files */\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    /* Skip - applies to almost all on the left side */\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    background: url(\'./images/rightarrowgray.png\') center center no-repeat;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed {\n"
"    background: url(\'./images/rightarrowgray.png\') center center no-repeat;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    /* Skip - files */\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"    background: url(\'./images/downarrowgray.png\') center center no-repeat;\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings {\n"
"    background: url(\'./images/downarrowgray.png\') center center no-repeat;\n"
"}\n"
"\n"
"/* === QScrollBar:horizontal === */\n"
"QScrollBar:horizontal {\n"
"    background: #263238;                /* Background where slider is not */\n"
"    height: 10px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #263238;                /* Background where slider is not */\n"
"    width: 10px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #37474F;                    /* Slider color */\n"
"    min-width: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #37474F;                    /* Slider color */\n"
"    min-height: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;                                                /* Removes the dotted background */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {    /* Hides the slider arrows */\n"
"      border: none;\n"
"      background: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #546E7A;\n"
"    border: 1px solid transparent;\n"
"    padding: 4px 22px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #AFBDC4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background: transparent;\n"
"    border: 1px solid transparent;\n"
"    border-top: none;\n"
"    border-bottom: 2px solid #80CBC4;\n"
"    color: #546E7A;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background: transparent;\n"
"    border: 1px solid transparent;\n"
"    color: #546E7A;\n"
"}\n"
"\n"
"/*****************************************************************************\n"
"Main Screen\n"
"*****************************************************************************/\n"
"QTreeView {\n"
"    background-color: #263238;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #263238;        /* File Menu Background color */\n"
"    color: #546E7A;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #AFBDC4;\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: transparent;            /* Could change this to #546E7A and reduce the margin top and bottom to 1px */\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"    margin-top: 5px;\n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"/* === QMenuBar === */\n"
"QMenuBar {\n"
"    background-color: #263238;\n"
"    color: #546E7A;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:disabled {\n"
"    color: gray;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    color: #AFBDC4;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QToolBar {\n"
"    background: #263238;\n"
"    border: 1px solid transparent;\n"
"}\n"
"\n"
"QToolBar:handle {\n"
"    background: transparent;\n"
"    border-left: 2px dotted #80CBC4;    /* Fix the 4 handle dots so it doesn\'t look crappy */\n"
"    color: transparent;\n"
"}\n"
"\n"
"QToolBar::separator {\n"
"    border: 0;\n"
"}\n"
"\n"
"/* === QToolButton === */\n"
"QToolButton:hover, QToolButton:pressed {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"    background: url(\'./images/downarrowgray.png\') center center no-repeat;\n"
"    background-color: #263238;                                                /* This needs to be set to ensure the other brown arrows don\'t show */\n"
"}\n"
"\n"
"QToolButton::menu-button:hover, QToolButton::menu-button:pressed {\n"
"    background-color: #263238;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background-color: #263238;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #546E7A;        /* Text at the bottom right corner of the screen */\n"
"}\n"
"\n"
"QToolButton {    /* I don\'t like how the items depress */\n"
"    color: #546E7A;\n"
"}\n"
"\n"
"QToolButton:hover, QToolButton:pressed, QToolButton:checked {\n"
"    background-color: #263238;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    color: #AFBDC4;\n"
"\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"\n"
"QToolButton {\n"
"    border: 1px solid transparent;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: transparent;                /* I don\'t like how the down arrows in the top menu bar move down when clicked */\n"
"    border: 1px solid transparent;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"    border-left: 1px solid transparent;\n"
"    background: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"    border-left: 1px solid transparent;\n"
"    background: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    color: #546E7A;\n"
"    background-color: #263238;\n"
"}\n"
"\n"
"QAbstractScrollArea  {    /* Borders around the code editor and debug window */\n"
"    border: 0;\n"
"}\n"
"\n"
"/*****************************************************************************\n"
"Play around with these settings\n"
"*****************************************************************************/\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; /* Test this out on OS X, it will affect the tabs in the Options Dialog, on OS X they are centered */\n"
"}")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/icon.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

import images_rc
