import sys
import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setFixedWidth(200)
        self.setFixedHeight(200)

        self.widget = QWidget(self)
        self.layout = QVBoxLayout(self)
        self.nav_mark = QLabel("ORIGAMI")
        self.nav_mark.setFont(QFont("Black Han Sans"))

        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.widget)
        self.layout.addWidget(self.nav_mark)

        self.widget.setStyleSheet("""
        QWidget {
            border: 20px solid black;
            border-radius: 20px;
            background-color: rgb(0, 255, 255);
            }
        """)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()

    print(PYQT_VERSION_STR)
    os.chdir('../')
    print(os.getcwd())


    sys.exit(app.exec_())