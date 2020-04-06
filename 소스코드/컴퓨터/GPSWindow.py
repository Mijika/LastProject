import io
import os
import sys

import folium

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWebEngineWidgets
import qdarkstyle

from GPS import GPS
from UI import TitleBar
from UI import BasicWindow


class GPSWindow(BasicWindow):

    def __init__(self, parent=None):
        super(GPSWindow, self).__init__(parent)
        super().setTitleName("GPS Window")
        super().basicUI()

        self.mapDateIo = io.BytesIO()

        self.initUi()
        self.gps = GPS(self, QSize(self.frm.width(), self.frm.height()), self.mapDateIo)

    def initUi(self):

        self.startGPSBtn = QPushButton('GPS 시작', self)
        self.TrackingBtn = QPushButton('트래킹 시작', self)
        self.helpBtn = QPushButton('도움말', self)

        self.startGPSBtn.setCheckable(True)
        self.TrackingBtn.setCheckable(True)
        self.helpBtn.setCheckable(False)

        # self.startGPSBtn.clicked.connect(self.startGPS)
        # self.TrackingBtn.buttonClicked[int].connect(self.Tracking)
        # self.helpBtn.clicked.connect(self.help)

        self.btn_vbox.addWidget(self.startGPSBtn)
        self.btn_vbox.addWidget(self.TrackingBtn)
        self.btn_vbox.addWidget(self.helpBtn)
        self.btn_vbox.addStretch(1)

        try:
            self.frm = QtWebEngineWidgets.QWebEngineView()
            self.frm.setHtml(self.mapDateIo.getvalue().decode())
        except Exception as e:
            print("web Engine Error" + str(e))


        self.Context_hbox.addWidget(self.frm, 1)

        self.move(800, 100)
        self.show()

    @pyqtSlot()
    def startGPS(self):
        if self.startGPSBtn.isChecked():
            self.startGPSBtn.setText('GPS 정지')
            self.gps.startGPS()
        else:
            self.startGPSBtn.setText('GPS 시작')
            self.gps.stopGPS()

    @pyqtSlot()
    def Tracking(self):
        if self.TrackingBtn.isChecked():
            self.TrackingBtn.setText('트래킹 정지')
            self.gps.startTracking()
        else:
            self.TrackingBtn.setText('트래킹 시작')
            self.gps.stopTracking()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # QT 다크테마
    os.environ['QT_API'] = "pyqt5"
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)

    window = GPSWindow()
    sys.exit(app.exec_())
