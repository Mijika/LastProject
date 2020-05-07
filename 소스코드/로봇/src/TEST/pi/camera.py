from threading import Thread
import time

import cv2

from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Video(QObject):
	sendImage = pyqtSignal(QImage)

	def __init__(self, parent=None):
		super().__init__()
		self.flag = False
		self.parent = parent
		self.size = (480, 240)
		self.sendImage.connect(self.parent.recvImage)

	def videoInit(self):
		try:
			self.cap = cv2.VideoCapture("0", cv2.CAP_DSHOW)
			self.capWidth = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
			self.capHeight = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
			print(str(self.capWidth) + str(self.capHeight))

		except Exception as e:
			print("Cam Error : ", e)

	def startCam(self):
		self.flag = True
		self.videoInit()

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
			print("Error cam not opend" + str(e))
		else:
			self.cap.release()

	def threadFunc(self):
		while self.bThread:
			ok, frame = self.cap.read()

			if ok:
				rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
				h, w, ch = rgb.shape
				bytesPerLine = ch * w
				img = QImage(rgb.data, w, h, bytesPerLine, QImage.Format_RGB888)
				resizedImg = img.scaled(self.size.widget(), self.size.height(), Qt.KeepAspectRatio)

				self.sendImage.emit(resizedImg)

			else:
				print("Cam read error")

			time.sleep(0.01)

		self.sendImage.emit(QImage())
		print('thread finished')
