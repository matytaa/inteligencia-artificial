import collections
import copy
from NodoPuzzle import NodoPuzzle
from GenerarId import GenerarId

class SlidingPuzzle:
	matrizPuzzle = [[]]
	filaMostrar = [0,0,0]
	filaColumnas = 0
	matrizResultado_3x3 = [[0,1,2],[3,4,5],[6,7,8]]
	matrizResultado_4x4 = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
	exploraciones = 0
	filaConCero = None
	columnaConCero = None
	listaID = []
	misNodos = []
	movimiento = []
	cantidadDeNodos = 0

	def __init__(self, matrizPuzzle, dimension):
		self.matrizPuzzle = matrizPuzzle
		self.filaColumnas = dimension

	def mostrarPuzzle(self, unaMatriz):
		if self.filaColumnas == 3:
			self.filaMostrar = [0,0,0]
		elif self.filaColumnas == 4:
			self.filaMostrar = [0,0,0,0]

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
		#else:
			#print("movimiento no valido")
		return unaMatrizAModificar

	def mover_hacia_abajo(self, fila, columna, unaMatriz):
		self.intercambiar(fila,columna, fila+1, columna, unaMatriz)
		#print("\n intercambio abajo")
		#self.mostrarPuzzle(unaMatriz)
		return unaMatriz

	def mover_hacia_arriba(self, fila, columna, unaMatriz):
		self.intercambiar(fila,columna, fila-1, columna, unaMatriz)
		#print("\n intercambio arriba")
		#self.mostrarPuzzle(unaMatriz)
		return unaMatriz

	def mover_hacia_izquierda(self, fila, columna, unaMatriz):
		self.intercambiar(fila,columna, fila, columna-1, unaMatriz)
		#print("\n intercambio izquierda")
		#self.mostrarPuzzle(unaMatriz)
		return unaMatriz

	def mover_hacia_derecha(self, fila, columna, unaMatriz):
		self.intercambiar(fila,columna, fila, columna+1, unaMatriz)
		#print("\n intercambio derecha")
		#self.mostrarPuzzle(unaMatriz)
		return unaMatriz

	def termino(self, unaMatriz):
		if self.filaColumnas == 3:
			return self.matrizResultado_3x3 == unaMatriz
		elif self.filaColumnas == 4:
			return self.matrizResultado_4x4 == unaMatriz

	def incluirEnLista(self, unaMatriz):
		unId = GenerarId().generar_id(unaMatriz)
		#self.listaID = [GenerarId().generar_id(unaMatriz)]
		if unId in self.listaID:
			return False
		self.listaID.append(unId)
		return True

	def incrementarExploraciones(self):
		self.exploraciones += 1
	
	def cantidadExploraciones(self):
		return self.exploraciones

	def realizar_jugada(self, unaMatriz, unNodo):
		self.buscarCero(unaMatriz)
		matriz_jugadas = copy.deepcopy(unaMatriz)
		self.incluirEnLista(matriz_jugadas)
		matriz_jugadas = self.mover_hacia_izquierda(self.filaConCero,self.columnaConCero,matriz_jugadas)
		if matriz_jugadas != unaMatriz :
			self.incrementarExploraciones()
			if self.incluirEnLista(matriz_jugadas):
				self.misNodos.append(NodoPuzzle(matriz_jugadas, unNodo, False))

		matriz_jugadas = copy.deepcopy(unaMatriz)
		matriz_jugadas = self.mover_hacia_derecha(self.filaConCero,self.columnaConCero,matriz_jugadas)
		if matriz_jugadas != unaMatriz:
			self.incrementarExploraciones()
			if self.incluirEnLista(matriz_jugadas):
				self.misNodos.append(NodoPuzzle(matriz_jugadas, unNodo, False))
		
		matriz_jugadas = copy.deepcopy(unaMatriz)
		matriz_jugadas = self.mover_hacia_arriba(self.filaConCero,self.columnaConCero,matriz_jugadas)
		if matriz_jugadas != unaMatriz:
			self.incrementarExploraciones()
			if self.incluirEnLista(matriz_jugadas):
				self.misNodos.append(NodoPuzzle(matriz_jugadas, unNodo, False))
		
		matriz_jugadas = copy.deepcopy(unaMatriz)
		matriz_jugadas = self.mover_hacia_abajo(self.filaConCero,self.columnaConCero,matriz_jugadas)
		if matriz_jugadas != unaMatriz:
			self.incrementarExploraciones()
			if self.incluirEnLista(matriz_jugadas):
				self.misNodos.append(NodoPuzzle(matriz_jugadas, unNodo, False))
	
	def jugar(self, unaMatriz):
		miNodo = NodoPuzzle(unaMatriz, None, False)
		self.misNodos.append(miNodo)
		while True:
			if len(self.misNodos) == 0: 
				return None
			unNodo = self.misNodos.pop(0)
			#if unNodo.obtenerDato() == self.matrizResultado_3x3:
			if self.termino(unNodo.obtenerDato()):
				self.cantidadDeNodos = len(self.misNodos)
				self.movimiento.insert(0,unNodo)
				return True
			unNodo.visitado = True
			self.realizar_jugada(unNodo.obtenerDato(), unNodo)


	def mostrarSolucion(self):
		nodoSolucion = self.movimiento.pop(0)
		matriz_solucion=[]
		movimiento=[]
		matriz_solucion.append(nodoSolucion.obtenerDato())
		unNodoPadre = nodoSolucion.obtenerNodoPadre()
		while unNodoPadre != None:
			matriz_solucion.insert(0,unNodoPadre.obtenerDato())
			unNodoPadre = unNodoPadre.obtenerNodoPadre()
		
		for i in range(0, len(matriz_solucion)):
			print("Movimiento " + str(i))
			self.mostrarPuzzle(matriz_solucion.pop(0))
			print("\n")
		print("Cantidad de posiciones evaluadas: " + str(self.exploraciones))
		print("Cantidad de nodos: " + str(self.cantidadDeNodos))

