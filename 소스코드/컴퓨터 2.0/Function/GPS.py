import io
import sys

import folium
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GPS(QObject):
	"""docstring for GPS"""

	sendGPS = pyqtSignal(str)

	def __init__(self, widget, GPS=[37.4806831,127.0840176], zoom=17):
		super().__init__()
		self.GPS = GPS
		self.zoom = zoom
		self.widget = widget
		self.sendGPS.connect(self.widget.recvGPS)

		self.GPSSet()

	def GPSSet(self):
		m = folium.Map(
			location = self.GPS, zoom_start=self.zoom)

		data = io.BytesIO()
		m.save(data, close_file=False)

		html = data.getvalue().decode()

		self.sendGPS.emit(html)
