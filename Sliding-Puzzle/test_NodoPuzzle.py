import unittest
import collections
import numpy as np

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

	def test_verificar_existencia_de_matriz_en_lista_nodos(self):
		matrizPadre = [[1,4,5],[6,0,7],[2,3,8]]
		matrizIzquierda = [[1,4,5],[0,6,7],[2,3,8]]
		matrizDerecha = [[1,4,5],[6,7,0],[2,3,8]]
		matrizArriba = [[1,0,5],[6,4,7],[2,3,8]]
		matrizAbajo = [[1,4,5],[6,3,7],[2,0,8]]

		matrizBuscada = [[1,4,5],[6,3,7],[2,0,8]]
		x = np.matrix(matrizBuscada)
		y = x.tolist()
		print("HOLA")
		print y

		temp = NodoPuzzle(matrizPadre, None, False)
		temp1 = NodoPuzzle(matrizIzquierda, matrizPadre, False)
		temp2 = NodoPuzzle(matrizDerecha, matrizPadre, False)
		temp3 = NodoPuzzle(matrizArriba, matrizPadre, False)
		temp4 = NodoPuzzle(matrizAbajo, matrizPadre, False)


		print("Mostrar Matriz")
		print temp.obtenerDato()