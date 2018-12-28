from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import loginwindow as lw
import mainwindow as mw
import vesselwindow as vw
import portwindow as pw
import addwindow as aw
import delwindow as dw
import sys
import networkx as nx
from ut import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        splash_pix = QPixmap('images/icon.png')
        self.splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        self.splash.setMask(splash_pix.mask())
        self.splash.show()
        app.processEvents()

        super(MainWindow, self).__init__(parent)

        self.graph = nx.read_yaml("images/graph.yaml")

        self.uiLogin = lw.LoginWindow()

        self.uiMain = mw.MainWindow()

        self.uiVessel = vw.VesselWindow()
        self.uiPort = pw.PortWindow()

        self.uiAdd = aw.AddWindow()
        self.uiDel = dw.DelWindow()

        self.startLogin()

    def startLogin(self):
        self.uiLogin.setupUi(self)
        self.uiLogin.okPB.clicked.connect(self.checkLogin)
        self.show()
        self.splash.finish(self)

    def startMain(self, auth):
        self.uiMain.setupUi(self, auth)
        self.uiMain.ports_ok.clicked.connect(self.checkPort)
        self.uiMain.ships_ok.clicked.connect(self.checkVessel)
        for PB in self.uiMain.topPBs:
            PB.clicked.connect(self.portFromTop)
        self.show()

    def startVessel(self, auth, name):
        self.tmp_name = name
        self.uiVessel.setupUi(self, auth, name)
        self.uiVessel.backPB.clicked.connect(self.gotoMain)
        self.uiVessel.addPB.clicked.connect(self.gotoAdd)
        self.uiVessel.delPB.clicked.connect(self.gotoDel)
        self.show()
        self.splash.finish(self)

    def startAdd(self, auth, name):
        self.uiAdd.setupUi(
            self,
            auth,
            self.graph,
            name,
            self.uiVessel.last_port,
            self.uiVessel.last_date
        )
        self.uiAdd.cancelPB.clicked.connect(self.cancelAdd)
        self.uiAdd.savePB.clicked.connect(self.saveAdd)

        self.uiAdd.clearPB.clicked.connect(self.gotoAdd)
        self.show()

    def startDel(self, auth, name):
        self.uiDel.setupUi(self, auth, name)
        self.show()

    def startPort(self, auth, name, img):
        self.uiPort.setupUi(self, auth, name, img)
        self.uiPort.backPB.clicked.connect(self.gotoMain)
        self.show()
        self.splash.finish(self)

    def gotoAdd(self):
        self.startAdd(self.auth, self.tmp_name)

    def gotoDel(self):
        self.startDel(self.auth, self.tmp_name)

    def cancelAdd(self):
        self.startVessel(self.auth, self.tmp_name)

    def saveAdd(self):
        print(self.uiAdd.schedule)
        self.uiAdd.db.schedules.insert_many(self.uiAdd.schedule)
        self.uiAdd.db.tasks.insert_one(self.uiAdd.task)
        self.startVessel(self.auth, self.tmp_name)  # TEMP

    def checkLogin(self):
        # from time import sleep

        self.login = self.uiLogin.loginLE.text()
        self.pwd = self.uiLogin.pwdLE.text()

        self.auth = (self.login, self.pwd)

        if try_login(login=self.login, password=self.pwd):
            self.uiLogin.loginLE.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            self.uiLogin.pwdLE.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            # sleep(1)
            self.startMain(auth=(self.login, self.pwd))
        else:
            self.uiLogin.loginLE.setStyleSheet("border-bottom: 2px solid #D72638;")
            self.uiLogin.pwdLE.setStyleSheet("border-bottom: 2px solid #D72638;")

    def checkPort(self):
        p_name = self.uiMain.ports_line_edit.text()
        if p_name not in self.uiMain.port_list:
            self.uiMain.ports_line_edit.setStyleSheet("border-bottom: 2px solid #D72638;")
        else:
            self.splash.show()
            app.processEvents()
            point_map = plot_map(auth=(self.login, self.pwd), port_name=p_name)
            self.uiMain.ports_line_edit.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            self.startPort(auth=(self.login, self.pwd), name=self.uiMain.ports_line_edit.text(), img=point_map)

    def checkVessel(self):
        p_name = self.uiMain.ships_line_edit.text()
        print('Ship name: ' + self.uiMain.ships_line_edit.text())
        if p_name not in self.uiMain.ship_list:
            self.uiMain.ships_line_edit.setStyleSheet("border-bottom: 2px solid #D72638;")
        else:
            self.splash.show()
            app.processEvents()
            self.uiMain.ships_line_edit.setStyleSheet("border-bottom: 2px solid #53DD6C;")
            self.startVessel(auth=(self.login, self.pwd), name=self.uiMain.ships_line_edit.text())

    def gotoMain(self):
        self.auth = (self.login, self.pwd)
        self.startMain(auth=self.auth)

    def portFromTop(self):
        print('Port name: ' + self.sender().text())
        point_map = plot_map(auth=(self.login, self.pwd), port_name=self.sender().text())
        self.startPort(auth=(self.login, self.pwd), name=self.sender().text(), img=point_map)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

