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
		resultado = self.miPuzzle.down(0,1)
		matrizEsperada = [[1,4,5],[6,0,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	def test_realizar_intercambio_hacia_izquierda(self):
		resultado = self.miPuzzle.left(0,1)
		matrizEsperada = [[0,1,5],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)
		
	def test_realizar_intercambio_hacia_derecha(self):
		resultado = self.miPuzzle.right(0,1)
		matrizEsperada = [[1,5,0],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	def test_realizar_intercambio_hacia_arriba(self):
		resultado = self.miPuzzle.up(0,1)
		matrizEsperada = [[1,0,5],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)