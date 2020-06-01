import unittest
import random

def opuesto(x):
	return -x

class Test(unittest.TestCase):
	def test_opuesto(self):
		for attempt in range(20):
			x = random.randint(-9e4, 9e4)
			self.assertEqual(opuesto(x), -x)
						
if __name__ == "__main__":
	unittest.main()