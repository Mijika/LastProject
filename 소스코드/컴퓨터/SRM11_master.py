import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import cv2


class CamStraming(QtCore.QObject):
    def __init__(self, parent=None):
        super(CamStraming, self).__init__(parent)
        # esp32 비디오 스트리밍 주소 입력
        self.camArr = "http://172.30.1.19:8091/?action=stream"
        self.camera = cv2.VideoCapture(self.camArr)
        self.ret, self.image = self.camera.read()
        height, width = self.image.shape[:2]

    def startVideo(self):
        global image

        self.run_video = True
        while self.run_video:
            self.ret, self.image = self.camera.read()
            self.color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            self.qt_image1 = QtGui.QImage(self.color_swapped_image.data,
                                          self.width,
                                          self.height,
                                          self.color_swapped_image.strides[0],
                                          QtGui.QImage.Format_RGB888)
            self.VideoSignal1.emit(self.qt_image1)

            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(25, loop.quit)  # 25ms
            loop.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
