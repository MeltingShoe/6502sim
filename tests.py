import unittest
from modules import word


class TestThing(unittest.TestCase):

	def setUp(self):
		self.thing = thingClass()

	def testThingBehavior(self):
		self.assertTrue(self.thing.doSomethingAndReturnTrue)

if __name__ == '__main__':
    unittest.main()

def run():
	unittest.main()