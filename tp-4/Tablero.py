import Movimiento

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
master = Tk()


tablero = Canvas(master, width=Movimiento.filas*Movimiento.ancho, height=Movimiento.columnas*Movimiento.ancho)
jugador = (0, Movimiento.columnas-1)

Movimiento.ajustar_grilla()


def reiniciar_juego():
    global jugador, puntaje, mi_posicion, reiniciar
    jugador = (0, Movimiento.columnas-1)
    Movimiento.puntaje = 1
    Movimiento.reiniciar = False
    tablero.coords(mi_posicion,
                   jugador[0]*Movimiento.ancho+Movimiento.ancho*2/10,
                   jugador[1]*Movimiento.ancho+Movimiento.ancho*2/10,
                   jugador[0]*Movimiento.ancho+Movimiento.ancho*8/10,
                   jugador[1]*Movimiento.ancho+Movimiento.ancho*8/10)

def puedo_reiniciar():
    return Movimiento.reiniciar

master.bind("<Up>", Movimiento.mover_arriba)
master.bind("<Down>", Movimiento.mover_abajo)
master.bind("<Right>", Movimiento.mover_derecha)
master.bind("<Left>", Movimiento.mover_izquierda)

mi_posicion = tablero.create_rectangle(jugador[0]*Movimiento.ancho+Movimiento.ancho*2/10,
                                       jugador[1]*Movimiento.ancho+Movimiento.ancho*2/10,
                                       jugador[0]*Movimiento.ancho+Movimiento.ancho*8/10,
                                       jugador[1]*Movimiento.ancho+Movimiento.ancho*8/10,
                                       fill="orange", width=1, tag="mi_posicion")

tablero.grid(row=0, column=0)


def comenzar():
    master.mainloop()
