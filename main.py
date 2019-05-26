#################################
##							   ##	
##	Online Parallel Learning   ##
##	Taubaté´s University	   ##
##							   ##
##	- Fernando N. S. Costa	   ##
##	- Gabriel F. Carvalho	   ##
##							   ##	
#################################

#################################
##	Imports

import sys				#System
import asyncio
import time
import numpy as np

						#UI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QMessageBox, QLineEdit, QWidget, QLabel, QGridLayout, QRadioButton, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QFont, QPen, QIntValidator

#	End Imports
##################################
#	Main Class

class App(QMainWindow):

	def __init__(self):
		super().__init__()

		##########################
		#	Usable Vars
		self._TITLE = "Online Parallel Model Learning" 
		self._LEFT = 10
		self._TOP = 10
		self._BG_WIDTH = 680;
		self._BG_HEIGHT = 480;

		##########################
		#	Windows Flags
		self.setWindowFlags(
			QtCore.Qt.Window |
			QtCore.Qt.CustomizeWindowHint |
			QtCore.Qt.WindowTitleHint |
			QtCore.Qt.WindowCloseButtonHint |
			QtCore.Qt.WindowStaysOnTopHint
		)

		##########################
		#	Pixmap
		self.pixmap = QPixmap('src/bg.png')

		##########################
		#	Initializing UI
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self._TITLE)
		self.setGeometry(self._LEFT, self._TOP, self._BG_WIDTH, self._BG_HEIGHT)
		#self.drawUI()
		self.show()

	###############################
	#	Events
	def paintEvent(self, e):
		painter = QtGui.QPainter(self)
		painter.drawPixmap(self.rect(), self.pixmap)
		painter.setRenderHint(QPainter.Antialiasing, True)

		pen = QtGui.QPen()
		pen.setWidth(3)
		pen.setColor(QtCore.Qt.red)
		pen.setCapStyle(QtCore.Qt.RoundCap)
		pen.setJoinStyle(QtCore.Qt.RoundJoin)
		painter.setPen(pen)

	#################################
	#	Python Slots

	#################################
	#	Python Methods

#	Main Class Ending
#####################################
#	Initializing Main Class

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	ex.resize(ex.pixmap.width(), ex.pixmap.height())
	ex.move(500, 450)
	ex.setFixedSize(ex.size())
	ex.update()
	sys.exit(app.exec_())