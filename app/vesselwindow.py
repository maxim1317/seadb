from PyQt5 import QtCore, QtGui, QtWidgets

from style import *
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
        icon.addPixmap(QtGui.QPixmap("./images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.aframax_img = "\"images/tanker_aframax.svg\""
        self.panamax_img = "\"images/tanker_panamax.svg\""
        self.suezmax_img = "\"images/tanker_suezmax.svg\""
        self.VLCC_img    = "\"images/tanker_vlcc.svg\""
        self.ULCC_img    = "\"images/tanker_ulcc.svg\""

        VesselWindow.setWindowIcon(icon)
        VesselWindow.setAutoFillBackground(False)

        self.theme = Theme(dark=False)
        self.style = Style().style
        VesselWindow.setStyleSheet(self.style)

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

        self.journal_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.journal_table.setFont(font)
        # self.journal_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.journal_table.setResizeMode(QtWidgets.QTableView.Adjust)
        self.journal_table.setWordWrap(True)
        self.journal_table.setObjectName("journal_table")

        self.buildJournal()

        self.verticalLayout_2.addWidget(self.journal_table)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.okPB = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        # font = QtGui.QFont()
        # font.setPointSize(18)
        # self.okPB.setFont(font)
        # self.okPB.hide()
        # self.okPB.setObjectName("pushButton")
        # self.horizontalLayout_3.addWidget(self.okPB)
        # spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem2)

        self.backPB = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(18)
        self.backPB.setFont(font)
        self.backPB.setText("Back")
        self.backPB.setStyleSheet("color: " + self.theme.red + ";")
        self.horizontalLayout_3.addWidget(self.backPB)

        SI = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(SI)

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
        self.delPB.hide()
        self.horizontalLayout_3.addWidget(self.delPB)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        # self.backHL = QtWidgets.QHBoxLayout()
        # self.verticalLayout_2.addLayout(self.backHL)

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

        if self.info["class"] == "LR1":
            ship_img = self.aframax_img
        elif self.info["class"] == "Aframax":
            ship_img = self.panamax_img
        elif self.info["class"] == "Suezmax":
            ship_img = self.suezmax_img
        elif self.info["class"] == "VLCC":
            ship_img = self.VLCC_img
        elif self.info["class"] == "ULCC":
            ship_img = self.ULCC_img
        else:
            print(self.info["class"])

        self.ship_view_label.setText("<html><head/><body><p><img src=" + ship_img + "/></p></body></html>")
        self.ship_view_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ship_view_label.setObjectName("ship_view_label")

        self.verticalLayout.addWidget(self.ship_view_label)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.setLineWidth(2)
        self.line.setStyleSheet("color: " + self.theme.accent + ";")
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
        self.journal_table.setSortingEnabled(False)
        # self.okPB.setText(_translate("VesselWindow", "OK"))
        self.addPB.setText(_translate("VesselWindow", "Add"))
        # self.delPB.setText(_translate("VesselWindow", "Delete"))
        if self.auth[0] not in ["admin", "oberon", "manager"]:
            self.okPB.hide()
            self.addPB.hide()
            self.delPB.hide()
        elif self.auth[0] == "manager":
            self.delPB.hide()

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

    def buildJournal(self):
        self.journal_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.journal_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.journal_table.setFocusPolicy(QtCore.Qt.NoFocus)

        schedule = self.info["schedule"]

        login, password = self.auth
        client = MongoClient("mongodb://" + login + ":" + password + "@127.0.0.1:27017/seadb")
        db = client[DB_NAME]

        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)

        self.journal_table.setColumnCount(5)
        self.journal_table.setRowCount(len(schedule))
        # self.journal_table.setColumnWidth(0, self.journal_table.sizeHint().width() // 5)
        # self.journal_table.setColumnWidth(1, self.journal_table.sizeHint().width() // 5)
        # self.journal_table.setColumnWidth(2, self.journal_table.sizeHint().width() // 5)
        # self.journal_table.setColumnWidth(3, self.journal_table.sizeHint().width() // 5)
        # self.journal_table.setColumnWidth(4, self.journal_table.sizeHint().width() // 5)
        # self.journal_table.setStyleSheet("background: transparent; color: #CFD8DC;")
        # stylesheet = "QTableView{          \
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
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

        self.journal_table.setHorizontalHeaderLabels(["From", "To", "Begins", "Ends", "Job"])

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
            self.journal_table.setItem(i, 0, _from )
            self.journal_table.setItem(i, 1, _to   )
            self.journal_table.setItem(i, 2, _begin)
            self.journal_table.setItem(i, 3, _end  )
            self.journal_table.setItem(i, 4, _job  )

            self.last_port = __to
            self.last_date = __end

        return
