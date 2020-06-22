import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 255)
        self.unlockButton = QtWidgets.QPushButton(Dialog)
        self.unlockButton.setGeometry(QtCore.QRect(10, 180, 171, 51))
        self.unlockButton.setObjectName("unlockButton")
        self.lockButton = QtWidgets.QPushButton(Dialog)
        self.lockButton.setGeometry(QtCore.QRect(220, 180, 151, 51))
        self.lockButton.setObjectName("lockButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.unlockButton.setText(_translate("Dialog", "OK"))
        self.lockButton.setText(_translate("Dialog", "Lock"))
        self.label.setText(_translate("Dialog", ""))
        self.lineEdit.setText(_translate("Dialog", ""))

class Dialog2(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog2, self).__init__(parent)
        self.setupUi(self)
        self.is_key_ctrl_pressed = False
        self.unlockButton.clicked.connect(self.unlock)

    @QtCore.pyqtSlot()
    def unlock(self):
        if self.is_key_ctrl_pressed:
            print("unlock")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.is_key_ctrl_pressed = True
        super(Dialog2, self).keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Control:
            self.is_key_ctrl_pressed = False

        super(Dialog2, self).keyReleaseEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog2()
    w.show()
    sys.exit(app.exec_())