# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtask.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 880)
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
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 30, 1281, 801))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.load_img = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.load_img.setAlignment(QtCore.Qt.AlignCenter)
        self.load_img.setObjectName("load_img")
        self.verticalLayout.addWidget(self.load_img)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.load_from = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_from.setFont(font)
        self.load_from.setObjectName("load_from")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.load_from)
        self.load_from_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_from_edit.setFont(font)
        self.load_from_edit.setObjectName("load_from_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.load_from_edit)
        self.load_to = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_to.setFont(font)
        self.load_to.setObjectName("load_to")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.load_to)
        self.load_to_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_to_edit.setFont(font)
        self.load_to_edit.setObjectName("load_to_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.load_to_edit)
        self.load_starts = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_starts.setFont(font)
        self.load_starts.setObjectName("load_starts")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.load_starts)
        self.load_starts_edit = QtWidgets.QDateEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_starts_edit.setFont(font)
        self.load_starts_edit.setObjectName("load_starts_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.load_starts_edit)
        self.load_ends = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_ends.setFont(font)
        self.load_ends.setObjectName("load_ends")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.load_ends)
        self.load_ends_edit = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_ends_edit.setFont(font)
        self.load_ends_edit.setObjectName("load_ends_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.load_ends_edit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.unload_from = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_from.setFont(font)
        self.unload_from.setObjectName("unload_from")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.unload_from)
        self.unload_from_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_from_edit.setFont(font)
        self.unload_from_edit.setObjectName("unload_from_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.unload_from_edit)
        self.unload_to = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_to.setFont(font)
        self.unload_to.setObjectName("unload_to")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.unload_to)
        self.unload_to_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_to_edit.setFont(font)
        self.unload_to_edit.setObjectName("unload_to_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.unload_to_edit)
        self.unload_starts = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_starts.setFont(font)
        self.unload_starts.setObjectName("unload_starts")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.unload_starts)
        self.unload_ends = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_ends.setFont(font)
        self.unload_ends.setObjectName("unload_ends")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.unload_ends)
        self.unload_starts_edit = QtWidgets.QDateEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_starts_edit.setFont(font)
        self.unload_starts_edit.setObjectName("unload_starts_edit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.unload_starts_edit)
        self.unload_ends_edit = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_ends_edit.setFont(font)
        self.unload_ends_edit.setObjectName("unload_ends_edit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.unload_ends_edit)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.horizontalLayout_3.addLayout(self.formLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.horizontalLayout_3.addLayout(self.formLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backPB = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.backPB.setFont(font)
        self.backPB.setObjectName("backPB")
        self.horizontalLayout_2.addWidget(self.backPB)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.savePB = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.savePB.setFont(font)
        self.savePB.setObjectName("savePB")
        self.horizontalLayout_2.addWidget(self.savePB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Create your task"))
        self.label.setText(_translate("MainWindow", "Load"))
        self.load_img.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/icon.png\"/></p></body></html>"))
        self.load_from.setText(_translate("MainWindow", "From"))
        self.load_to.setText(_translate("MainWindow", "To"))
        self.load_starts.setText(_translate("MainWindow", "Starts on"))
        self.load_ends.setText(_translate("MainWindow", "Ends on"))
        self.load_ends_edit.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.label_2.setText(_translate("MainWindow", "Unload"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/icon.png\"/></p></body></html>"))
        self.unload_from.setText(_translate("MainWindow", "From"))
        self.unload_to.setText(_translate("MainWindow", "To"))
        self.unload_starts.setText(_translate("MainWindow", "Starts on"))
        self.unload_ends.setText(_translate("MainWindow", "Ends on"))
        self.unload_ends_edit.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "OK"))
        self.label_9.setText(_translate("MainWindow", "Voyage Plan"))
        self.label_4.setText(_translate("MainWindow", "Ship will visit"))
        self.label_6.setText(_translate("MainWindow", "0 ports"))
        self.label_7.setText(_translate("MainWindow", "The task will take"))
        self.label_8.setText(_translate("MainWindow", "0 days"))
        self.backPB.setText(_translate("MainWindow", "Cancel"))
        self.savePB.setText(_translate("MainWindow", "Save"))

import images_rc
