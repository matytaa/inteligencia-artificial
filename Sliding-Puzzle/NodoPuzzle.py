import collections

class NodoPuzzle:
	miMatriz = None
	nodoPadre = None
	visitado = None

	def __init__(self, unaMatriz, unNodoPadre, estadoVisita):
		self.miMatriz = unaMatriz
		self.nodoPadre = unNodoPadre
		self.visitado = estadoVisita

	def obtenerDato(self):
		return self.miMatriz

	def obtenerNodoPadre(self):
		return self.nodoPadre

	def fueVisitado(self):
		return self.visitado

	def asignarMiMatriz(self,nuevomiMatriz):
		self.miMatriz = nuevomiMatriz
