# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 672)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        MainWindow.setFont(font)
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 1051, 621))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 190, 1051, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ships_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ships_label.setFont(font)
        self.ships_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ships_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ships_label.setObjectName("ships_label")
        self.verticalLayout.addWidget(self.ships_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        strList = ['Python', 'PyQt5', 'Qt', 'Django', 'QML']
        ships_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        completer = QtWidgets.QCompleter(strList, ships_line_edit)
        ships_line_edit.setCompleter(completer)        # Set QCompleter in the input field
        ships_line_edit.setObjectName("ships_line_edit")
        self.horizontalLayout.addWidget(ships_line_edit)
        self.ships_ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ships_ok.setObjectName("ships_ok")
        self.horizontalLayout.addWidget(self.ships_ok)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab, "")
        self.ports_tab = QtWidgets.QWidget()
        self.ports_tab.setObjectName("ports_tab")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.ports_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 1051, 591))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.ports_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ports_label.setFont(font)
        self.ports_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ports_label.setObjectName("ports_label")
        self.verticalLayout_5.addWidget(self.ports_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.ports_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        self.ports_line_edit.setFont(font)
        self.ports_line_edit.setObjectName("ports_line_edit")
        self.horizontalLayout_3.addWidget(self.ports_line_edit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.ports_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.ports_ok.setObjectName("ports_ok")
        self.horizontalLayout_3.addWidget(self.ports_ok)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setAutoFillBackground(True)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ports_label_top_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
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
        self.verticalLayout_4.addWidget(self.ports_top_10_list)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.ports_tab, "")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ships_label.setText(_translate("MainWindow", "Enter vessel name"))
        self.ships_ok.setText(_translate("MainWindow", "OK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Vessels"))
        self.ports_label.setText(_translate("MainWindow", "Enter port name"))
        self.ports_ok.setText(_translate("MainWindow", "OK"))
        self.ports_label_top_10.setText(_translate("MainWindow", "Busiest ports"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ports_tab), _translate("MainWindow", "Ports"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

