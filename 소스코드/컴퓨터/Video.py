from threading import Thread
import time

import cv2

from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Video(QObject):
    sendImage = pyqtSignal(QImage)

    def __init__(self, widget, size):
        super().__init__()
        self.flag = False
        self.widget = widget
        self.size = size
        self.sendImage.connect(self.widget.recvImage)

    def startCam(self):
        self.flag = True
        try:
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        except Exception as e:
            print('Cam Error : ', e)
        else:
            self.bThread = True
            self.thread = Thread(target=self.threadFunc)
            self.thread.start()

    def stopCam(self):
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

    def recording(self):
        print("녹화 시작")
        pass

    def endRecording(self):
        print("녹화 종료")
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
