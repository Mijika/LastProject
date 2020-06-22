import cv2 as cv
import numpy as np
import socket
from _thread import *
from threading import *


def recaImg(scok, count):
	imgBuf = b''
	while count:
		newbuf = scok.recv(count)
		if not newbuf:
			return None

		imgBuf += newbuf
		count -= len(newbuf)

	return imgBuf


class Communication():
	def __init__(self):
		self.robotIP = []
		self.sem = Semaphore(200)
		self.threads = list()

		self.HOST = '127.0.0.1'
		self.PORT = 10242

	def findRobotIP(self):
		for ip in range(1, 255):
			ip = "192.168.219." + str(ip)
			self.threads.append(Thread(target=self.connScan,
	                                       args=(ip, self.robotIP, self.sem)))

		for thread in self.threads:
			thread.start()

		print("로봇 IP 찾는중....")

		for thread in self.threads:
			thread.join()

		if len(self.robotIP) == 0:
			print("없음")
		else:
			for i in self.robotIP:
				print(i)


	def socketConnection():
		pass

	class connScan():
	    def __init__(self, tgtHost, robotIP, sem):
	        self.tgtHost = '127.0.0.1'
	        self.tgtPort = 9999
	        self.robotIP = robotIP
	        self.sem = sem

	        self.run()

	    def run(self):
	        self.sem.acquire()
	        try:
	            client = socket(AF_INET, SOCK_STREAM)
	            client.setdefaulttimeout(0.5)
	            client.connect((self.tgtHost, self.tgtPort))
	            self.robotIP.append(self.tgtHost)
	            client.close()
	        except Exception as e:
	            pass
	        self.sem.release()


address = "127.0.01"
port = 9191

a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

location = (address, port)
result_of_check = a_socket.connect_ex(location)

if result_of_check == 0:
    print("Port is open")
else:
    print("Port is not open")

a_socket.close()