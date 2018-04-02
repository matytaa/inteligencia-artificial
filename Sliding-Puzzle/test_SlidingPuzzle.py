import unittest
from SlidingPuzzle import SlidingPuzzle

class test_SlidingPuzzle(unittest.TestCase):

	def setUp(self):
		matrizPuzzle = [[1,0,5],[6,4,7],[2,3,8]]
		self.miPuzzle = SlidingPuzzle(matrizPuzzle)
	
	def test_mostrar_SlidingPuzzle(self):
		print("Inicio")
		self.miPuzzle.mostrarPuzzle()

	def test_realizar_intercambio_hacia_abajo(self):
		self.miPuzzle.down(0,1)
		print("intercambio abajo")
		self.miPuzzle.mostrarPuzzle()

	def test_realizar_intercambio_hacia_izquierda(self):
		self.miPuzzle.left(0,1)
		print("intercambio izquierda")
		self.miPuzzle.mostrarPuzzle()
