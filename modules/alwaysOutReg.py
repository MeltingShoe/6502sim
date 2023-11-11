from modules.word import word

class oneOneAlwaysReg(word):
	def __init__(self, bus, outBus):
		super().__init__()
		self.inBus = bus
		self.outBus = bus
		print('inbus')
		
	def output(self):
		self.outBus.writeToBus(self._read())
	def load(self):
		print(self.inBus.readFromBus())
		self._write(self.inBus.readFromBus())
		self.outBus.writeToBus(self._read())