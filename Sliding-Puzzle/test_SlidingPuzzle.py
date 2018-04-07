import unittest
import collections
from SlidingPuzzle import SlidingPuzzle

class test_SlidingPuzzle(unittest.TestCase):

	def setUp(self):
		matrizPuzzle = [[1,0,5],[6,4,7],[2,3,8]]
		self.miPuzzle = SlidingPuzzle(matrizPuzzle, 3)
	
	def test_mostrar_SlidingPuzzle(self):
		print("Inicio")
		self.miPuzzle.mostrarPuzzle()

	def test_realizar_intercambio_hacia_abajo(self):
		resultado = self.miPuzzle.mover_hacia_abajo(0,1)
		matrizEsperada = [[1,4,5],[6,0,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	def test_realizar_intercambio_hacia_izquierda(self):
		resultado = self.miPuzzle.mover_hacia_izquierda(0,1)
		matrizEsperada = [[0,1,5],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)
		
	def test_realizar_intercambio_hacia_derecha(self):
		resultado = self.miPuzzle.mover_hacia_derecha(0,1)
		matrizEsperada = [[1,5,0],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	def test_realizar_intercambio_hacia_arriba(self):
		resultado = self.miPuzzle.mover_hacia_arriba(0,1)
		matrizEsperada = [[1,0,5],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	def test_consultar_si_se_resolvio_el_puzzle(self):
		matrizPuzzle = [[1,0,2],[3,4,5],[6,7,8]]
		self.miPuzzle = SlidingPuzzle(matrizPuzzle, 3)
		resultado = self.miPuzzle.mover_hacia_izquierda(0,1)
		self.assertTrue(self.miPuzzle.termino(resultado))
		print("TERMINO")
		print self.miPuzzle.termino(resultado)

#	def test_recorrer_por_bfs(self):
#		print("BFS")
#		resultado = [[1,0,5],[6,4,7],[2,3,8]]
#		matrizEsperada = [[0,1,2],[3,4,5],[6,7,8]]
#		self.miPuzzle.bfs(resultado,matrizEsperada)
#		self.list(bfs(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
