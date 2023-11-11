
from modules.word import word

class bReg(word):
	def __init__(self, bus):
		super().__init__()
		self.inBus = bus
	def output(self):
		self.inBus.writeToBus(self._read())
	def load(self):
		self._write(self.inBus.readFromBus())

