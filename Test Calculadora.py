import unittest
import random

def calculadora(a, b, operacion):
    if operacion == 1:
        return a + b
    elif operacion == 2:
        return a - b
    else:
        return a * b

class Test(unittest.TestCase):
	def test_calculadora(self):
		for attempt in range(20):
			a, b, operacion = random.randint(1, 10), random.randint(1, 10), random.randint(1, 3)
			if operacion == 1:
				self.assertEqual(calculadora(a, b, operacion), a + b)
			elif operacion == 2:
				self.assertEqual(calculadora(a, b, operacion), a - b)
			else:
				self.assertEqual(calculadora(a, b, operacion), a * b)
										
if __name__ == "__main__":
	unittest.main()