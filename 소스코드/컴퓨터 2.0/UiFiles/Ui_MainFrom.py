# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainFrom.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets

class Ui_FormMainwindow():
    def setupUi(self, FormMainwindow):
        FormMainwindow.setObjectName("FormMainwindow")
        FormMainwindow.resize(800, 600)
        FormMainwindow.setMinimumSize(QtCore.QSize(800, 600))
        FormMainwindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(FormMainwindow)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widgetMain = QtWidgets.QWidget(FormMainwindow)
        self.widgetMain.setStyleSheet("background-color: rgb(21, 52, 80);")
        self.widgetMain.setObjectName("widgetMain")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widgetMain)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widgetTitlebat = QtWidgets.QWidget(self.widgetMain)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetTitlebat.sizePolicy().hasHeightForWidth())
        self.widgetTitlebat.setSizePolicy(sizePolicy)
        self.widgetTitlebat.setMinimumSize(QtCore.QSize(0, 23))
        self.widgetTitlebat.setMaximumSize(QtCore.QSize(16777215, 23))
        self.widgetTitlebat.setObjectName("widgetTitlebat")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widgetTitlebat)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonNormal = QtWidgets.QPushButton(self.widgetTitlebat)
        self.buttonNormal.setText("")
        self.buttonNormal.setObjectName("buttonNormal")
        self.horizontalLayout.addWidget(self.buttonNormal)
        self.buttouMax = QtWidgets.QPushButton(self.widgetTitlebat)
        self.buttouMax.setText("")
        self.buttouMax.setObjectName("buttouMax")
        self.horizontalLayout.addWidget(self.buttouMax)
        self.buttonClose = QtWidgets.QPushButton(self.widgetTitlebat)
        self.buttonClose.setText("")
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout.addWidget(self.buttonClose)
        self.verticalLayout_2.addWidget(self.widgetTitlebat)
        self.widgetCenter = QtWidgets.QWidget(self.widgetMain)
        self.widgetCenter.setObjectName("widgetCenter")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widgetCenter)
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 50)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetMeun = QtWidgets.QWidget(self.widgetCenter)
        self.widgetMeun.setMinimumSize(QtCore.QSize(0, 50))
        self.widgetMeun.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widgetMeun.setObjectName("widgetMeun")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetMeun)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLogo = QtWidgets.QLabel(self.widgetMeun)
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
        self.labelLogo.setStyleSheet("color: rgb(211, 150, 0);\n"
"background-color: rgb(41, 64, 82);")
        self.labelLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogo.setObjectName("labelLogo")
        self.horizontalLayout_2.addWidget(self.labelLogo)
        self.widgetComboBox = QtWidgets.QWidget(self.widgetMeun)
        self.widgetComboBox.setStyleSheet("background-color: rgb(68, 114, 148);")
        self.widgetComboBox.setObjectName("widgetComboBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widgetComboBox)
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBoxRobot = QtWidgets.QComboBox(self.widgetComboBox)
        self.comboBoxRobot.setEditable(False)
        self.comboBoxRobot.setFrame(True)
        self.comboBoxRobot.setObjectName("comboBoxRobot")
        self.comboBoxRobot.addItem("")
        self.comboBoxRobot.addItem("")
        self.comboBoxRobot.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxRobot)
        self.comboBoxCam = QtWidgets.QComboBox(self.widgetComboBox)
        self.comboBoxCam.setObjectName("comboBoxCam")
        self.comboBoxCam.addItem("")
        self.comboBoxCam.addItem("")
        self.comboBoxCam.addItem("")
        self.comboBoxCam.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxCam)
        self.comboBoxGPS = QtWidgets.QComboBox(self.widgetComboBox)
        self.comboBoxGPS.setObjectName("comboBoxGPS")
        self.comboBoxGPS.addItem("")
        self.comboBoxGPS.addItem("")
        self.comboBoxGPS.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxGPS)
        self.comboBoxLog = QtWidgets.QComboBox(self.widgetComboBox)
        self.comboBoxLog.setObjectName("comboBoxLog")
        self.comboBoxLog.addItem("")
        self.comboBoxLog.addItem("")
        self.comboBoxLog.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxLog)
        self.comboBoxHelp = QtWidgets.QComboBox(self.widgetComboBox)
        self.comboBoxHelp.setObjectName("comboBoxHelp")
        self.comboBoxHelp.addItem("")
        self.comboBoxHelp.addItem("")
        self.comboBoxHelp.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxHelp)
        self.horizontalLayout_2.addWidget(self.widgetComboBox)
        self.verticalLayout_3.addWidget(self.widgetMeun)
        self.widgetContents = QtWidgets.QWidget(self.widgetCenter)
        self.widgetContents.setObjectName("widgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetContents)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelCam = QtWidgets.QLabel(self.widgetContents)
        self.labelCam.setMinimumSize(QtCore.QSize(400, 400))
        self.labelCam.setStyleSheet("background-color: rgb(68, 114, 196);")
        self.labelCam.setObjectName("labelCam")
        self.horizontalLayout_3.addWidget(self.labelCam)
        self.widgetcontentsDitali = QtWidgets.QWidget(self.widgetContents)
        self.widgetcontentsDitali.setObjectName("widgetcontentsDitali")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetcontentsDitali)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webEngine = QtWebEngineWidgets.QWebEngineView(self.widgetcontentsDitali)
        self.webEngine.setMinimumSize(QtCore.QSize(100, 100))
        self.webEngine.setStyleSheet("background-color: rgb(3, 137, 255);")
        self.webEngine.setObjectName("webEngine")
        self.verticalLayout.addWidget(self.webEngine)
        self.labelState = QtWidgets.QLabel(self.widgetcontentsDitali)
        self.labelState.setMinimumSize(QtCore.QSize(100, 40))
        self.labelState.setMaximumSize(QtCore.QSize(16777215, 120))
        self.labelState.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelState.setObjectName("labelState")
        self.verticalLayout.addWidget(self.labelState)
        self.horizontalLayout_3.addWidget(self.widgetcontentsDitali)
        self.verticalLayout_3.addWidget(self.widgetContents)
        self.verticalLayout_2.addWidget(self.widgetCenter)
        self.verticalLayout_4.addWidget(self.widgetMain)

        self.comboBoxCam.setStyleSheet("""
            QComboBox {
            border: 1px solid gray;
            border-radius: 3px;
            padding: 1px 18px 1px 3px;
            min-width: 6em;
        }

        QComboBox:editable {
            background: white;
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

        QComboBox::down-arrow {
            image: url(/usr/share/icons/crystalsvg/16x16/actions/1downarrow.png);
        }

        QComboBox::down-arrow:on { /* shift the arrow when popup is open */
            top: 1px;
            left: 1px;
        }
        QComboBox QAbstractItemView {
            border: 2px solid darkgray;
            selection-background-color: lightgray;
        }
        """)

        self.retranslateUi(FormMainwindow)
        QtCore.QMetaObject.connectSlotsByName(FormMainwindow)

    def retranslateUi(self, FormMainwindow):
        _translate = QtCore.QCoreApplication.translate
        FormMainwindow.setWindowTitle(_translate("FormMainwindow", "Form"))
        self.labelLogo.setText(_translate("FormMainwindow", "ORIGAMI"))
        self.comboBoxRobot.setCurrentText(_translate("FormMainwindow", "로봇"))
        self.comboBoxRobot.setItemText(0, _translate("FormMainwindow", "로봇"))
        self.comboBoxRobot.setItemText(1, _translate("FormMainwindow", "로봇 연결"))
        self.comboBoxRobot.setItemText(2, _translate("FormMainwindow", "로봇 설정"))
        self.comboBoxCam.setItemText(0, _translate("FormMainwindow", "CAM"))
        self.comboBoxCam.setItemText(1, _translate("FormMainwindow", "CAM 설정"))
        self.comboBoxCam.setItemText(2, _translate("FormMainwindow", "녹화"))
        self.comboBoxCam.setItemText(3, _translate("FormMainwindow", "흑백"))
        self.comboBoxGPS.setItemText(0, _translate("FormMainwindow", "GPS"))
        self.comboBoxGPS.setItemText(1, _translate("FormMainwindow", "GPS 설정"))
        self.comboBoxGPS.setItemText(2, _translate("FormMainwindow", "트랙킹"))
        self.comboBoxLog.setItemText(0, _translate("FormMainwindow", "로그"))
        self.comboBoxLog.setItemText(1, _translate("FormMainwindow", "로그 설정"))
        self.comboBoxLog.setItemText(2, _translate("FormMainwindow", "로그 보기"))
        self.comboBoxHelp.setItemText(0, _translate("FormMainwindow", "도움말"))
        self.comboBoxHelp.setItemText(1, _translate("FormMainwindow", "도움말"))
        self.comboBoxHelp.setItemText(2, _translate("FormMainwindow", "단축키"))
        self.labelCam.setText(_translate("FormMainwindow", "Cam img"))
        self.labelState.setText(_translate("FormMainwindow", "robot state"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormMainwindow = QtWidgets.QWidget()
    ui = Ui_FormMainwindow()
    ui.setupUi(FormMainwindow)
    FormMainwindow.show()
    sys.exit(app.exec_())
