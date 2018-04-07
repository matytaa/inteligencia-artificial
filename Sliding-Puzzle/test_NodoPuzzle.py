import unittest
import collections
from NodoPuzzle import NodoPuzzle
from SlidingPuzzle import SlidingPuzzle

class test_NodoPuzzle(unittest.TestCase):
	def setUp(self):
		matrizPuzzle = [[1,4,5],[6,0,7],[2,3,8]]
		self.miPuzzle = SlidingPuzzle(matrizPuzzle, 3)

	def test_crear_nodo_y_asignar_puzzle(self):
		temp = NodoPuzzle(self.miPuzzle.matrizPuzzle)
		print("Mostrar Matriz")
		print temp.obtenerDato()