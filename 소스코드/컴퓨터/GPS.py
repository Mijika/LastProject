import io
import time
from threading import Thread

from PyQt5.QtCore import *
from PyQt5.QtGui import *

import folium
from folium import plugins


class GPS(QObject):
    def __init__(self, widget, size, mapDateIo):
        super().__init__()
        self.flag = False
        self.widget = widget
        self.size = size
        self.dateIo = mapDateIo

        self.GPSInit()

    def GPSInit(self):
        self.location = [45.5236, -122.6750]
        self.m = folium.Map(self.location,
                            tiles="Stamen Toner",
                            zoom_start=16)

    def startSGP(self):
        self.flag = True
        try:
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        except Exception as e:
            print('GPS Error : ', e)
        else:
            self.bThread = Truearget=self.threadFunc)
            self.thread.start()

            self.thread = Thread(t
    def stopGPS(self):
        self.bThread = False
        bopen = False

        if not self.flag:
            return

        try:
            bopen = self.cap.isOpened()
        except Exception as e:
            print('Error cam not opened' + str(e))
        else:
            self.cap.release()

    def startTracking(self):
        pass

    def stopTracking(self):
        pass

    def threadFunc(self):
        while self.bThread:
            ok, frame = self.cap.read()
            if ok:
                # create image
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb.shape
                bytesPerLine = ch * w
                img = QImage(rgb.data, w, h, bytesPerLine, QImage.Format_RGB888)
                resizedImg = img.scaled(self.size.width(), self.size.height(), Qt.KeepAspectRatio)
                self.sendImage.emit(resizedImg)
            else:
                print('cam read errror')

            time.sleep(0.01)

        self.sendImage.emit(QImage())
        print('thread finished')
