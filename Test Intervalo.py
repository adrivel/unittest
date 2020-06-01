import unittest
import random

def intervalo(a, x, b):
	return a <= x <= b

class Test(unittest.TestCase):
	def test_intervalo(self):
		for attempt in range(20):
			a, x, b = random.randint(0, 100), random.randint(-100, 400), random.randint(200, 300)
			self.assertEqual(intervalo(a, x, b), a <= x <= b)
			
if __name__ == "__main__":
	unittest.main()