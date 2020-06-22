import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QImage

class MainWindowBase:
	def _initUi(self):
		self.setupUi()
		self.buttonNormal.setVisible(False)

		self.widgetMain.installEventFilter(self)

	def _initSignals(self):
		pass


	# 버튼의 오브젝트 네임과 함수 명이 자동적으로 매칭되서;; 연결이 되는 것 같다...
	# ex) self.buttonNormal.setObjectName("buttonNormal")
	# 	  on_"buttonNormal"_clicked
	@pyqtSlot()
	def on_buttonMinimum_clicked(self):
		self.showMinimized()

	@pyqtSlot()
	def on_buttonMaximum_clicked(self):
		self.showMaximized()

	@pyqtSlot()
	def on_buttonNormal_clicked(self):
		self.showNormal()

	@pyqtSlot()
	def on_buttonClose_clicked(self):
		self.close()

	@pyqtSlot(QImage)
	def recvImage(self, img):
		self.labelCam.setPixmap(QPixmap.fromImage(img))

	@pyqtSlot(str)
	def recvGPS(self, html):
		self.webEngine.setHtml(html)