import unittest
from modules import word
from modules import bus
from modules import basicRegister as bReg
from modules.alwaysOutReg import oneOneAlwaysReg

class TestWord(unittest.TestCase):

	def setUp(self):
		self.testWord = word.word()

	def testInitType(self):
		self.assertTrue(type(self.testWord._data) is list)

	def testInitZeros(self):
		x = 0
		for i in self.testWord._data:
			x += i
		self.assertTrue(x == 0)
	def testReadType(self):
		self.assertTrue(type(self.testWord._read()) is list)

	def testReadZeros(self):
		x = 0
		for i in self.testWord._read():
			x += i
		self.assertTrue(x == 0)

	def testSet(self):
		a = [1,1,0,1,1,0,1,1]
		self.testWord._write(a)
		self.assertTrue(self.testWord._data == a)

	def testEnforceType(self):
		a = 'bussin'
		b = self.testWord._write(a)
		self.assertTrue(b == -1)

	def testEnforceLen(self):
		a = [1,0,1,1,0,1]
		b = self.testWord._write(a)
		self.assertTrue(b == -1)

	def testReadWrite(self):
		a = [1,0,1,0,0,1,0,1]
		self.testWord._write(a)
		b = self.testWord._read()
		self.assertTrue(a == b)

	def testEnforceBinary(self):
		a = [0,1,2,0,1,0,0,1]
		b = self.testWord._write(a)
		self.assertTrue(b == -1)


class TestBus(unittest.TestCase):

	def setUp(self):
		self.testBus = bus.bus()

	def testReadWrite(self):
		a = [1,0,1,0,0,1,0,1]
		self.testBus.writeToBus(a)
		b = self.testBus.readFromBus()
		self.assertTrue(a == b)

class TestBReg(unittest.TestCase):

	def setUp(self):
		self.testBus = bus.bus()
		self.testbReg = bReg.bReg(self.testBus)
		self.testbReg2 = bReg.bReg(self.testBus)

	def testTransfer(self):
		a = [1,0,1,0,0,1,0,1]
		self.testbReg._write(a)
		self.testbReg.output()
		self.testbReg2.load()
		b = self.testbReg2._read()
		self.assertTrue(a == b)

class TestOneOne(unittest.TestCase):

	def setUp(self):
		self.testBus = bus.bus()
		self.testBus2 = bus.bus()
		self.oneOneReg = oneOneAlwaysReg(self.testBus,self.testBus2)
		self.testbReg = bReg.bReg(self.testBus)
		self.testbReg2 = bReg.bReg(self.testBus2)

	def testTransfer(self):
		a = [1,0,1,0,0,1,0,1]
		d = self.testbReg._write(a)
		print('d',d)
		self.testbReg.output()
		self.oneOneReg.load()
		b = self.testbReg2._read()
		print('b',b)
		self.assertEqual(a, b)
if __name__ == '__main__':
    unittest.main()
