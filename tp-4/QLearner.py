import Tablero
import Movimiento
import threading
import time

descuento = 0.3
movimientos = Movimiento.movimientos
estados = []
matriz = {}
for i in range(Movimiento.filas):
    for j in range(Movimiento.columnas):
        estados.append((i, j))

for estado in estados:
    matriz_auxiliar = {}
    for movimiento_a_realizar in movimientos:
        matriz_auxiliar[movimiento_a_realizar] = 0.1
        Movimiento.set_puntaje_celda(estado, movimiento_a_realizar, matriz_auxiliar[movimiento_a_realizar])
    matriz[estado] = matriz_auxiliar

for (i, j, c, w) in Movimiento.celdas_especiales:
    for movimiento_a_realizar in movimientos:
        matriz[(i, j)][movimiento_a_realizar] = w
        Movimiento.set_puntaje_celda((i, j), movimiento_a_realizar, w)


def mover(movimiento_a_realizar):
    un_jugador = Tablero.jugador
    un_puntaje = -Movimiento.puntaje
    if movimiento_a_realizar == movimientos[0]:
        Movimiento.intentar_mover(0, -1)
    elif movimiento_a_realizar == movimientos[1]:
        Movimiento.intentar_mover(0, 1)
    elif movimiento_a_realizar == movimientos[2]:
        Movimiento.intentar_mover(-1, 0)
    elif movimiento_a_realizar == movimientos[3]:
        Movimiento.intentar_mover(1, 0)
    else:
        return
    otro_jugador = Tablero.jugador
    un_puntaje += Movimiento.puntaje
    return un_jugador, movimiento_a_realizar, un_puntaje, otro_jugador


def matriz_maxima(un_jugador):
    valor = None
    actual = None
    for una_posicion, un_valor in matriz[un_jugador].items():
        if valor is None or (un_valor > valor):
            valor = un_valor
            actual = una_posicion
    return actual, valor


def incrementar_matriz(un_jugador, una_posicion, diferencial, incremento):
    matriz[un_jugador][una_posicion] *= 1 - diferencial
    matriz[un_jugador][una_posicion] += diferencial * incremento
    Movimiento.set_puntaje_celda(un_jugador, una_posicion, matriz[un_jugador][una_posicion])


def ejecutar():
    global descuento
    time.sleep(1)
    diferencial = 1
    juego = 1
    while True:
        un_jugador = Tablero.jugador
        maximo_actual, maximo_valor = matriz_maxima(un_jugador)
        (un_jugador, una_posicion, un_puntaje, otro_jugador) = mover(maximo_actual)

        # Actualizamos la matriz
        maximo_actual, maximo_valor = matriz_maxima(otro_jugador)
        incrementar_matriz(un_jugador, una_posicion, diferencial, un_puntaje + descuento * maximo_valor)

        juego += 1.0
        if Tablero.puedo_reiniciar():
            Tablero.reiniciar_juego()
            time.sleep(0.01)
            juego = 1.0
            
        diferencial = pow(juego, -0.1)
        time.sleep(0.1)


juego = threading.Thread(target=ejecutar)
juego.daemon = True
juego.start()
Tablero.comenzar()
