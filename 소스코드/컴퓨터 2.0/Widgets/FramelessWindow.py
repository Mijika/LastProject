from PyQt5.QtCore import Qt, QEvent, QRect
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget

Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)

class FramelessWindow(QWidget):

	MARGIN = 2

	def __init__(self, *args, **kwargs):
		super(FramelessWindow, self).__init__(*args, **kwargs)
		self._pos = None  # 마우스 좌표
		self._pressed = False  # 현재 마우스를 누르고 있는가
		self._canmove = False  # 可以移动
		self.Direction = None  # 光标方向
		# 계속해서 마우스 좌표를 확인
		self.setMouseTracking(True)
		# 알파값 있는 위젯을 사용
		self.setAttribute(Qt.WA_TranslucentBackground, True)
		# 윈도우 타이블바 제거
		self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

	def mousePressEvent(self, event):
		# 마우스 좌클릭을 했을때
		super(FramelessWindow, self).mousePressEvent(event)
		if event.buttons() == Qt.LeftButton:
			self._pos = event.pos()
			self._pressed = True
			if self.childAt(self._pos) != None:
				# 마우스가 위젯을 클릭 했을때
				self._canmove = True

	def mouseReleaseEvent(self, event):
		# 마우스에서 클릭을 놓았을때 발생
		super(FramelessWindow, self).mouseReleaseEvent(event)
		self._pressed = False
		self._canmove = False
		self.Direction = None

	def mouseDoubleClickEvent(self, event):
		# 커졌다 작았짐
		super(FramelessWindow, self).mouseDoubleClickEvent(event)
		if event.buttons() == Qt.LeftButton:
			if self.childAt(self._pos) != None:
				# 이 프로그램 위젯 위에서 더블클릭했을때 발생
				if self.isMaximized() or self.isFullScreen():
					self.showNormal()
				else:
					self.showMaximized()

	def mouseMoveEvent(self, event):
		# 鼠标移动事件
		super(FramelessWindow, self).mouseMoveEvent(event)

		pos = event.pos()
		xPos, yPos = pos.x(), pos.y()
		wm, hm = self.width() - self.MARGIN, self.height() - self.MARGIN
		if self.isMaximized() or self.isFullScreen():
			# 最大化或者全屏则忽略
			self.Direction = None
			self.setCursor(Qt.ArrowCursor)
			return
		if self._canmove:
			self.move(self.mapToGlobal(event.pos() - self._pos))
			return
		if event.buttons() == Qt.LeftButton and self._pressed:
			self._resizeWidget(pos)
			return
		if xPos <= self.MARGIN and yPos <= self.MARGIN:
			# 左上角
			self.Direction = LeftTop
			self.setCursor(Qt.SizeFDiagCursor)
		elif wm <= xPos <= self.width() and hm <= yPos <= self.height():
			# 右下角
			self.Direction = RightBottom
			self.setCursor(Qt.SizeFDiagCursor)
		elif wm <= xPos and yPos <= self.MARGIN:
			# 右上角
			self.Direction = RightTop
			self.setCursor(Qt.SizeBDiagCursor)
		elif xPos <= self.MARGIN and hm <= yPos:
			# 左下角
			self.Direction = LeftBottom
			self.setCursor(Qt.SizeBDiagCursor)
		elif 0 <= xPos <= self.MARGIN and self.MARGIN <= yPos <= hm:
			# 左边
			self.Direction = Left
			self.setCursor(Qt.SizeHorCursor)
		elif wm <= xPos <= self.width() and self.MARGIN <= yPos <= hm:
			# 右边
			self.Direction = Right
			self.setCursor(Qt.SizeHorCursor)
		elif self.MARGIN <= xPos <= wm and 0 <= yPos <= self.MARGIN:
			# 上面
			self.Direction = Top
			self.setCursor(Qt.SizeVerCursor)
		elif self.MARGIN <= xPos <= wm and hm <= yPos <= self.height():
			# 下面
			self.Direction = Bottom
			self.setCursor(Qt.SizeVerCursor)

	def leaveEvent(self, event):
		# 鼠标离开事件
		self.setCursor(Qt.ArrowCursor)  # 恢复鼠标形状
		super(FramelessWindow, self).leaveEvent(event)

	def changeEvent(self, event):
		# 窗口改变事件
		super(FramelessWindow, self).changeEvent(event)
		if event.type() == QEvent.WindowStateChange:  # 窗口状态改变
			state = self.windowState()
			if state == (state | Qt.WindowMaximized):
				# 最大化,要去除上下左右边界,如果不去除则边框地方会有空隙
				self.layout().setContentsMargins(0, 0, 0, 0)
			else:
				# 要保留上下左右边界,否则没有边框无法调整
				self.layout().setContentsMargins(
					self.MARGIN, self.MARGIN, self.MARGIN, self.MARGIN)

	def move(self, pos):
		if self.windowState() == Qt.WindowMaximized or self.windowState() == Qt.WindowFullScreen:
			# 最大化或者全屏则不允许移动
			return
		super(FramelessWindow, self).move(pos)

	def _resizeWidget(self, pos):
		# 调整窗口大小
		if self.Direction == None:
			return
		mpos = pos - self._pos
		xPos, yPos = mpos.x(), mpos.y()
		geometry = self.geometry()
		x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
		if self.Direction == LeftTop:  # 左上角
			if w - xPos > self.minimumWidth():
				x += xPos
				w -= xPos
			if h - yPos > self.minimumHeight():
				y += yPos
				h -= yPos
		elif self.Direction == RightBottom:  # 右下角
			if w + xPos > self.minimumWidth():
				w += xPos
				self._pos = pos
			if h + yPos > self.minimumHeight():
				h += yPos
				self._pos = pos
		elif self.Direction == RightTop:  # 右上角
			if h - yPos > self.minimumHeight():
				y += yPos
				h -= yPos
			if w + xPos > self.minimumWidth():
				w += xPos
				self._pos.setX(pos.x())
		elif self.Direction == LeftBottom:  # 左下角
			if w - xPos > self.minimumWidth():
				x += xPos
				w -= xPos
			if h + yPos > self.minimumHeight():
				h += yPos
				self._pos.setY(pos.y())
		elif self.Direction == Left:  # 左边
			if w - xPos > self.minimumWidth():
				x += xPos
				w -= xPos
			else:
				return
		elif self.Direction == Right:  # 右边
			if w + xPos > self.minimumWidth():
				w += xPos
				self._pos = pos
			else:
				return
		elif self.Direction == Top:  # 上面
			if h - yPos > self.minimumHeight():
				y += yPos
				h -= yPos
			else:
				return
		elif self.Direction == Bottom:  # 下面
			if h + yPos > self.minimumHeight():
				h += yPos
				self._pos = pos
			else:
				return
		self.setGeometry(x, y, w, h)
