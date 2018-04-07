import unittest
import collections
from SlidingPuzzle import SlidingPuzzle

class test_SlidingPuzzle(unittest.TestCase):

	def setUp(self):
		self.matrizPuzzle = [[1,0,5],[6,4,7],[2,3,8]]
		self.miPuzzle = SlidingPuzzle(self.matrizPuzzle, 3)
	
	@unittest.skip("testing skipping")
	def test_mostrar_SlidingPuzzle(self):
		print("Inicio")
		self.miPuzzle.mostrarPuzzle(self.matrizPuzzle)

	@unittest.skip("testing skipping")
	def test_realizar_intercambio_hacia_abajo(self):
		resultado = self.miPuzzle.mover_hacia_abajo(0,1,self.matrizPuzzle)
		matrizEsperada = [[1,4,5],[6,0,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	@unittest.skip("testing skipping")
	def test_realizar_intercambio_hacia_izquierda(self):
		resultado = self.miPuzzle.mover_hacia_izquierda(0,1,self.matrizPuzzle)
		matrizEsperada = [[0,1,5],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	@unittest.skip("testing skipping")		
	def test_realizar_intercambio_hacia_derecha(self):
		resultado = self.miPuzzle.mover_hacia_derecha(0,1,self.matrizPuzzle)
		matrizEsperada = [[1,5,0],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	@unittest.skip("testing skipping")
	def test_realizar_intercambio_hacia_arriba(self):
		resultado = self.miPuzzle.mover_hacia_arriba(0,1,self.matrizPuzzle)
		matrizEsperada = [[1,0,5],[6,4,7],[2,3,8]]
		self.assertEqual(resultado, matrizEsperada)

	@unittest.skip("testing skipping")
	def test_consultar_si_se_resolvio_el_puzzle(self):
		matrizPuzzle = [[1,0,2],[3,4,5],[6,7,8]]
		self.miPuzzle = SlidingPuzzle(matrizPuzzle, 3)
		resultado = self.miPuzzle.mover_hacia_izquierda(0,1,matrizPuzzle)
		self.assertTrue(self.miPuzzle.termino(resultado))
		print("TERMINO")
		print self.miPuzzle.termino(resultado)

	def test_se_espera_obtener_que_los_movimientos_posibles_sean_4(self):
		print("No dijiste la palabra magica 1")
		matrizPuzzle = [[1,4,5],[6,0,7],[2,3,8]]
		cantidaMovimientos = self.miPuzzle.realizar_jugada(matrizPuzzle)
		self.assertEqual(cantidaMovimientos, 4)

	def test_probando_frontera_superior(self):
		print("No dijiste la palabra magica 2")
		matrizPuzzle = [[1,0,5],[6,4,7],[2,3,8]]
		cantidaMovimientos = self.miPuzzle.realizar_jugada(matrizPuzzle)
		self.assertEqual(cantidaMovimientos, 3)

	def test_probando_frontera_inferior(self):
		print("No dijiste la palabra magica 3")
		matrizPuzzle = [[1,3,5],[6,4,7],[2,0,8]]
		cantidaMovimientos = self.miPuzzle.realizar_jugada(matrizPuzzle)
		self.assertEqual(cantidaMovimientos, 3)

	def test_probando_frontera_izquierda_superior(self):
		print("No dijiste la palabra magica 4")
		matrizPuzzle = [[0,1,5],[6,4,7],[2,3,8]]
		cantidaMovimientos = self.miPuzzle.realizar_jugada(matrizPuzzle)
		self.assertEqual(cantidaMovimientos, 2)

	def test_probando_frontera_derecha(self):
		print("No dijiste la palabra magica 5")
		matrizPuzzle = [[1,7,5],[6,4,0],[2,3,8]]
		cantidaMovimientos = self.miPuzzle.realizar_jugada(matrizPuzzle)
		self.assertEqual(cantidaMovimientos, 3)

#	def test_recorrer_por_bfs(self):
#		print("BFS")
#		resultado = [[1,0,5],[6,4,7],[2,3,8]]
#		matrizEsperada = [[0,1,2],[3,4,5],[6,7,8]]
#		self.miPuzzle.bfs(resultado,matrizEsperada)
#		self.list(bfs(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
