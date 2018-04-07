import unittest
import collections
from NodoPuzzle import NodoPuzzle
from SlidingPuzzle import SlidingPuzzle

class test_NodoPuzzle(unittest.TestCase):
	def setUp(self):
		matrizPuzzle = [[1,4,5],[6,0,7],[2,3,8]]
		self.miPuzzle = SlidingPuzzle(matrizPuzzle, 3)

	def test_crear_nodo_y_asignar_puzzle(self):
		matrizPadre = [[1,4,5],[0,6,7],[2,3,8]]
		temp = NodoPuzzle(self.miPuzzle.matrizPuzzle, matrizPadre, False)
		print("Mostrar Matriz")
		print temp.obtenerDato()