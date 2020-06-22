# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import os

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import QtWebEngineWidgets

from PyQt5.QtCore import Qt, QEvent, QSize
from PyQt5.QtGui import QPainter, QPen, QColor, QIcon
from PyQt5.QtWidgets import QWidget

class Ui_MainForm(QtWidgets.QWidget):
	MARGIN = 2

	def setupUi(self):
		self.setObjectName("MainForm")
		self.resize(800, 600)
		self.setMinimumSize(QtCore.QSize(800, 600))
		self.setFocusPolicy(QtCore.Qt.StrongFocus)

		#윈도우 위젯, 레이아웃
		self.widgetMain = QtWidgets.QWidget(self)
		self.widgetMain.setObjectName("widgetMain")
		self.HLayoutMainForm = QtWidgets.QHBoxLayout(self)
		self.HLayoutMainForm.setContentsMargins(0, 0, 0, 0)
		self.HLayoutMainForm.setSpacing(0)
		self.HLayoutMainForm.setObjectName("HLayoutMainForm")

		#메인 위젯, 레이아웃
		self.widgetMain.setObjectName("widgetMain")
		self.VLayoutMain = QtWidgets.QVBoxLayout(self.widgetMain)
		self.VLayoutMain.setContentsMargins(0, 0, 0, 0)
		self.VLayoutMain.setSpacing(0)
		self.VLayoutMain.setObjectName("VLayoutMain")

		##타이틀 위젯, 레이아웃
		self.widgetTitlebar = QtWidgets.QWidget(self.widgetMain)
		self.widgetTitlebar.setObjectName("widgetTitlebar")

		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.widgetTitlebar.sizePolicy().hasHeightForWidth())
		self.widgetTitlebar.setSizePolicy(sizePolicy)

		self.HLayoutTitlebar = QtWidgets.QHBoxLayout(self.widgetTitlebar)
		self.HLayoutTitlebar.setContentsMargins(0, 0, 0, 0)
		self.HLayoutTitlebar.setSpacing(2)
		self.HLayoutTitlebar.setObjectName("HLayoutTitlebar")

		self.Titlebarspacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

		self.buttonMinimum = QtWidgets.QPushButton(self.widgetTitlebar)
		self.buttonMinimum.setText("")
		self.buttonMinimum.setObjectName("buttonMinimum")

		self.buttonMaximum = QtWidgets.QPushButton(self.widgetTitlebar)
		self.buttonMaximum.setText("")
		self.buttonMaximum.setObjectName("buttonMaximum")

		self.buttonNormal = QtWidgets.QPushButton(self.widgetTitlebar)
		self.buttonNormal.setText("")
		self.buttonNormal.setObjectName("buttonNormal")

		self.buttonClose = QtWidgets.QPushButton(self.widgetTitlebar)
		self.buttonClose.setText("")
		self.buttonClose.setObjectName("buttonClose")

		self.HLayoutTitlebar.addItem(self.Titlebarspacer)
		self.HLayoutTitlebar.addWidget(self.buttonMinimum)
		self.HLayoutTitlebar.addWidget(self.buttonMaximum)
		self.HLayoutTitlebar.addWidget(self.buttonNormal)
		self.HLayoutTitlebar.addWidget(self.buttonClose)
		self.VLayoutMain.addWidget(self.widgetTitlebar)


		##센터 위젯, 레이아웃
		self.widgetCenter = QtWidgets.QWidget(self.widgetMain)
		self.widgetCenter.setObjectName("widgetCenter")

		self.VLayoutCenter = QtWidgets.QVBoxLayout(self.widgetCenter)
		self.VLayoutCenter.setContentsMargins(30, 30, 30, 50)
		self.VLayoutCenter.setSpacing(20)
		self.VLayoutCenter.setObjectName("VLayoutCenter")

		###센터 메뉴 위젯, 레이아웃
		self.widgetMeun = QtWidgets.QWidget(self.widgetCenter)
		self.widgetMeun.setMinimumSize(QtCore.QSize(0, 50))
		self.widgetMeun.setMaximumSize(QtCore.QSize(16777215, 60))
		self.widgetMeun.setObjectName("widgetMeun")

		self.HlayoutMeun = QtWidgets.QHBoxLayout(self.widgetMeun)
		self.HlayoutMeun.setContentsMargins(0, 0, 0, 0)
		self.HlayoutMeun.setSpacing(0)
		self.HlayoutMeun.setObjectName("HlayoutMeun")

		####로고 레이블
		self.labelLogo = QtWidgets.QLabel(self.widgetMeun)
		self.labelLogo.setMinimumSize(QtCore.QSize(190, 0))
		self.labelLogo.setMaximumSize(QtCore.QSize(200, 16777215))
		font = QtGui.QFont()
		font.setFamily("Black Han Sans")
		font.setPointSize(24)
		font.setStyleStrategy(QtGui.QFont.PreferDefault)
		self.labelLogo.setFont(font)
		self.labelLogo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		self.labelLogo.setMouseTracking(False)
		self.labelLogo.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.labelLogo.setAutoFillBackground(False)
		self.labelLogo.setAlignment(QtCore.Qt.AlignCenter)
		self.labelLogo.setObjectName("labelLogo")
		self.HlayoutMeun.addWidget(self.labelLogo)

		####센터 메뉴 콤보 박스 위젯, 레이아웃
		self.widgetComboBox = QtWidgets.QWidget(self.widgetMeun)
		self.widgetComboBox.setObjectName("widgetComboBox")

		self.HLayoutComboBox = QtWidgets.QHBoxLayout(self.widgetComboBox)
		self.HLayoutComboBox.setContentsMargins(20, 0, 20, 0)
		self.HLayoutComboBox.setSpacing(10)
		self.HLayoutComboBox.setObjectName("HLayoutComboBox")

		self.comboBoxRobot = QtWidgets.QComboBox(self.widgetComboBox)
		self.comboBoxRobot.setFrame(True)
		self.comboBoxRobot.setObjectName("comboBoxRobot")
		self.comboBoxRobot.addItem("")
		self.comboBoxRobot.addItem("")
		self.comboBoxRobot.addItem("")
		self.comboBoxSet(self.comboBoxRobot)
		self.HLayoutComboBox.addWidget(self.comboBoxRobot)

		self.comboBoxCam = QtWidgets.QComboBox(self.widgetComboBox)
		self.comboBoxCam.setObjectName("comboBoxCam")
		self.comboBoxCam.addItem("")
		self.comboBoxCam.addItem("")
		self.comboBoxCam.addItem("")
		self.comboBoxCam.addItem("")
		self.comboBoxSet(self.comboBoxCam)
		self.HLayoutComboBox.addWidget(self.comboBoxCam)

		self.comboBoxGPS = QtWidgets.QComboBox(self.widgetComboBox)
		self.comboBoxGPS.setObjectName("comboBoxGPS")
		self.comboBoxGPS.addItem("")
		self.comboBoxGPS.addItem("")
		self.comboBoxGPS.addItem("")
		self.comboBoxSet(self.comboBoxGPS)
		self.HLayoutComboBox.addWidget(self.comboBoxGPS)

		self.comboBoxLog = QtWidgets.QComboBox(self.widgetComboBox)
		self.comboBoxLog.setObjectName("comboBoxLog")
		self.comboBoxLog.addItem("")
		self.comboBoxLog.addItem("")
		self.comboBoxLog.addItem("")
		self.comboBoxSet(self.comboBoxLog)
		self.HLayoutComboBox.addWidget(self.comboBoxLog)

		self.comboBoxHelp = QtWidgets.QComboBox(self.widgetComboBox)
		self.comboBoxHelp.setObjectName("comboBoxHelp")
		self.comboBoxHelp.addItem("")
		self.comboBoxHelp.addItem("")
		self.comboBoxHelp.addItem("")
		self.comboBoxSet(self.comboBoxHelp)
		self.HLayoutComboBox.addWidget(self.comboBoxHelp)

		self.HlayoutMeun.addWidget(self.widgetComboBox)
		self.VLayoutCenter.addWidget(self.widgetMeun)

		### 센터 컨텐츠 위젯, 레이아웃
		self.widgetContents = QtWidgets.QWidget(self.widgetCenter)
		self.widgetContents.setObjectName("widgetContents")

		self.HLayoutContents = QtWidgets.QHBoxLayout(self.widgetContents)
		self.HLayoutContents.setContentsMargins(0, 0, 0, 0)
		self.HLayoutContents.setSpacing(20)
		self.HLayoutContents.setObjectName("HLayoutContents")

		#### 컨텐츠 캠 레이블
		self.labelCam = QtWidgets.QLabel(self.widgetContents)
		self.labelCam.setMinimumSize(QtCore.QSize(400, 400))
		self.labelCam.setObjectName("labelCam")
		self.HLayoutContents.addWidget(self.labelCam)

		#### 컨텐츠 디테일 위젯, 레이아웃
		self.widgetContentsDitali = QtWidgets.QWidget(self.widgetContents)
		self.widgetContentsDitali.setObjectName("widgetContentsDitali")

		self.VLayoutContentsDitali = QtWidgets.QVBoxLayout(self.widgetContentsDitali)
		self.VLayoutContentsDitali.setContentsMargins(0, 0, 0, 0)
		self.VLayoutContentsDitali.setSpacing(20)
		self.VLayoutContentsDitali.setObjectName("VLayoutContentsDitali")

		self.webEngine = QtWebEngineWidgets.QWebEngineView(self.widgetContentsDitali)
		self.webEngine.setMinimumSize(QtCore.QSize(100, 100))
		self.webEngine.setObjectName("webEngine")
		self.VLayoutContentsDitali.addWidget(self.webEngine)

		self.labelState = QtWidgets.QLabel(self.widgetContentsDitali)
		self.labelState.setMinimumSize(QtCore.QSize(100, 50))
		self.labelState.setMaximumSize(QtCore.QSize(16777215, 120))
		self.labelState.setObjectName("labelState")
		self.VLayoutContentsDitali.addWidget(self.labelState)

		self.HLayoutContents.addWidget(self.widgetContentsDitali)
		self.VLayoutCenter.addWidget(self.widgetContents)
		self.VLayoutMain.addWidget(self.widgetCenter)
		self.HLayoutMainForm.addWidget(self.widgetMain)

		self.retranslateUi()
		self.setWidgetStyleSheet()
		self.titleButIconSet()
		QtCore.QMetaObject.connectSlotsByName(self)

	def comboBoxSet(self, comboBox):
		comboBox.setFont(QtGui.QFont('맑은 고딕', 12))
		comboBox.setEditable(True)
		comboBox.lineEdit().setReadOnly(True)
		for i in range(comboBox.count()):
			comboBox.setItemData(i, Qt.AlignCenter, Qt.TextAlignmentRole)

	def titleButIconSet(self):
		iconPath = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), "Resources", "Images", "Icon")
		self.buttonMinimum.setIcon(QIcon(os.path.join(iconPath, "minimize.PNG")))
		self.buttonMaximum.setIcon(QIcon(os.path.join(iconPath, "middle.PNG")))
		self.buttonNormal.setIcon(QIcon(os.path.join(iconPath, "middle.PNG")))
		self.buttonClose.setIcon(QIcon(os.path.join(iconPath, "close.PNG")))

		self.buttonMinimum.setIconSize(QSize(36, 36))
		self.buttonMaximum.setIconSize(QSize(36, 36))
		self.buttonNormal.setIconSize(QSize(36, 36))
		self.buttonClose.setIconSize(QSize(36, 36))

	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.setWindowTitle(_translate("MainForm", "Form"))
		self.labelLogo.setText(_translate("MainForm", "ORIGAMI"))
		self.comboBoxRobot.setCurrentText(_translate("MainForm", "로봇"))
		self.comboBoxRobot.setItemText(0, _translate("MainForm", "로봇"))
		self.comboBoxRobot.setItemText(1, _translate("MainForm", "로봇 연결"))
		self.comboBoxRobot.setItemText(2, _translate("MainForm", "로봇 설정"))
		self.comboBoxCam.setItemText(0, _translate("MainForm", "CAM"))
		self.comboBoxCam.setItemText(1, _translate("MainForm", "CAM 설정"))
		self.comboBoxCam.setItemText(2, _translate("MainForm", "녹화"))
		self.comboBoxCam.setItemText(3, _translate("MainForm", "흑백"))
		self.comboBoxGPS.setItemText(0, _translate("MainForm", "GPS"))
		self.comboBoxGPS.setItemText(1, _translate("MainForm", "GPS 설정"))
		self.comboBoxGPS.setItemText(2, _translate("MainForm", "트랙킹"))
		self.comboBoxLog.setItemText(0, _translate("MainForm", "로그"))
		self.comboBoxLog.setItemText(1, _translate("MainForm", "로그 설정"))
		self.comboBoxLog.setItemText(2, _translate("MainForm", "로그 보기"))
		self.comboBoxHelp.setItemText(0, _translate("MainForm", "도움말"))
		self.comboBoxHelp.setItemText(1, _translate("MainForm", "도움말"))
		self.comboBoxHelp.setItemText(2, _translate("MainForm", "단축키"))
		self.labelCam.setText(_translate("MainForm", "Cam img"))
		self.labelState.setText(_translate("MainForm", "robot state"))

	def setWidgetStyleSheet(self):
		styleSheet = """
			#widgetMain {
				border-radius: 4px;
				background-color: rgb(52, 61, 70);
			}

			#widgetTitlebar {
				min-height: 36px;
				max-height: 36px;
				border-top-right-radius: 4px;
				border-top-left-radius: 4px;
				background-color: rgb(33, 33, 33);
			}

			#buttonMinimum, #buttonMaximum, #buttonNormal, #buttonClose {
				/*定义最小最大宽高*/
				min-width: 36px;
				max-width: 36px;
				min-height: 36px;
				max-height: 36px;
				border: none;
				color: white;   /*文字颜色*/
				font-size: 16px;
				font-size: 16px;
			}

			#buttonMinimum:hover, #buttonMaximum:hover, #buttonNormal:hover, #buttonClose:hover {
				background-color: rgba(255, 255, 255, 100); /*带透明度白色背景*/
			}

			#buttonClose:hover {
			    background-color: rgba(212, 64, 39, 255); /*红色*/
			}

			#buttonClose {
			    border-top-right-radius: 4px;
			}

			#widgetComboBox {
				background-color: rgb(68, 114, 148);
			}
			#labelLogo {
				color: rgb(211, 150, 0);
				background-color: rgb(41, 64, 82);
			}
			#labelCam {
				background-color: rgb(68, 114, 196);
			}
			#webEngine {
				background-color: rgb(3, 137, 255);
			}
			#labelState {
				background-color: rgb(180, 180, 180);
			}

			QComboBox {
				border: 1px solid gray;
				border-radius: 3px;
				padding: 1px 18px 1px 3px;
				min-width: 6em;
			}
			QComboBox:editable {
				background: #FFFFFF
			}
			QComboBox:!editable, QComboBox::drop-down:editable {
				 background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
											 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
											 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
			}
			/* QComboBox gets the "on" state when the popup is open */
			QComboBox:!editable:on, QComboBox::drop-down:editable:on {
				background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
											stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
											stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
			}
			QComboBox:on { /* shift the text when the popup opens */
				padding-top: 3px;
				padding-left: 4px;
			}
			QComboBox::drop-down {
				subcontrol-origin: padding;
				subcontrol-position: top right;
				width: 15px;

				border-left-width: 1px;
				border-left-color: darkgray;
				border-left-style: solid; /* just a single line */
				border-top-right-radius: 3px; /* same radius as the QComboBox */
				border-bottom-right-radius: 3px;
			}
			QComboBox::down-arrow:on { /* shift the arrow when popup is open */
				top: 1px;
				left: 1px;
			}
			QComboBox QAbstractItemView {
				border: 2px solid darkgray;
				selection-background-color: lightgray;
			}
		"""

		self.setStyleSheet(styleSheet)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ui = Ui_MainForm()
	ui.setupUi()
	ui.show()
	sys.exit(app.exec_())
