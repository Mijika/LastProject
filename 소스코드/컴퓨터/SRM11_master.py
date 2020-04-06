import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarkstyle

from UI import TitleBar
from UI import BasicWindow
from StreamingWindow import StreamingWindow

__author__ = "damgi Ahn <sbahn42@gmail.com>"
__version__ = "1.0.0"

class MainWindow(QWidget):
    def __init__(self):
        sert = StreamingWindow()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # QT 다크테마
    os.environ['QT_API'] = "pyqt5"
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app.setStyleSheet(dark_stylesheet)

    window = MainWindow()
    sys.exit(app.exec_())
