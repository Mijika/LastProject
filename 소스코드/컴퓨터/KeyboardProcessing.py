from threading import Thread
import time

from pynput.keyboard import Listener, Key

from PyQt5.QtCore import *
from PyQt5.QtGui import *

#   "W" : 전진
#   "S" : 후진
#   "D" : 우회전
#   "A" : 좌회전

#   "F" : 부저 올리기
#   "T" : LED on   //한번더 "T" 면 off

#   "U" : 지름 증가
#   "I" : 지름 감소


class KeyboardProcessing(QObject):

    def __init__(self, tcp):
        super().__init__()
        self.store = list()
        self.flag = False
        self.tcp = tcp
        self.CommandSignalInIt()

    def CommandSignalInIt(self):
        # 시그널 정의
        self.sendMoveForward = pyqtSignal(int)
        self.sendMoveReverse = pyqtSignal(int)
        self.sendMoveLeftTurn = pyqtSignal(int)
        self.sendMoveRightTurn = pyqtSignal(int)

        self.sendLedToggle = pyqtSignal()
        self.sendBuzzer = pyqtSignal(int)

        self.sendDiameterUp = pyqtSignal(int)
        self.sendDiameterDown = pyqtSignal(int)
        # 슬롯 정의
        self.sendMoveForward.connect(self.tcp.ESP_MoveForward)
        self.sendMoveReverse.connect(self.tcp.ESP_MoveReverse)
        self.sendMoveLeftTurn.connect(self.tcp.ESP_MoveLeftTurn)
        self.sendMoveRightTurn.connect(self.tcp.ESP_MoveRightTurn)

        self.sendLedToggle.connect(self.tcp.ESP_LedToggle)
        self.sendBuzzer.connect(self.tcp.ESP_Buzzer)

        self.sendDiameterUp.connect(self.tcp.ESP_DiameterUp)
        self.sendDiameterDown.connect(self.tcp.ESP_DiameterDown)

    def startKeyboardProcessing(self):
        self.flag = True

        self.bThread = True
        self.thread = Thread(target=self.threadFunc)
        self.thread.start()

    def threadFunc(self):
        while self.bThread:
            with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
                listener.join()

        print('Keyboard thread finished')

    def handleKeyPress(self, key):
        if key in store:  # 중복 방지
            return

        store.append(key)

        sendingPressProcessing(key)

    def handleKeyRelease(self, key):
        sendingReleaseProcessing(key)

        if key in store:
            store.remove(key)
        # 종료
        if key == Key.esc:
            return False

    def sendingPressProcessing(self, key):
        if not(len(str(key).strip("'")) < 2):  # 쉬프트나 다른 여러 글자로 되어 있는 키 제거
            return

        if 'w' in str(key):
            print("PressESP_MoveForward")
            return
        if 'W' in str(key):
            print("PressESP_MoveForward")
            return
        if 'a' in str(key):
            print("PressESP_MoveLeftTurn")
            return
        if 'A' in str(key):
            print("PressESP_MoveLeftTurn")
            return
        if 's' in str(key):
            print("PressESP_MoveReverse")
            return
        if 'S' in str(key):
            print("PressESP_MoveReverse")
            return
        if 'd' in str(key):
            print("PressESP_MoveRightTurn")
            return
        if 'D' in str(key):
            print("PressESP_MoveRightTurn")
            return

        if 'f' in str(key):
            print("PressESP_LedToggle")
            return
        if 'F' in str(key):
            print("PressESP_LedToggle")
            return
        if 't' in str(key):
            print("PressESP_Buzzer")
            return
        if 'T' in str(key):
            print("PressESP_Buzzer")
            return

        if 'u' in str(key):
            print("PressESP_DiameterUp")
            return
        if 'U' in str(key):
            print("PressESP_DiameterUp")
            return
        if 'i' in str(key):
            print("PressESP_DiameterDown")
            return
        if 'I' in str(key):
            print("PressESP_DiameterDown")
            return

    def sendingReleaseProcessing(self, key):
        if not(len(str(key).strip("'")) < 2):  # 쉬프트나 다른 여러 글자로 되어 있는 키 제거
            return

        if 'w' in str(key):
            print("ReleaseESP_MoveForward")
            return
        if 'W' in str(key):
            print("ReleaseESP_MoveForward")
            return
        if 'a' in str(key):
            print("ReleaseESP_MoveLeftTurn")
            return
        if 'A' in str(key):
            print("ReleaseESP_MoveLeftTurn")
            return
        if 's' in str(key):
            print("ReleaseESP_MoveReverse")
            return
        if 'S' in str(key):
            print("ReleaseESP_MoveReverse")
            return
        if 'd' in str(key):
            print("ReleaseESP_MoveRightTurn")
            return
        if 'D' in str(key):
            print("ReleaseESP_MoveRightTurn")
            return

        if 't' in str(key):
            print("ReleaseESP_Buzzer")
            return
        if 'T' in str(key):
            print("ReleaseESP_Buzzer")
            return

        if 'u' in str(key):
            print("ReleaseESP_DiameterUp")
            return
        if 'U' in str(key):
            print("ReleaseESP_DiameterUp")
            return
        if 'i' in str(key):
            print("ReleaseESP_DiameterDown")
            return
        if 'I' in str(key):
            print("ReleaseESP_DiameterDown")
            return
