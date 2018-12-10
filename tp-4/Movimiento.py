import Tablero

movimientos = ["up", "down", "left", "right"]
indicador_en_pantalla = 0.1

puntaje_minimo_celda = -0.2
puntaje_maximo_celda = 0.2
ancho = 100
(filas, columnas) = (4, 4)

puntaje = 1
reiniciar = False
recompensa = -0.04

paredes = [(1, 2)]
celdas_especiales = [(3, 1, "red", -1), (3, 0, "green", 1)]
puntajes_de_celdas = {}

def realizar_movimiento(i, j, movimiento_a_realizar):
    if movimiento_a_realizar == movimientos[0]:
        return Tablero.tablero.create_polygon((i+0.5-indicador_en_pantalla)*ancho, (j+indicador_en_pantalla)*ancho,
                                    (i+0.5+indicador_en_pantalla)*ancho, (j+indicador_en_pantalla)*ancho,
                                    (i+0.5)*ancho, j*ancho,
                                    fill="white", width=1)
    elif movimiento_a_realizar == movimientos[1]:
        return Tablero.tablero.create_polygon((i+0.5-indicador_en_pantalla)*ancho, (j+1-indicador_en_pantalla)*ancho,
                                    (i+0.5+indicador_en_pantalla)*ancho, (j+1-indicador_en_pantalla)*ancho,
                                    (i+0.5)*ancho, (j+1)*ancho,
                                    fill="white", width=1)
    elif movimiento_a_realizar == movimientos[2]:
        return Tablero.tablero.create_polygon((i+indicador_en_pantalla)*ancho, (j+0.5-indicador_en_pantalla)*ancho,
                                    (i+indicador_en_pantalla)*ancho, (j+0.5+indicador_en_pantalla)*ancho,
                                    i*ancho, (j+0.5)*ancho,
                                    fill="white", width=1)
    elif movimiento_a_realizar == movimientos[3]:
        return Tablero.tablero.create_polygon((i+1-indicador_en_pantalla)*ancho, (j+0.5-indicador_en_pantalla)*ancho,
                                    (i+1-indicador_en_pantalla)*ancho, (j+0.5+indicador_en_pantalla)*ancho,
                                    (i+1)*ancho, (j+0.5)*ancho,
                                    fill="white", width=1)


def render_grid():
    global celdas_especiales, paredes, ancho, filas, columnas, jugador
    for i in range(filas):
        for j in range(columnas):
            Tablero.tablero.create_rectangle(i*ancho, j*ancho, (i+1)*ancho, (j+1)*ancho, fill="white", width=1)
            temp = {}
            for movimiento_a_realizar in movimientos:
                temp[movimiento_a_realizar] = realizar_movimiento(i, j, movimiento_a_realizar)
            puntajes_de_celdas[(i,j)] = temp
    for (i, j, c, w) in celdas_especiales:
        Tablero.tablero.create_rectangle(i*ancho, j*ancho, (i+1)*ancho, (j+1)*ancho, fill=c, width=1)
    for (i, j) in paredes:
        Tablero.tablero.create_rectangle(i*ancho, j*ancho, (i+1)*ancho, (j+1)*ancho, fill="black", width=1)

def set_puntaje_celda(state, movimiento_a_realizar, val):
    global puntaje_minimo_celda, puntaje_maximo_celda
    triangle = puntajes_de_celdas[state][movimiento_a_realizar]
    green_dec = int(min(255, max(0, (val - puntaje_minimo_celda) * 255.0 / (puntaje_maximo_celda - puntaje_minimo_celda))))
    green = hex(green_dec)[2:]
    red = hex(255-green_dec)[2:]
    if len(red) == 1:
        red += "0"
    if len(green) == 1:
        green += "0"
    color = "#" + red + green + "00"
    Tablero.tablero.itemconfigure(triangle, fill=color)


def intentar_mover(una_fila, una_columna):
    global jugador, filas, columnas, puntaje, recompensa, mi_posicion, reiniciar
    if reiniciar == True:
        Tablero.reiniciar_juego()
    nueva_fila = Tablero.jugador[0] + una_fila
    nueva_columna = Tablero.jugador[1] + una_columna
    puntaje += recompensa
    if (nueva_fila >= 0) \
            and (nueva_fila < filas) \
            and (nueva_columna >= 0) \
            and (nueva_columna < columnas) \
            and not ((nueva_fila, nueva_columna) in paredes):
        Tablero.tablero.coords(Tablero.mi_posicion,
                               nueva_fila*ancho+ancho*2/10,
                               nueva_columna*ancho+ancho*2/10,
                               nueva_fila*ancho+ancho*8/10,
                               nueva_columna*ancho+ancho*8/10)
        Tablero.jugador = (nueva_fila, nueva_columna)
    for (i, j, c, w) in celdas_especiales:
        if nueva_fila == i and nueva_columna == j:
            puntaje -= recompensa
            puntaje += w
            if puntaje > 0:
                print ("[Exito] puntaje obtenido: ", puntaje)
            else:
                print ("[Fallo] puntaje obtenido: ", puntaje)
            reiniciar = True
            return


def mover_arriba(event):
    intentar_mover(0, -1)


def mover_abajo(event):
    intentar_mover(0, 1)


def mover_izquierda(event):
    intentar_mover(-1, 0)


def mover_derecha(event):
    intentar_mover(1, 0)
