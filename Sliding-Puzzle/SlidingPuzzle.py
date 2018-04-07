import collections

class SlidingPuzzle:
	matrizPuzzle = [[]]
	filaMostrar = [0,0,0]
	filaColumnas = 0
	matrizResultado = [[0,1,2],[3,4,5],[6,7,8]]

	def __init__(self, matrizPuzzle, dimension):
		self.matrizPuzzle = matrizPuzzle
		self.filaColumnas = dimension

	def mostrarPuzzle(self, unaMatriz):
		self.filaMostrar = [0,0,0]
		for i in range(self.filaColumnas):
			for j in range(self.filaColumnas):
				self.filaMostrar[j] = unaMatriz[i][j]
			print self.filaMostrar

	def intercambiar(self, fila_original, columna_original, fila_nueva, columna_nueva, unaMatriz):
		if fila_nueva >= 0 and columna_nueva >=0 and self.filaColumnas > fila_nueva and self.filaColumnas > columna_nueva:
			auxiliar = unaMatriz[fila_nueva][columna_nueva]
			unaMatriz[fila_nueva][columna_nueva] = 0
			unaMatriz[fila_original][columna_original] = auxiliar
		else:
			print("movimiento no valido")
		return unaMatriz

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
		otra_matriz = self.mover_hacia_izquierda(1,1,unaMatriz)
		return otra_matriz
	
