import unittest
from GenerarId import GenerarId
import numpy as np

class test_GenerarId(unittest.TestCase):
	@unittest.skip("testing skipping")
	def test_generarId_con_matriz_enviada(self):
		unaMatriz = [[1,4,5],[0,6,7],[2,3,8]]
		unId = '145067238'
		otroId = GenerarId().generar_id(unaMatriz)
		self.assertEqual(unId, otroId)

	@unittest.skip("testing skipping")
	def test_generarId_con_otra_matriz_enviada(self):
		unaMatriz = [[1,4,5],[7,6,0],[2,3,8]]
		unId = '145760238'
		otroId = GenerarId().generar_id(unaMatriz)
		listaID = [GenerarId().generar_id(unaMatriz)]
		self.assertEqual(unId, otroId)
		self.assertTrue(unId in listaID)
