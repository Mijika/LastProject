import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarkstyle

from Video import Video
from UI import TitleBar
from UI import BasicWindow

__author__ = "damgi Ahn <sbahn42@gmail.com>"
__version__ = "1.0.0"

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class StreamingWindow(BasicWindow):

    def __init__(self, parent=None):
        super(StreamingWindow, self).__init__(parent)
        super().setTitleName("Streaming Window")
        super().basicUI()

        self.initUi()
        self.video = Video(self, QSize(self.frm.width(), self.frm.height()))

    def initUi(self):

        self.startCamBtn = QPushButton('캠 시작', self)
        self.recordingBtn = QPushButton('녹화 시작', self)
        self.endRecordingBtn = QPushButton('녹화 종료', self)
        self.helpBtn = QPushButton('도움말', self)

        self.startCamBtn.setCheckable(True)
        self.recordingBtn.setCheckable(True)
        self.endRecordingBtn.setCheckable(True)
        self.helpBtn.setCheckable(False)

        # 녹화와 녹화 종료 토글 그룹
        self.recordingGrp = QButtonGroup(self)
        self.recordingGrp.addButton(self.recordingBtn, 0)
        self.recordingGrp.addButton(self.endRecordingBtn, 1)

        self.startCamBtn.clicked.connect(self.onOffCam)
        self.recordingGrp.buttonClicked[int].connect(self.recordingOption)
        self.helpBtn.clicked.connect(self.help)

        self.btn_vbox.addWidget(self.startCamBtn)
        self.btn_vbox.addWidget(self.recordingBtn)
        self.btn_vbox.addWidget(self.endRecordingBtn)
        self.btn_vbox.addWidget(self.helpBtn)
        self.btn_vbox.addStretch(1)

        # video area
        self.frm = QLabel(self)
        self.frm.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.frm.setLineWidth(1)

        self.Context_hbox.addWidget(self.frm, 1)

        self.move(100, 100)
        self.show()

    @pyqtSlot()
    def onOffCam(self):
        if self.startCamBtn.isChecked():
            self.startCamBtn.setText('캠 정지')
            self.video.startCam()
        else:
            self.startCamBtn.setText('캠 시작')
            self.video.stopCam()

    @pyqtSlot(int)
    def recordingOption(self, id):
        if self.recordingGrp.button(id).isChecked():
            if not id:
                self.video.recording()
            else:
                self.video.endRecording()

    @pyqtSlot()
    def help(self):
        print("도움말")
        pass

    @pyqtSlot(QImage)
    def recvImage(self, img):
        self.frm.setPixmap(QPixmap.fromImage(img))

    def closeEvent(self, e):
        self.video.stopCam()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # QT 다크테마
    os.environ['QT_API'] = "pyqt5"
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)

    window = StreamingWindow()
    sys.exit(app.exec_())
