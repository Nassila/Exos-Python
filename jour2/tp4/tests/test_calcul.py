import sys
sys.path.append('..')
from src.calcul import Calcul
import unittest


class TestCalcul(unittest.TestCase):
	def test_add(self):
		c = Calcul()
		assert c.add(1, 4) == 5
		assert c.add(10, 4) == 14
		assert c.add(1, 4) == c.add(5,0)
		assert c.add(1, 4) == c.add(4,1)

	def test_sous(self):
		c = Calcul()
		assert c.sous(10,2) == 8
		assert c.sous(14,20) == -6
		assert c.sous(14,2) == -c.sous(2,14)

	def test_div(self):
		c = Calcul()
		assert c.div(4, 2) == 2

	def test_sous(self):
		c = Calcul()
		assert c.sous(4, 1) == 3


if __name__ == '__main__':
	unittest.main()