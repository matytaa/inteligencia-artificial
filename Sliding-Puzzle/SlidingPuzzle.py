class SlidingPuzzle:
	matrizPuzzle = [[]]
	filaMostrar = [0,0,0]

	def __init__(self, matrizPuzzle):
		self.matrizPuzzle = matrizPuzzle

	def mostrarPuzzle(self):
		for i in range(3):
			for j in range(3):
				self.filaMostrar[j] = self.matrizPuzzle[i][j]
			print self.filaMostrar

	def down(self, fila, columna):
		auxiliar = self.matrizPuzzle[fila+1][columna]
		self.matrizPuzzle[fila+1][columna] = 0
		self.matrizPuzzle[fila][columna] = auxiliar

	def left(self, fila, columna):
		auxiliar = self.matrizPuzzle[fila][columna-1]
		self.matrizPuzzle[fila][columna-1] = 0
		self.matrizPuzzle[fila][columna] = auxiliar