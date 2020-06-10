# ScrabbleAR: el tablero
# Una vez configurado, se mostrará un tablero en el cual cada jugador irá agregando las palabras.
# La figura 1 muestra el tablero del juego original.
# Figura 1: tablero del juego Scrabble.
# En el caso de ScrabbleAR se contará con tres (3) modelos de tableros fijos (esto no será
# configurable) de acuerdo a las siguientes indicaciones:
# ● El tablero podrá ser rectangular o cuadrado, como mínimo deberá incluir un cuadrado de
# 15x15. Se podrán agregar más columnas o filas.
# ● Deben incluir casillas con premio en donde se dupliquen, tripliquen los puntos por letra,
# se dupliquen o tripliquen el valor de la palabra. En el caso de conseguir una palabra que
# incluya la puntuación como letra y como palabra a la vez, se cuenta primero la puntuación
# de la letra y, después, la de la palabra. En todos los casos se deberán diseñar íconos que
# identifiquen estos casilleros.
# ● Deben incluir casillas con descuentos, en donde se restan 1, 2 o 3 puntos al puntaje
# alcanzado. Al igual que en el caso anterior, se deberán diseñar íconos que identifiquen
# estos casilleros.
# ------------------------------------------------------------------------------------------
import PySimpleGUI as sg
import random

def colorize_buttons(button):
    (i, j) = button
    color = 'gray'
    if i == j or i + j == 14:
        color = 'red'
    if i in {0, 7, 14} and j in {0, 7, 14}:
        color = 'yellow'
    s = set((i, j))
    if s == {0, 3} or s == {0,11} or s == {3, 14} or s == {3, 14} or s == {11, 14}:
        color = 'green'
    if s == {2, 6} or s == {2, 8} or s == {3, 7} or s == {6, 12} or s == {7, 11} or s == {8, 12}:
        color = 'green'
    if i in {6, 8} and j in {6, 8}:
        color = 'blue'
    if s == {1, 5} or s == {1, 9} or s == {5, 13} or s == {9, 13}:
        color = 'blue'
    return color

sg.theme('Dark Teal 12')

# Botones del menú
archivo = ['&Nuevo', '&Guardar', '&Cargar', '&Salir']
ayuda = ['&Ver reglas', '&Acerca de ScrabbleAR']
botones_del_menu = [['&Archivo', archivo], ['A&yuda', ayuda]]

FILAS = COLUMNAS = 15
board = [
    [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for j in range(COLUMNAS)] for i in range(FILAS)
    ]

layout =  [
    [sg.Menu(botones_del_menu)]
    ]
# por qué no funcionó el siguiente código y sólo se obtenía la matriz siempre con valor de i == 14??
# for i in range(FILAS):
#     layout.append(sg.Button('ahrre {},{}'.format(i, j), size=(4, 2), key=(i,j), pad=(0,0)) for j in range(COLUMNAS))
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        color = colorize_buttons((i, j))
        fila.append(sg.Button('ahrre {},{}'.format(i, j), size=(4, 2), key=(i,j), pad=(0,0), button_color=(None, color)))
    layout.append(fila)

window = sg.Window('ScrabbleAR', layout)

go = True
while go:
    event, values = window.read()
    if event in (None, 'Salir'):
        go = False
    # window[(row, col)].update('New text')   # To change a button's text, use this pattern
    # For this example, change the text of the button to the board's value and turn color black
    if go:
        window[event].update(board[event[0]][event[1]], button_color=('white','black'))
window.close()