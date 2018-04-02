import unittest
from SlidingPuzzle import SlidingPuzzle

class test_SlidingPuzzle(unittest.TestCase):

	def setUp(self):
		matrizPuzzle = [[1,0,5],[6,4,7],[2,3,8]]
		self.miPuzzle = SlidingPuzzle(matrizPuzzle, 3)
	
	def test_mostrar_SlidingPuzzle(self):
		print("Inicio")
		self.miPuzzle.mostrarPuzzle()

	def test_realizar_intercambio_hacia_abajo(self):
		self.miPuzzle.down(0,1)

	def test_realizar_intercambio_hacia_izquierda(self):
		self.miPuzzle.left(0,1)
		
	def test_realizar_intercambio_hacia_derecha(self):
		self.miPuzzle.right(0,1)

	def test_realizar_intercambio_hacia_arriba(self):
		self.miPuzzle.up(0,1)