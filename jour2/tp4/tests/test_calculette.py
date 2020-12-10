# fichier de test unitaire
import sys
sys.path.append('..')
from src.calculette import Calculette
import unittest
"""
DEFINITION DES METHODES DE TEST DANS LA CLASSE DE TEST
"""
class TestCalculatrice(unittest.TestCase):
	def test_add(self):
		c = Calculette()
		assert c.add(1, 4) == 5
		assert c.add(10, 4) == 14
		assert c.add(1, 4) == c.add(5,0)
		assert c.add(1, 4) == c.add(4,1)

	def test_sous(self):
		c = Calculette()
		assert c.sous(10,2) == 8
		assert c.sous(14,20) == -6
		assert c.sous(14,2) == -c.sous(2,14)

	def test_mult(self):
		c = Calculette()
		assert c.mult(10,2) == 20

	def test_div(self):
		c = Calculette()
		assert c.div(10,2) == 5


"""
LANCEMENT DES TEST
"""
# if __name__ == '__main__':
# 	unittest.main()