import collections

class NodoPuzzle:
	dato = None

	def __init__(self,datoInicial):
		self.dato = datoInicial

	def obtenerDato(self):
		return self.dato

	def asignarDato(self,nuevodato):
		self.dato = nuevodato
