import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class TitleBar(QWidget):
    """제목 표시줄 위젯"""
    qss = """
        QWidget {
            color: #FFFFFF;
            background: #3C4043;
            height: 32px;
        }
        QLabel {
            color: #FFFFFF;
            background: #3C4043;
            font-size: 16px;
            padding: 5px 5px;
        }
        QToolButton{
            border-radius: 0px
        }
        QToolButton:hover{
            border-radius: 0px
            background: #505558;
        }
    """

    def __init__(self, parent, arg):
        super().__init__()
        self.parent = parent
        self.arg = arg

        self.bar_height = 36
        self.btn_height = 36
        self.has_clicked = False
        self.is_maximized = False

        self.setStyleSheet(self.qss)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.labelName = "            " + self.arg

        self.label = QLabel(self.labelName)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedHeight(self.bar_height)
        self.btn_minimize = self.create_tool_btn('minimize.PNG')
        self.btn_minimize.clicked.connect(self.show_minimized)
        self.btn_close = self.create_tool_btn('close.PNG')
        self.btn_close.clicked.connect(self.close)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn_minimize)
        self.layout.addWidget(self.btn_close)

    def create_tool_btn(self, icon_path):
        """제목표시줄 아이콘 생성"""
        icon = os.path.join(ROOT_PATH, "icon", icon_path)

        btn = QToolButton(self)
        btn.setIcon(QIcon(icon))
        btn.setIconSize(QSize(self.bar_height, self.bar_height))
        btn.setFixedSize(self.btn_height, self.btn_height)
        return btn

    def show_minimized(self):
        """버튼 명령: 최소화"""
        self.parent.showMinimized()

    def close(self):
        """버튼 명령: 닫기"""
        self.parent.close()

    def mousePressEvent(self, event):
        """오버로딩: 마우스 클릭 이벤트
        - 제목 표시줄 클릭시 이동 가능 플래그
        """
        if event.button() == Qt.LeftButton:
            self.parent.is_moving = True
            self.parent.offset = event.pos()

    def mouseMoveEvent(self, event):
        """오버로딩: 마우스 이동 이벤트
        - 제목 표시줄 드래그시 창 이동
        """
        try:
            if self.parent.is_moving:
                self.parent.move(event.globalPos() - self.parent.offset)
        except Exception as e:
            pass


class BasicWindow(QWidget):
    """docstring for BasicWindow"""

    def __init__(self, parent=None):
        super(BasicWindow, self).__init__(parent)
        self.size = QSize(600, 536)

        self.titlebar_name = "window"

    def basicUI(self):
        # 상단 테이블 바 없에는 플래그
        self.setWindowFlags(
            Qt.Window |
            Qt.CustomizeWindowHint |
            Qt.FramelessWindowHint
        )

        # 기본 타이틀 바와 레이아옷 선언
        self.window_vbox = QVBoxLayout(self)
        self.window_vbox.setContentsMargins(0, 0, 0, 0)
        self.titlebar_widget = TitleBar(self, self.titlebar_name)
        self.titlebar_widget.setObjectName("windowTitle")

        # 컨텍스 레이아웃
        self.Context_hbox = QHBoxLayout()
        self.Context_hbox.setContentsMargins(5, 5, 5, 5)

        # 버튼 레이아웃
        self.btn_vbox = QVBoxLayout()

        self.Context_hbox.addLayout(self.btn_vbox)

        self.window_vbox.addWidget(self.titlebar_widget)
        self.window_vbox.addLayout(self.Context_hbox)

        self.setLayout(self.window_vbox)
        self.resize(self.size)
        self.setFixedSize(self.size)

    def setTitleName(self, name):
        self.titlebar_name = name
