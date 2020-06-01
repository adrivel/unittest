import unittest

def ocultarVocales(text):
	string = text
	vowels = ('a', 'e', 'i', 'o', 'u')
	for x in text.lower():
		if x in vowels:
			string = string.replace(x, "")
	return string
	
class Test(unittest.TestCase):
	def test_ocultarvocales(self):
		text = input()

		self.assertEqual(ocultarVocales(text), 'hl q tl') # El test solo funcionará si se introduce "hola que tal"

if __name__ == "__main__":
	unittest.main()