import unittest
from GenerarId import GenerarId

class test_GenerarId(unittest.TestCase):
	def test_generarId_con_matriz_enviada(self):
		unaMatriz = [[1,4,5],[0,6,7],[2,3,8]]
		unId = '145067238'
		otroId = GenerarId().generar_id(unaMatriz)
		self.assertEqual(unId, otroId)