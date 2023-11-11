from modules.word import word

class bus:
	def __init__(self):
		self.word = word()
	def writeToBus(self,data):
		self.word._write(data)
	def readFromBus(self):
		return self.word._read()