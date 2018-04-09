import sys
import numpy as np
import collections
from SlidingPuzzle import SlidingPuzzle
from NodoPuzzle import NodoPuzzle

def procesar_argumentos():
    """Reads the user input and defines the initial state of the puzzle"""
    puzzle_a_resolver = sys.argv[1]
    puzzle_a_resolver = puzzle_a_resolver.split(",")
    vector_de_argumentos = []
    for item in puzzle_a_resolver:
        vector_de_argumentos.append(int(item))

    largo_vector = len(vector_de_argumentos)
    if largo_vector%3==0:
    	filas_columnas=3
    elif largo_vector%4==0:
    	filas_columnas=4

    if verificarParametros(vector_de_argumentos,filas_columnas*filas_columnas):
    	x = np.reshape(vector_de_argumentos, (filas_columnas, filas_columnas))
    	matriz_inicial = x.tolist()
    	return matriz_inicial

    print ("Argumento invalido")
    return None

def verificarParametros(vector_inicial,cantidad_de_numeros):
	x = range(cantidad_de_numeros)
	for numero in x:
		if numero not in vector_inicial:
			return False
	return True


def main():
    matriz_inicial = procesar_argumentos()
    if matriz_inicial != None:
	    largo_matriz = len(matriz_inicial)
	    filas_columnas = 0

	    if largo_matriz%3 == 0:
	    	filas_columnas = 3
	    elif largo_matriz%4 == 0:
	    	filas_columnas = 4
	    else:
	    	print ("Matriz no soportada")
	    	return

	    miPuzzle = SlidingPuzzle(matriz_inicial, filas_columnas)
	    miPuzzle.jugar(matriz_inicial)
	    miPuzzle.mostrarSolucion()

# Main method call
if __name__ == "__main__":
    main()