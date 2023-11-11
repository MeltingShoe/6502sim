class word:
	def __init__(self):
		self._data = [0,0,0,0,0,0,0,0]
	def _read(self):
		print('read',self._data)
		return self._data
	def _write(self,inData):
		if(type(inData) != list or len(inData) != 8):
			return -1
		for i in inData:
			if(i !=0 and i != 1):
				return -1
		print('write',self._data)
		self._data = inData
