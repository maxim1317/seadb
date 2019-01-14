from PyQt5 import QtCore, QtGui, QtWidgets

from style import *
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
        icon.addPixmap(QtGui.QPixmap("./images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PortWindow.setWindowIcon(icon)
        PortWindow.setAutoFillBackground(False)

        self.theme = Theme(dark=False)
        self.style = Style().style
        PortWindow.setStyleSheet(self.style)

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

        self.plot_space = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plot_space.setFont(font)
        self.plot_space.setAlignment(QtCore.Qt.AlignCenter)
        self.plot_space.setObjectName("plot_space")
        self.verticalLayout_2.addWidget(self.plot_space)

        self.journal_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.journal_table.setFont(font)
        self.journal_table.setWordWrap(True)
        self.journal_table.setObjectName("journal_table")

        self.buildJournal()
        self.plot = self.plot_turnover()
        self.plot_space.setText("<html><head/><body><p><img src='" + self.plot + "'/></p></body></html>")

        self.verticalLayout_2.addWidget(self.journal_table)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.backHL = QtWidgets.QHBoxLayout()

        self.backPB = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(18)
        self.backPB.setFont(font)
        self.backPB.setText("Back")
        self.backPB.setStyleSheet("color: " + self.theme.red + ";")
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
        self.line.setStyleSheet("color: " + self.theme.accent + ";")
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
        self.label_13.setText(_translate("PortWindow"    , str(round(self.info["turnover"], 2)) + ' MT'))

        self.label_7.setText(_translate("PortWindow"     , "Ships in port"))
        self.label_14.setText(_translate("PortWindow"    , str(self.info["ships_in_port"])))

    def buildJournal(self):
        from random import triangular

        self.dates_plot = {}

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

        # stylesheet = "                     \
        #     QTableView{                    \
        #         background: transparent;   \
        #         background-color: #263238; \
        #         color: #546E7A;            \
        #     };                             \
        #     QHeaderView::section{          \
        #         background: transparent;   \
        #         background-color: #263238; \
        #         color: #80CBC4;            \
        #         font-size: 12;             \
        #     }                              \
        # "
        # self.journal_table.setStyleSheet(stylesheet)

        self.journal_table.verticalHeader().hide()
        header = self.journal_table.horizontalHeader()
        header.setStyleSheet("background-color: " + self.theme.bg + "; color: " + self.theme.accent + ";")
        header.setFont(font)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        self.journal_table.setHorizontalHeaderLabels(["Date", "Ship", "Cargo Amount", "Job"])

        prev_ships = set([])

        font.setPointSize(12)
        for i in range(0, len(journal)):
            ship   = db.ships.find_one({"_id": journal[i]["ship_id"]})

            _date  = QtWidgets.QTableWidgetItem(str(journal[i]["date"].date()))
            _date.setFont(font)
            _ship  = QtWidgets.QTableWidgetItem(ship["name"])
            _ship.setFont(font)
            _job   = QtWidgets.QTableWidgetItem(db.jobs.find_one({"_id": journal[i]["operation"]})["job"])
            if _job.text() == "LOADING":
                _job.setForeground(QtGui.QColor(self.theme.green))
            if _job.text() == "UNLOADING":
                _job.setForeground(QtGui.QColor(self.theme.red))
            _job.setFont(font)

            amnt = ship["cargo_amount"]
            if amnt == 0 and _job.text() != "RESTING":
                size_type = ship["size_type_id"]
                amnt = triangular(
                    0,
                    db.sizes.find({"_id": size_type}).limit(1)[0]["max_amount"],
                    db.sizes.find({"_id": size_type}).limit(1)[0]["max_amount"] - 100000.0
                )
            if _job.text() == "RESTING":
                amnt = 0
            _amnt  = QtWidgets.QTableWidgetItem(str(int(amnt)))
            _amnt.setFont(font)

            if ship["_id"] not in prev_ships:
                self.dates_plot[journal[i]["date"].date()] = self.dates_plot.get(journal[i]["date"].date(), 0) + round(amnt) / 5
                # prev_ships.add(ship["_id"])

            self.journal_table.setItem(i, 0, _date)
            self.journal_table.setItem(i, 1, _ship)
            self.journal_table.setItem(i, 2, _amnt)
            self.journal_table.setItem(i, 3, _job )

        return

    def plot_turnover(self):
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        import os.path

        path = "images/plots/" + self.name.replace(" ", "") + ".png"

        # if os.path.exists(path):
        #     return path

        x = [i for i in self.dates_plot.keys()]
        y = [i / (1000 * 1000) for i in self.dates_plot.values()]

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m.%Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        plt.xlabel("Date", color=self.theme.red)
        plt.ylabel("Turnover (MT)", color=self.theme.red)
        plt.plot(x, y, '.', color=self.theme.red)
        plt.gcf().autofmt_xdate()
        [i.set_color(self.theme.primary) for i in plt.gca().get_xticklabels()]
        [i.set_color(self.theme.primary) for i in plt.gca().get_yticklabels()]
        plt.savefig(
            path,
            transparent=True,
            frameon=False,
            figsize=(650 / 96, 300 / 96),
            dpi=96
        )
        plt.close()
        return path
