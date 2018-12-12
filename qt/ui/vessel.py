# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vessel.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1272, 868)
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
        font = QtGui.QFont()
        font.setPointSize(18)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 1211, 783))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_17 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.listWidget.setFont(font)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ship_name_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ship_name_label.setFont(font)
        self.ship_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ship_name_label.setObjectName("ship_name_label")
        self.verticalLayout.addWidget(self.ship_name_label)
        self.ship_view_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ship_view_label.setFont(font)
        self.ship_view_label.setText("")
        self.ship_view_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ship_view_label.setObjectName("ship_view_label")
        self.verticalLayout.addWidget(self.ship_view_label)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_2.setSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_11)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_12)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_13)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_15)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_16)
        self.horizontalLayout.addLayout(self.formLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_17.setText(_translate("MainWindow", "Journal"))
        self.listWidget.setSortingEnabled(False)
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_3.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))
        self.ship_name_label.setText(_translate("MainWindow", "Vessel"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "somename"))
        self.label_2.setText(_translate("MainWindow", "Home port"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "Flag"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "Class"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Cargo"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Avg. speed"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "Load"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "Current status"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))

import images_rc
