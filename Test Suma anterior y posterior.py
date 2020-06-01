import unittest
import random

def suma(x):
	return x + (x + 1) + (x - 1)

class Test(unittest.TestCase):
	def test_suma(self):
		for attempt in range(20):
			x = random.randint(1, 9e4)
			self.assertEqual(suma(x), x * 3)

if __name__ == "__main__":
	unittest.main()