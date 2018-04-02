class SlidingPuzzle:
	matrizPuzzle = [[]]
	filaMostrar = [0,0,0]
	filaColumnas = 0

	def __init__(self, matrizPuzzle, dimension):
		self.matrizPuzzle = matrizPuzzle
		self.filaColumnas = dimension

	def mostrarPuzzle(self):
		for i in range(3):
			for j in range(3):
				self.filaMostrar[j] = self.matrizPuzzle[i][j]
			print self.filaMostrar

	def intercambiar(self, fila_original, columna_original, fila_nueva, columna_nueva):
		if fila_nueva >= 0 and columna_nueva >=0 and self.filaColumnas > fila_nueva and self.filaColumnas > columna_nueva:
			auxiliar = self.matrizPuzzle[fila_nueva][columna_nueva]
			self.matrizPuzzle[fila_nueva][columna_nueva] = 0
			self.matrizPuzzle[fila_original][columna_original] = auxiliar
		else:
			print("movimiento no valido")

	def down(self, fila, columna):
		self.intercambiar(fila,columna, fila+1, columna)
		print("\n intercambio abajo")
		self.mostrarPuzzle()

	def up(self, fila, columna):
		self.intercambiar(fila,columna, fila-1, columna)
		print("\n intercambio arriba")
		self.mostrarPuzzle()

	def left(self, fila, columna):
		self.intercambiar(fila,columna, fila, columna-1)
		print("\n intercambio izquierda")
		self.mostrarPuzzle()

	def right(self, fila, columna):
		self.intercambiar(fila,columna, fila, columna+1)
		print("\n intercambio derecha")
		self.mostrarPuzzle()