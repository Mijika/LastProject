import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from win32api import GetSystemMetrics

__author__ = "damgi Ahn <sbahn42@gmail.com>"
__version__ = "1.2"


QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


class Main(QWidget):
	def __init__(self):
		super(Main, self).__init__()
		self.titleName = "main"
		self.width = GetSystemMetrics(0)
		self.height = GetSystemMetrics(1)

		self.initUI()
		self.setStyle()

	def initUI(self):
		# 타이틀 바와 레이아옷 선언
		self.windowVbox = QVBoxLayout(self)
		self.windowVbox.setContentsMargins(0, 0, 0, 0)

		self.titlebarWidget = TitleBar(self, self.titleName)
		self.titlebarWidget.setObjectName("window")

		# 상단 네비게이션 레이아웃
		self.navHbox = QHBoxLayout()
		self.navHbox.setContentsMargins(0, 0, 0, 0)
		self.navHbox.setSpacing(0)
		self.navHbox.move(0, 0)

		self.navMark = QLabel("ORIGAMI")
		self.navMark.setAlignment(Qt.AlignVCenter)
		self.navMark.setFont(QFont("Black Han Sans"))
		self.navMark.setObjectName("mark")

		self.camCombo = QComboBox(self)
		self.camCombo.addItem("캠 설정")
		self.camCombo.addItem("녹화")
		self.camCombo.addItem("흑백")

		self.gpsCombo = QComboBox(self)
		self.gpsCombo.addItem("GPS 설정")
		self.gpsCombo.addItem("트랙킹")

		self.logCombo = QComboBox(self)
		self.logCombo.addItem("로그 설정")
		self.logCombo.addItem("보기")

		self.navHbox.addWidget(self.navMark)
		self.navHbox.addWidget(self.camCombo)
		self.navHbox.addWidget(self.gpsCombo)
		self.navHbox.addWidget(self.logCombo)

		# 컨텍츠 레이아웃
		self.contextVbox = QVBoxLayout()
		self.contextVbox.setContentsMargins(10, 20, 20, 10)
		self.contextVbox.addLayout(self.navHbox)

		self.windowVbox.addWidget(self.titlebarWidget)
		self.windowVbox.addLayout(self.contextVbox)
		self.setLayout(self.windowVbox)

		self.showFullScreen()

	def setStyle(self):
		self.styleSheet = """
			QWidget {
	            background-color: #153450;
	        }
		"""
		self.setStyleSheet(self.styleSheet)

	def closeEvent(self, e):
		pass


class TitleBar(QWidget):
	def __init__(self, widget, parent):
		super(TitleBar, self).__init__()
		self.widget = widget
		self.parent = parent

		self.bar_height = 36
		self.has_clicked = False
		self.is_maximized = False

		self.initUI()
		self.setStyle()

	def initUI(self):
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0,0,0,0)
		self.layout.setSpacing(0)

		self.titleStr = self.parent
		self.label = QLabel(self.titleStr)
		self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		self.label.setFixedHeight(self.bar_height)
		self.label.setObjectName("titleSpace")

		self.btn_close = self.create_tool_btn("close.png")
		self.btn_close.setObjectName("closeBtn")
		self.btn_close.clicked.connect(self.close)

		self.layout.addWidget(self.label)
		self.layout.addWidget(self.btn_close)

	def setStyle(self):
		self.styleSheet = """
	        QWidget {
	        	color: #FFFFFF;
	        	background-color: #3C4043;
	            height: 32px;
	        }
	        QLabel#titleSpace {
	            color: rgb(255, 255, 255);
	            background-color: #3C4043;
	            font-size: 16px;
	            padding: 5px 5px;
	        }
	        QToolButton#closeBtn{
	        	background: transparent;
	        	background-color: #3C4043;
	        }
	        QToolButton#closeBtn:pressed {
	            background-color: rgb(255, 0, 0);
	        }
	        QToolButton#closeBtn:hover{
            	background-color: rgb(255, 0, 0);
        	}
	    """
		self.setStyleSheet(self.styleSheet)

	def create_tool_btn(self, icon_path):
		root_path = os.path.dirname(os.path.abspath(__file__))
		icon = os.path.join(root_path, "icon", icon_path)

		btn = QToolButton(self)
		btn.setIcon(QIcon(icon))
		btn.setIconSize(QSize(self.bar_height, self.bar_height))
		btn.setFixedSize(self.bar_height, self.bar_height)

		return btn

	def close(self):
		self.widget.close()



if __name__ == "__main__":
	app = QApplication(sys.argv)

	main = Main()
	sys.exit(app.exec_())