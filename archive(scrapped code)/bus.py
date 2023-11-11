from modules.word import word

class bus:
	def __init__(self):
		self.word = word()
	def writeToBus(self,data):
		print('writeToBus')
		self.word._write(data)
	def readFromBus(self):
		print('readFromBus')
		return self.word._read()