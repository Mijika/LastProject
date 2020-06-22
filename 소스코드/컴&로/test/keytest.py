import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Main(QWidget):
	def __init__(self):
		super(Main, self).__init__()

		self.setWindowTitle('key')
		self.resize(320, 240)
		self.show()

		self.duplicateCheck = []

		self.printable = [
				Qt.Key_Space,
				Qt.Key_Exclam,
				Qt.Key_QuoteDbl,
				Qt.Key_NumberSign,
				Qt.Key_Dollar,
				Qt.Key_Percent,
				Qt.Key_Ampersand,
				Qt.Key_Apostrophe,
				Qt.Key_ParenLeft,
				Qt.Key_ParenRight,
				Qt.Key_Asterisk,
				Qt.Key_Plus,
				Qt.Key_Comma,
				Qt.Key_Minus,
				Qt.Key_Period,
				Qt.Key_Slash,
				Qt.Key_0,
				Qt.Key_1,
				Qt.Key_2,
				Qt.Key_3,
				Qt.Key_4,
				Qt.Key_5,
				Qt.Key_6,
				Qt.Key_7,
				Qt.Key_8,
				Qt.Key_9,
				Qt.Key_Colon,
				Qt.Key_Semicolon,
				Qt.Key_Less,
				Qt.Key_Equal,
				Qt.Key_Greater,
				Qt.Key_Question,
				Qt.Key_At,
				Qt.Key_A,
				Qt.Key_B,
				Qt.Key_C,
				Qt.Key_D,
				Qt.Key_E,
				Qt.Key_F,
				Qt.Key_G,
				Qt.Key_H,
				Qt.Key_I,
				Qt.Key_J,
				Qt.Key_K,
				Qt.Key_L,
				Qt.Key_M,
				Qt.Key_N,
				Qt.Key_O,
				Qt.Key_P,
				Qt.Key_Q,
				Qt.Key_R,
				Qt.Key_S,
				Qt.Key_T,
				Qt.Key_U,
				Qt.Key_V,
				Qt.Key_W,
				Qt.Key_X,
				Qt.Key_Y,
				Qt.Key_Z,
				Qt.Key_BracketLeft,
				Qt.Key_Backslash,
				Qt.Key_BracketRight,
				Qt.Key_AsciiCircum,
				Qt.Key_Underscore,
				Qt.Key_QuoteLeft,
				Qt.Key_BraceLeft,
				Qt.Key_Bar,
				Qt.Key_BraceRight,
				Qt.Key_AsciiTilde,
			]

		self.a = 1

	def keyReleaseEvent(self, e):
		if e.key() in self.duplicateCheck:
			self.duplicateCheck.remove(e.key())
		else:
			return
		print(self.a)
		self.a += 1
		print(e.text(), "-")

	def keyPressEvent(self, e):
		if e.key() in self.duplicateCheck:
			return

		def isPrintable(key):
			if key in self.printable:
				return True
			else:
				return False

		control = False

		if e.modifiers() & Qt.ControlModifier:
			print('Control')
			return

		if e.modifiers() & Qt.ShiftModifier:
			print('Shift')
			return

		if e.modifiers() & Qt.AltModifier:
			print('Alt')
			return

		if e.key() == Qt.Key_Delete:
			print('Delete')
			return

		elif e.key() == Qt.Key_Backspace:
			print('Backspace')
			return

		elif e.key() in [Qt.Key_Return, Qt.Key_Enter]:
			print('Enter')
			return

		elif e.key() == Qt.Key_Escape:
			print('Escape')
			return

		elif e.key() == Qt.Key_Right:
			print('Right')
			return

		elif e.key() == Qt.Key_Left:
			print('Left')
			return

		elif e.key() == Qt.Key_Up:
			print('Up')
			return

		elif e.key() == Qt.Key_Down:
			print('Down')
			return

		if not control and isPrintable(e.key()):
			self.duplicateCheck.append(e.key())
			print(e.text(), "+")


if __name__ == '__main__':
	app = QApplication(sys.argv)

	win = Main()
	sys.exit(app.exec_())
