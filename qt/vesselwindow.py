from PyQt5 import QtCore, QtGui, QtWidgets
from ut import *


class VesselWindow(object):
    def setupUi(self, VesselWindow, auth, name):
        self.auth = auth
        self.name = name

        self.info = get_vessel_info(auth, name)

        VesselWindow.setObjectName("VesselWindow")
        VesselWindow.resize(1272, 868)
        center(VesselWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VesselWindow.sizePolicy().hasHeightForWidth())
        VesselWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        VesselWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        VesselWindow.setWindowIcon(icon)
        VesselWindow.setAutoFillBackground(False)
        VesselWindow.setStyleSheet(
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
        VesselWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(VesselWindow)
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

        self.journal_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.journal_label.setFont(font)
        self.journal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.journal_label.setObjectName("journal_label")
        self.verticalLayout_2.addWidget(self.journal_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.journal_list = QtWidgets.Qjournal_list(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.journal_list.setFont(font)
        self.journal_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.journal_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.journal_list.setWordWrap(True)
        self.journal_list.setObjectName("journal_list")

        self.buildJournal()

        self.verticalLayout_2.addWidget(self.journal_list)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.okPB = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.okPB.setFont(font)
        self.okPB.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.okPB)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.addPB = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.addPB.setFont(font)
        self.addPB.setObjectName("addPB")
        self.horizontalLayout_3.addWidget(self.addPB)
        self.delPB = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.delPB.setFont(font)
        self.delPB.setObjectName("delPB")
        self.horizontalLayout_3.addWidget(self.delPB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

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
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.setLineWidth(2)
        self.line.setStyleSheet("color: #80CBC4;")
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
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.formLayout_2.setSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.vs_name_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_name_label.setFont(font)
        self.vs_name_label.setObjectName("vs_name_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vs_name_label)
        self.vs_name_field = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_name_field.setFont(font)
        self.vs_name_field.setObjectName("vs_name_field")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vs_name_field)
        self.vs_home_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_home_label.setFont(font)
        self.vs_home_label.setObjectName("vs_home_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.vs_home_label)
        self.vs_home_field = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_home_field.setFont(font)
        self.vs_home_field.setObjectName("vs_home_field")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.vs_home_field)
        self.vs_flag_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_flag_label.setFont(font)
        self.vs_flag_label.setObjectName("vs_flag_label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.vs_flag_label)
        self.vs_flag_form = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_flag_form.setFont(font)
        self.vs_flag_form.setObjectName("vs_flag_form")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.vs_flag_form)
        self.vs_class_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_class_label.setFont(font)
        self.vs_class_label.setObjectName("vs_class_label")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.vs_class_label)
        self.vs_class_form = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_class_form.setFont(font)
        self.vs_class_form.setObjectName("vs_class_form")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.vs_class_form)
        self.vs_cargo_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_cargo_label.setFont(font)
        self.vs_cargo_label.setObjectName("vs_cargo_label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.vs_cargo_label)
        self.vs_cargo_form = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_cargo_form.setFont(font)
        self.vs_cargo_form.setObjectName("vs_cargo_form")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.vs_cargo_form)
        self.vs_speed_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_speed_label.setFont(font)
        self.vs_speed_label.setObjectName("vs_speed_label")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.vs_speed_label)
        self.vs_speed_form = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_speed_form.setFont(font)
        self.vs_speed_form.setObjectName("vs_speed_form")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.vs_speed_form)
        self.vs_load_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_load_label.setFont(font)
        self.vs_load_label.setObjectName("vs_load_label")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.vs_load_label)
        self.vs_load_form = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_load_form.setFont(font)
        self.vs_load_form.setObjectName("vs_load_form")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.vs_load_form)
        self.vs_status_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vs_status_label.setFont(font)
        self.vs_status_label.setObjectName("vs_status_label")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.vs_status_label)
        self.label_16_form = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_16_form.setFont(font)
        self.label_16_form.setObjectName("label_16_form")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.label_16_form)
        self.horizontalLayout.addLayout(self.formLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        VesselWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VesselWindow)
        self.statusbar.setObjectName("statusbar")
        VesselWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VesselWindow)
        QtCore.QMetaObject.connectSlotsByName(VesselWindow)

    def retranslateUi(self, VesselWindow):

        # info = {
        #     "name"         : name,
        #     "avg_speed"    : int(ship["avg_speed"]),
        #     "home_port"    : db.ports.find_one({"_id": ship["home_port_id"]})["name"],
        #     "load"         : int(ship["cargo_amount"]),
        #     "flag"         : db.countries.find_one({"_id": ship["flag_id"]})["name"],
        #     "class"        : db.sizes.find_one({"_id": ship["size_type_id"]})["name"],
        #     "cargo_type"   : db.cargo_types.find_one({"_id": ship["ship_type_id"]})["name"],
        #     "status"       : db.jobs.find_one({"_id": ship["job_id"]})["name"]
        # }

        _translate = QtCore.QCoreApplication.translate
        VesselWindow.setWindowTitle(_translate("VesselWindow", "Vessel"))
        self.journal_label.setText(_translate("VesselWindow", "Journal"))
        self.journal_list.setSortingEnabled(False)
        self.okPB.setText(_translate("VesselWindow", "OK"))
        self.addPB.setText(_translate("VesselWindow", "Add"))
        self.delPB.setText(_translate("VesselWindow", "Delete"))
        self.ship_name_label.setText(_translate("VesselWindow", "Vessel"))
        self.vs_name_label.setText(_translate("VesselWindow"  , "Name"))
        self.vs_name_field.setText(_translate("VesselWindow"  , self.info["name"]))
        self.vs_home_label.setText(_translate("VesselWindow"  , "Home port"))
        self.vs_home_field.setText(_translate("VesselWindow"  , self.info["home_port"]))
        self.vs_flag_label.setText(_translate("VesselWindow"  , "Flag"))
        self.vs_flag_form.setText(_translate("VesselWindow"   , self.info["flag"]))
        self.vs_class_label.setText(_translate("VesselWindow" , "Class"))
        self.vs_class_form.setText(_translate("VesselWindow"  , self.info["class"]))
        self.vs_cargo_label.setText(_translate("VesselWindow" , "Cargo"))
        self.vs_cargo_form.setText(_translate("VesselWindow"  , self.info["cargo_type"]))
        self.vs_speed_label.setText(_translate("VesselWindow" , "Avg. speed"))
        self.vs_speed_form.setText(_translate("VesselWindow"  , self.info["avg_speed"]))
        self.vs_load_label.setText(_translate("VesselWindow"  , "Load"))
        self.vs_load_form.setText(_translate("VesselWindow"   , self.info["load"]))
        self.vs_status_label.setText(_translate("VesselWindow", "Current status"))
        self.label_16_form.setText(_translate("VesselWindow"  , self.info["status"]))

    def buildJournal():

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

import images_rc
