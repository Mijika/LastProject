"""
Created on 2020.05.19
@author: 안담기
@email: sbahn42@gmail.com
@file: OrigamiServer
"""

import os
import sys
import traceback


__author__ = "안담기"
__Copyright__ = 'Copyright (c) 2020 Irony'
__Version__ = 1.0


def escape(s):
	s = s.replace("&", "&amp;")
	s = s.replace("<", "&lt;")
	s = s.replace(">", "&gt;")
	s = s.replace('"', "&quot;")
	s = s.replace('\'', "&#x27;")
	s = s.replace('\n', '<br/>')
	s = s.replace(' ', '&nbsp;')
	return s

def showError(message):
	from PyQt5.QtWidgets import QApplication, QErrorMessage, QCheckBox, \
		QPushButton, QLabel, QStyle
	from PyQt5.QtCore import Qt
	app = QApplication(sys.argv)

	# 아이콘 설정
	app.setWindowIcon(app.style().standardIcon(QStyle.SP_MessageBoxCritical))
	w = QErrorMessage()
	w.finished.connect(lambda _: app.quit)
	w.resize(800, 400)

	# 아이콘과 이름 정함
	w.setWindowFlags(w.windowFlags() & ~Qt.WindowContextHelpButtonHint)
	w.setWindowTitle(w.tr('Error'))

	# 에러 위젯에서 마크와 체크바 없에기
	w.findChild(QLabel, '').setVisible(False)
	w.findChild(QCheckBox, '').setVisible(False)
	# w.findChild(QPushButton, '').setVisible(False)
	w.showMessage(escape(message))
	sys.exit(app.exec_())


try:
	from Widgets import MainWindow
	MainWindow.main()
except SystemExit:
	pass
except:
	showError(traceback.format_exc())
