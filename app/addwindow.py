from PyQt5 import QtCore, QtGui, QtWidgets
import datetime as dt
import networkx as nx

from style import *
from ut import *


class AddWindow(object):
    def setupUi(self, AddWindow, auth, graph, name, prev_port, prev_date):
        self.auth = auth

        login, password = auth
        client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
        db = client[DB_NAME]

        self.db = db

        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(1342, 880)

        center(AddWindow)

        self.vessel = db.ships.find_one({"name": name})

        self.prev_date = prev_date
        self.prev_port  = prev_port
        self.good_ports = get_good_ports(auth, self.vessel["ship_type_id"])

        self.good_ports_names = [i["name"] for i in self.good_ports]

        self.graph = graph
        self.name  = name

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddWindow.sizePolicy().hasHeightForWidth())
        AddWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        AddWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddWindow.setWindowIcon(icon)
        AddWindow.setAutoFillBackground(False)

        self.theme = Theme(dark=False)
        self.style = Style().style
        AddWindow.setStyleSheet(self.style)

        AddWindow.setTabShape(QtWidgets.QTabWidget.Triangular)

        self.centralwidget = QtWidgets.QWidget(AddWindow)
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

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)

        self.line_2.setObjectName("line_2")
        self.line_2.setStyleSheet("color: " + self.theme.accent + ";")
        self.verticalLayout.addWidget(self.line_2)

        self.load_img = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.load_img.setAlignment(QtCore.Qt.AlignCenter)
        self.load_img.setObjectName("load_img")
        self.verticalLayout.addWidget(self.load_img)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

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
        completer = QtWidgets.QCompleter(self.good_ports_names, self.load_from_edit)
        self.load_from_edit.setCompleter(completer)        # Set QCompleter in the input field
        self.load_from_edit.setObjectName("load_from_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.load_from_edit)

        # self.load_to = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.load_to.setFont(font)
        # self.load_to.setObjectName("load_to")
        # self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.load_to)

        # self.load_to_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.load_to_edit.setFont(font)
        # self.load_to_edit.setObjectName("load_to_edit")
        # self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.load_to_edit)

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
        self.load_starts_edit.setCalendarPopup(False)
        self.load_starts_edit.setDisplayFormat("dd.MM.yyyy")
        self.load_starts_edit.setMinimumDate(self.prev_date)
        self.load_starts_edit.setStyleSheet(
            "    background: transparent;\n"
            "    border: 1px solid transparent;\n"
            "    border-top: none;\n"
            "    border-bottom: 2px solid " + self.theme.accent + ";\n"
            "    color: " + self.theme.primary + ";\n"
        )
        # self.load_ends = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.load_ends.setFont(font)
        # self.load_ends.setObjectName("load_ends")
        # self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.load_ends)

        # self.load_ends_edit = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.load_ends_edit.setFont(font)
        # self.load_ends_edit.setObjectName("load_ends_edit")
        # self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.load_ends_edit)

        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)

        self.load_okPB = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.load_okPB.setFont(font)
        self.load_okPB.setObjectName("pushButton")
        self.load_okPB.clicked.connect(self.checkLoad)
        self.horizontalLayout_4.addWidget(self.load_okPB)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)

        self.line_3.setObjectName("line_3")
        self.line_3.setStyleSheet("color: " + self.theme.accent + ";")
        self.verticalLayout_2.addWidget(self.line_3)

        self.unload_img = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.unload_img.setAlignment(QtCore.Qt.AlignCenter)
        self.unload_img.setObjectName("unload_img")
        self.verticalLayout_2.addWidget(self.unload_img)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)

        # self.unload_from = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.unload_from.setFont(font)
        # self.unload_from.setObjectName("unload_from")
        # self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.unload_from)

        # self.unload_from_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.unload_from_edit.setFont(font)
        # self.unload_from_edit.setObjectName("unload_from_edit")
        # self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.unload_from_edit)

        self.unload_to = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_to.setFont(font)
        self.unload_to.setObjectName("unload_to")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.unload_to)

        self.unload_to_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        completer = QtWidgets.QCompleter(self.good_ports_names, self.unload_to_edit)
        self.unload_to_edit.setCompleter(completer)        # Set QCompleter in the input field
        self.unload_to_edit.setFont(font)
        self.unload_to_edit.setObjectName("unload_to_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.unload_to_edit)

        # self.unload_starts = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.unload_starts.setFont(font)
        # self.unload_starts.setObjectName("unload_starts")
        # self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.unload_starts)

        # self.unload_starts_edit = QtWidgets.QDateEdit(self.verticalLayoutWidget_3)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.unload_starts_edit.setFont(font)
        # self.unload_starts_edit.setObjectName("unload_starts_edit")
        # self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.unload_starts_edit)

        self.unload_ends = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_ends.setFont(font)
        self.unload_ends.setObjectName("unload_ends")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.unload_ends)

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

        self.unload_okPB = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.unload_okPB.setFont(font)
        self.unload_okPB.setObjectName("unload_okPB")
        self.unload_okPB.clicked.connect(self.checkUnload)
        self.horizontalLayout_5.addWidget(self.unload_okPB)

        self.unload_to_edit.setEnabled(False)
        self.unload_okPB.setEnabled(False)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)

        # self.verticalLayout_2.setEnabled(False)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)

        self.line.setObjectName("line")
        self.line.setStyleSheet("color: " + self.theme.accent + ";")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)

        self.line_4.setStyleSheet("color: " + self.theme.accent + ";")
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)

        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)

        self.journal_table = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.journal_table.setFont(font)
        self.journal_table.setObjectName("journal_table")
        self.journal_table.setColumnCount(0)

        self.journal_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.journal_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.journal_table.setFocusPolicy(QtCore.Qt.NoFocus)

        self.journal_table.setColumnCount(5)

        self.journal_table.verticalHeader().hide()
        header = self.journal_table.horizontalHeader()
        header.setStyleSheet("background-color: " + self.theme.bg + "; color: " + self.theme.accent + ";")
        header.setFont(font)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        self.journal_table.setHorizontalHeaderLabels(["From", "To", "Begins", "Ends", "Job"])

        self.journal_table.setRowCount(0)
        self.verticalLayout_4.addWidget(self.journal_table)

        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.path_length_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.path_length_label.setFont(font)
        self.path_length_label.setObjectName("path_length_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.path_length_label)
        self.horizontalLayout_3.addLayout(self.formLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.how_many_days = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.how_many_days.setFont(font)
        self.how_many_days.setObjectName("how_many_days")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.how_many_days)
        self.horizontalLayout_3.addLayout(self.formLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.cancelPB = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cancelPB.setFont(font)
        self.cancelPB.setObjectName("cancelPB")
        self.horizontalLayout_2.addWidget(self.cancelPB)

        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)

        self.clearPB = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.clearPB.setFont(font)
        self.clearPB.setText("Clear")
        self.clearPB.setObjectName("clearPB")
        self.horizontalLayout_2.addWidget(self.clearPB)

        self.savePB = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.savePB.setFont(font)
        self.savePB.setObjectName("savePB")
        self.horizontalLayout_2.addWidget(self.savePB)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        AddWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddWindow)
        self.statusbar.setObjectName("statusbar")
        AddWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def checkLoad(self):
        self.port_from = self.load_from_edit.text()
        if self.port_from not in self.good_ports_names:
            self.load_from_edit.setStyleSheet("border-bottom: 2px solid " + self.theme.red + ";")
            return

        self.load_from_edit.setStyleSheet("border-bottom: 2px solid " + self.theme.green + ";")

        img = "images/ports/" + self.port_from + '_' + self.theme.name + ".png"
        self.load_img.setText("<html><head/><body><p><img src=\"" + img + "\"/></p></body></html>")
        self.path_from = self.find_path(self.prev_port, self.port_from)

        self.path_length = len(self.path_from)
        self.path_length_label.setText(str(self.path_length) + " ports")
        self.buildLoadJournal()

        self.unload_to_edit.setEnabled(True)
        self.unload_okPB.setEnabled(True)

        self.load_from_edit.setEnabled(False)
        self.load_starts_edit.setEnabled(False)
        self.load_okPB.setEnabled(False)

        self.unload_ends_edit.setText(self.last_date.strftime("%d.%m.%Y"))
        self.how_many_days.setText(str(self.last_date - self.load_starts_edit.date().toPyDate()))

        self.prev_port = self.path_from[len(self.path_from) - 1]
        return

    def checkUnload(self):
        self.port_to = self.unload_to_edit.text()
        if self.port_to not in self.good_ports_names:
            self.unload_to_edit.setStyleSheet("border-bottom: 2px solid " + self.theme.red + ";")
            return

        self.unload_to_edit.setStyleSheet("border-bottom: 2px solid " + self.theme.green + ";")

        img = "images/ports/" + self.port_to + '_' + self.theme.name + ".png"
        self.unload_img.setText("<html><head/><body><p><img src=\"" + img + "\"/></p></body></html>")
        self.path_to = self.find_path(self.prev_port, self.port_to)

        self.path_length += len(self.path_to)
        self.path_length_label.setText(str(self.path_length) + " ports")
        self.buildUnloadJournal()

        self.unload_ends_edit.setText(self.last_date.strftime("%d.%m.%Y"))
        self.how_many_days.setText(str(self.last_date - self.load_starts_edit.date().toPyDate()))

        self.unload_to_edit.setEnabled(False)
        self.unload_okPB.setEnabled(False)
        return

    def find_path(self, port_from, port_to):
        return nx.dijkstra_path(self.graph, port_from, port_to)

    def buildLoadJournal(self):
        login, password = self.auth
        client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
        db = client[DB_NAME]

        schedule = gen_load_schedule(self.auth, self.name, self.path_from, self.load_starts_edit.date().toPyDate())
        self.schedule = schedule

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)

        self.journal_table.setRowCount(len(schedule))

        font.setPointSize(14)
        for i in range(0, len(schedule)):

            # print(schedule[i]["pier_id"])

            if schedule[i]["destination_id"] is not None:
                # print(schedule[i]["destination_id"])
                __from = db.ports.find_one({
                    "_id": db.destinations.find_one({"_id": schedule[i]["destination_id"]})["departure"]
                })["name"]
                __to   = db.ports.find_one({
                    "_id": db.destinations.find_one({"_id": schedule[i]["destination_id"]})["destination"]
                })["name"]

            elif schedule[i]["anchorage_id"] is not None:
                __from = db.ports.find_one({
                    "_id": db.anchorages.find_one({"_id": schedule[i]["anchorage_id"]})["port_id"]
                })["name"]
                __to   = __from
            elif schedule[i]["pier_id"] is not None:
                __from = db.ports.find_one({
                    "_id": db.piers.find_one({"_id": schedule[i]["pier_id"]})["port_id"]
                })["name"]
                __to   = __from
            else:
                __from = "None"
                __to   = "None"

            __end = schedule[i]["estimated_end"].date()

            _from  = QtWidgets.QTableWidgetItem(__from)
            _from.setFont(font)
            _to    = QtWidgets.QTableWidgetItem(__to)
            _to.setFont(font)
            _begin = QtWidgets.QTableWidgetItem(str(schedule[i]["started"].date()))
            _begin.setFont(font)
            _end   = QtWidgets.QTableWidgetItem(str(__end))
            _end.setFont(font)
            _job   = QtWidgets.QTableWidgetItem(db.jobs.find_one({"_id": schedule[i]["job"]})["job"])
            _job.setFont(font)
            self.journal_table.setItem(i, 0, _from )
            self.journal_table.setItem(i, 1, _to   )
            self.journal_table.setItem(i, 2, _begin)
            self.journal_table.setItem(i, 3, _end  )
            self.journal_table.setItem(i, 4, _job  )

            self.last_port = __to
            self.last_date = __end
            self.from_len  = self.journal_table.rowCount()

        return

    def buildUnloadJournal(self):
        login, password = self.auth
        client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
        db = client[DB_NAME]

        schedule = gen_unload_schedule(self.auth, self.name, self.path_to, self.last_date)
        self.schedule.extend(schedule)

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)

        self.journal_table.setRowCount(self.journal_table.rowCount() + len(schedule))

        font.setPointSize(14)
        for i in range(0, len(schedule)):

            # print(schedule[i]["pier_id"])

            if schedule[i]["destination_id"] is not None:
                __from = db.ports.find_one({
                    "_id": db.destinations.find_one({"_id": schedule[i]["destination_id"]})["departure"]
                })["name"]
                __to   = db.ports.find_one({
                    "_id": db.destinations.find_one({"_id": schedule[i]["destination_id"]})["destination"]
                })["name"]

            elif schedule[i]["anchorage_id"] is not None:
                __from = db.ports.find_one({
                    "_id": db.anchorages.find_one({"_id": schedule[i]["anchorage_id"]})["port_id"]
                })["name"]
                __to   = __from
            elif schedule[i]["pier_id"] is not None:
                __from = db.ports.find_one({
                    "_id": db.piers.find_one({"_id": schedule[i]["pier_id"]})["port_id"]
                })["name"]
                __to   = __from
            else:
                __from = "None"
                __to   = "None"

            __end = schedule[i]["estimated_end"].date()

            _from  = QtWidgets.QTableWidgetItem(__from)
            _from.setFont(font)
            _to    = QtWidgets.QTableWidgetItem(__to)
            _to.setFont(font)
            _begin = QtWidgets.QTableWidgetItem(str(schedule[i]["started"].date()))
            _begin.setFont(font)
            _end   = QtWidgets.QTableWidgetItem(str(__end))
            _end.setFont(font)
            _job   = QtWidgets.QTableWidgetItem(db.jobs.find_one({"_id": schedule[i]["job"]})["job"])
            _job.setFont(font)
            self.journal_table.setItem(self.from_len + i, 0, _from )
            self.journal_table.setItem(self.from_len + i, 1, _to   )
            self.journal_table.setItem(self.from_len + i, 2, _begin)
            self.journal_table.setItem(self.from_len + i, 3, _end  )
            self.journal_table.setItem(self.from_len + i, 4, _job  )

            self.last_port = __to
            self.last_date = __end

            self.task = {
                "name": "user task " + dt.datetime.now().strftime("%d.%m.%Y %I:%M:%S"),
                "ship_id": db.ships.find_one({"name": self.name}),
                "schedule": self.schedule
            }

        return

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "AddWindow"))
        self.label_3.setText(_translate("AddWindow", "Create your task"))
        self.label.setText(_translate("AddWindow", "Load"))
        self.load_img.setText(_translate("AddWindow", "<html><head/><body><p><img src=\"./images/icon.png\"/></p></body></html>"))
        self.load_from.setText(_translate("AddWindow", "From"))
        # self.load_to.setText(_translate("AddWindow", "To"))
        self.load_starts.setText(_translate("AddWindow", "Starts on"))
        # self.load_ends.setText(_translate("AddWindow", "Ends on"))
        # self.load_ends_edit.setText(_translate("AddWindow", "TextLabel"))
        self.load_okPB.setText(_translate("AddWindow", "OK"))
        self.label_2.setText(_translate("AddWindow", "Unload"))
        self.unload_img.setText(_translate("AddWindow", "<html><head/><body><p><img src=\"./images/icon.png\"/></p></body></html>"))
        # self.unload_from.setText(_translate("AddWindow", "From"))
        self.unload_to.setText(_translate("AddWindow", "To"))
        # self.unload_starts.setText(_translate("AddWindow", "Starts on"))
        self.unload_ends.setText(_translate("AddWindow", "Ends on"))
        self.unload_ends_edit.setText(_translate("AddWindow", "Unknown"))
        self.unload_okPB.setText(_translate("AddWindow", "OK"))
        self.label_9.setText(_translate("AddWindow", "Voyage Plan"))
        self.label_4.setText(_translate("AddWindow", "Ship will visit"))
        self.path_length_label.setText(_translate("AddWindow", "0 ports"))
        self.label_7.setText(_translate("AddWindow", "The task will take"))
        self.how_many_days.setText(_translate("AddWindow", "0 days"))
        self.cancelPB.setText(_translate("AddWindow", "Cancel"))
        self.savePB.setText(_translate("AddWindow", "Save"))
