import os
import sys

if __name__ == '__main__':
	sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QEvent, Qt, QSize, QTimer
from PyQt5.QtGui import QEnterEvent, QPainter, QPen, QColor

from UiFiles.MainForm import Ui_MainForm
from Widgets.MainWindowBase import MainWindowBase
from Widgets.FramelessWindow import FramelessWindow

from Function.Video import Video
from Function.GPS import GPS


class MainWindow(FramelessWindow, MainWindowBase, Ui_MainForm):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self._initUi()
		self._initSignals()

		self.video = Video(self, QSize(self.labelCam.width(), self.labelCam.height()))
		self.video.startCam()
		try:
			self.gps = GPS(self)
		except Exception as e:
			raise e

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setPen(QPen(QColor(255, 255, 255, 1), 3 * self.MARGIN))
		painter.drawRect(self.rect())

		self.video.setSize(QSize(self.labelCam.width(), self.labelCam.height()))

	def closeEvent(self, event):
		# 储存窗口位置
		self.video.stopCam()
		super(MainWindow, self).closeEvent(event)

	def eventFilter(self, obj, event):
		# 事件过滤器
		if obj == self.widgetMain and isinstance(event, QEnterEvent):
			# 用于解决鼠标进入其它控件后还原为标准鼠标样式
			self.setCursor(Qt.ArrowCursor)
		return FramelessWindow.eventFilter(self, obj, event)

	def changeEvent(self, event):
		# 窗口改变事件
		FramelessWindow.changeEvent(self, event)
		if event.type() == QEvent.WindowStateChange:  # 窗口状态改变
			state = self.windowState()
			if state == (state | Qt.WindowMaximized):
				# 最大化状态,显示还原按钮
				self.buttonMaximum.setVisible(False)
				self.buttonNormal.setVisible(True)
			else:
				# 隐藏还原按钮
				self.buttonMaximum.setVisible(True)
				self.buttonNormal.setVisible(False)


def main():
	app = QApplication(sys.argv)
	w = MainWindow()
	w.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()