import unittest
import random

def maximo(vector):
    nummax = None
    for numero in vector:
        if nummax is None or numero > nummax:
            nummax = numero
    return nummax

class Test(unittest.TestCase):
  def test_vector(self):
    for attempt in range(20):
      vector = tuple(random.randint(-9e4, 9e4) for number in range(20))
      self.assertEqual(maximo(vector), max(vector))

if __name__ == "__main__":
  unittest.main()