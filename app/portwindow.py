from PyQt5 import QtCore, QtGui, QtWidgets
from ut import *


class PortWindow(object):
    def setupUi(self, PortWindow, auth, name, img):
        self.auth = auth
        self.name = name
        self.img  = img

        self.info = get_port_info(auth, name)

        PortWindow.setObjectName("PortWindow")
        PortWindow.resize(1272, 868)
        center(PortWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PortWindow.sizePolicy().hasHeightForWidth())
        PortWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        PortWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PortWindow.setWindowIcon(icon)
        PortWindow.setAutoFillBackground(False)
        PortWindow.setStyleSheet(
            "QWidget:window {                    /* Borders around the code editor and debug window */\n"
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
            "}"
        )
        PortWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(PortWindow)
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

        self.journal_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.journal_table.setFont(font)
        self.journal_table.setWordWrap(True)
        self.journal_table.setObjectName("journal_table")

        self.buildJournal()

        self.verticalLayout_2.addWidget(self.journal_table)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.backHL = QtWidgets.QHBoxLayout()

        self.backPB = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(18)
        self.backPB.setFont(font)
        self.backPB.setText("Back")
        self.backPB.setStyleSheet("color: #D72638;")
        self.backHL.addWidget(self.backPB)

        SI = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.backHL.addItem(SI)

        self.verticalLayout_2.addLayout(self.backHL)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.pn_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pn_label.setFont(font)
        self.pn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pn_label.setObjectName("pn_label")
        self.verticalLayout.addWidget(self.pn_label)

        self.port_view_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.port_view_label.setFont(font)
        self.port_view_label.setText("")
        self.port_view_label.setAlignment(QtCore.Qt.AlignCenter)
        self.port_view_label.setObjectName("port_view_label")
        self.verticalLayout.addWidget(self.port_view_label)

        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setStyleSheet("color: #80CBC4;")
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.label_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setText("<html><head/><body><p><img src='" + self.img + "'/></p></body></html>")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
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
        self.horizontalLayout.addLayout(self.formLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        PortWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PortWindow)
        self.statusbar.setObjectName("statusbar")
        PortWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PortWindow)
        QtCore.QMetaObject.connectSlotsByName(PortWindow)

    def retranslateUi(self, PortWindow):
        _translate = QtCore.QCoreApplication.translate
        PortWindow.setWindowTitle(_translate("PortWindow", self.name + " port"))
        self.label_17.setText(_translate("PortWindow"    , "Journal"))
        self.pn_label.setText(_translate("PortWindow"    , "Port info"))

        self.label.setText(_translate("PortWindow"       , "Name"))
        self.label_3.setText(_translate("PortWindow"     , self.name))

        self.label_2.setText(_translate("PortWindow"     , "Country"))
        self.label_10.setText(_translate("PortWindow"    , self.info["country"]))

        self.label_4.setText(_translate("PortWindow"     , "Location"))
        self.label_11.setText(_translate("PortWindow"    , self.info["location"]))

        self.label_5.setText(_translate("PortWindow"     , "Piers"))
        self.label_12.setText(_translate("PortWindow"    , self.info["piers"]))

        self.label_6.setText(_translate("PortWindow"     , "Last week turnover"))
        self.label_13.setText(_translate("PortWindow"    , str(self.info["turnover"])))

        self.label_7.setText(_translate("PortWindow"     , "Ships in port"))
        self.label_14.setText(_translate("PortWindow"    , str(self.info["ships_in_port"])))

    def buildJournal(self):
        from random import triangular

        self.journal_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.journal_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.journal_table.setFocusPolicy(QtCore.Qt.NoFocus)

        journal = self.info["journal"]

        login, password = self.auth
        client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
        db = client[DB_NAME]

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)

        self.journal_table.setColumnCount(4)
        self.journal_table.setRowCount(len(journal))

        stylesheet = "QTableView{          \
                background: transparent;   \
                background-color: #263238; \
                color: #546E7A;            \
            };                             \
            QHeaderView::section{          \
                background: transparent;   \
                background-color: #263238; \
                color: #80CBC4;            \
                font-size: 12;             \
            }                              \
        "
        self.journal_table.setStyleSheet(stylesheet)

        self.journal_table.verticalHeader().hide()
        header = self.journal_table.horizontalHeader()
        header.setStyleSheet("background-color: #263238; color: #80CBC4;")
        header.setFont(font)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.journal_table.setHorizontalHeaderLabels(["Date", "Ship", "Cargo amount", "Job"])

        font.setPointSize(14)
        for i in range(0, len(journal)):
            ship   = db.ships.find_one({"_id": journal[i]["ship_id"]})

            _date  = QtWidgets.QTableWidgetItem(str(journal[i]["date"].date()))
            _date.setFont(font)
            _ship  = QtWidgets.QTableWidgetItem(ship["name"])
            _ship.setFont(font)
            _job   = QtWidgets.QTableWidgetItem(db.jobs.find_one({"_id": journal[i]["operation"]})["job"])
            if _job.text() == "LOADING":
                _job.setForeground(QtGui.QColor("#53DD6C"))
            if _job.text() == "UNLOADING":
                _job.setForeground(QtGui.QColor("#D72638"))
            _job.setFont(font)

            amnt = ship["cargo_amount"]
            if amnt == 0 and _job.text != "RESTING":
                size_type = ship["size_type_id"]
                amnt = triangular(
                    0,
                    db.sizes.find({"_id": size_type}).limit(1)[0]["max_amount"],
                    db.sizes.find({"_id": size_type}).limit(1)[0]["max_amount"] - 100000.0
                )
            _amnt  = QtWidgets.QTableWidgetItem(str(int(amnt)))
            _amnt.setFont(font)

            self.journal_table.setItem(i, 0, _date)
            self.journal_table.setItem(i, 1, _ship)
            self.journal_table.setItem(i, 2, _amnt)
            self.journal_table.setItem(i, 3, _job )

        return

import images_rc
