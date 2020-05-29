import unittest
import random

def suma(x):
	return x + (x + 1) + (x - 1)

def intervalo(a, x, b):
	return a <= x <= b

def opuesto(x):
	return -x

def calculadora(a, b, operacion):
    if operacion == 1:
        return a + b
    elif operacion == 2:
        return a - b
    else:
        return a * b

class Test(unittest.TestCase):
	def test_suma(self):
		for attempt in range(20):
			x = random.randint(1, 9e4)
			self.assertEqual(suma(x), x * 3)

	def test_intervalo(self):
		for attempt in range(20):
			a, x, b = random.randint(0, 100), random.randint(-100, 400), random.randint(200, 300)
			self.assertEqual(intervalo(a, x, b), a <= x <= b)

	def test_opuesto(self):
		for attempt in range(20):
			x = random.randint(-9e4, 9e4)
			self.assertEqual(opuesto(x), -x)

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