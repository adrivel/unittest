import unittest

def contar(num):
	numeros = []
	for x in range(num):
		numeros.append(str(x + 1))
	return(", ".join(numeros))

class Test(unittest.TestCase):
	def test_suma(self):
		num = int(input())
		self.assertEqual(contar(num), '1, 2, 3, 4, 5') # El test solo funcionará si se introduce el número 5

if __name__ == "__main__":
	unittest.main()