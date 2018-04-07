class GenerarId:

	def generar_id(self, unaMatriz):
		cadena = ''
		for i in xrange(0, len(unaMatriz)):
			for j in xrange(0, len(unaMatriz[i])):
				cadena += str(unaMatriz[i][j])
		return cadena
