import collections
import copy

class SlidingPuzzle:
	matrizPuzzle = [[]]
	filaMostrar = [0,0,0]
	filaColumnas = 0
	matrizResultado = [[0,1,2],[3,4,5],[6,7,8]]
	exploraciones = 0
	filaConCero = None
	columnaConCero = None

	def __init__(self, matrizPuzzle, dimension):
		self.matrizPuzzle = matrizPuzzle
		self.filaColumnas = dimension

	def mostrarPuzzle(self, unaMatriz):
		self.filaMostrar = [0,0,0]
		for i in range(self.filaColumnas):
			for j in range(self.filaColumnas):
				self.filaMostrar[j] = unaMatriz[i][j]
			print self.filaMostrar

	def buscarCero(self, unaMatriz):
		for fila in range(self.filaColumnas):
			for columna in range(self.filaColumnas):
				if unaMatriz[fila][columna] == 0 :
					self.filaConCero = fila
					self.columnaConCero = columna

	def intercambiar(self, fila_original, columna_original, fila_nueva, columna_nueva, unaMatrizAModificar):
		if fila_nueva >= 0 and columna_nueva >=0 and self.filaColumnas > fila_nueva and self.filaColumnas > columna_nueva:
			auxiliar = unaMatrizAModificar[fila_nueva][columna_nueva]
			unaMatrizAModificar[fila_nueva][columna_nueva] = unaMatrizAModificar[fila_original][columna_original]
			unaMatrizAModificar[fila_original][columna_original] = auxiliar
		else:
			print("movimiento no valido")
		return unaMatrizAModificar

	def mover_hacia_abajo(self, fila, columna, unaMatriz):
		self.intercambiar(fila,columna, fila+1, columna, unaMatriz)
		print("\n intercambio abajo")
		self.mostrarPuzzle(unaMatriz)
		return unaMatriz

	def mover_hacia_arriba(self, fila, columna, unaMatriz):
		self.intercambiar(fila,columna, fila-1, columna, unaMatriz)
		print("\n intercambio arriba")
		self.mostrarPuzzle(unaMatriz)
		return unaMatriz

	def mover_hacia_izquierda(self, fila, columna, unaMatriz):
		self.intercambiar(fila,columna, fila, columna-1, unaMatriz)
		print("\n intercambio izquierda")
		self.mostrarPuzzle(unaMatriz)
		return unaMatriz

	def mover_hacia_derecha(self, fila, columna, unaMatriz):
		self.intercambiar(fila,columna, fila, columna+1, unaMatriz)
		print("\n intercambio derecha")
		self.mostrarPuzzle(unaMatriz)
		return unaMatriz

	def termino(self, unaMatriz):
		return self.matrizResultado == unaMatriz

	def realizar_jugada(self, unaMatriz):

		self.buscarCero(unaMatriz)
		otra_matriz = copy.deepcopy(unaMatriz)
		otra_matriz = self.mover_hacia_izquierda(self.filaConCero,self.columnaConCero,otra_matriz)
		if otra_matriz != unaMatriz :
			self.exploraciones += 1

		otra_matriz = copy.deepcopy(unaMatriz)
		otra_matriz = self.mover_hacia_derecha(self.filaConCero,self.columnaConCero,otra_matriz)
		if otra_matriz != unaMatriz:
			self.exploraciones += 1
		
		otra_matriz = copy.deepcopy(unaMatriz)
		otra_matriz = self.mover_hacia_arriba(self.filaConCero,self.columnaConCero,otra_matriz)
		if otra_matriz != unaMatriz:
			self.exploraciones += 1
		
		otra_matriz = copy.deepcopy(unaMatriz)
		otra_matriz = self.mover_hacia_abajo(self.filaConCero,self.columnaConCero,otra_matriz)
		if otra_matriz != unaMatriz:
			self.exploraciones += 1

		return self.exploraciones
	
