import PySimpleGUI as sg
from MODULO_ATRIL import Atril

class Tablero:
    letras_pc=Atril.TableroPc()
    letras_usuario= Atril.TableroUsuario()
    def __init__(self):
        #Creates a 2-dimensional array that will serve as the board, as well as adds in the premium squares.
        self.board = [["   " for i in range(15)] for j in range(15)]
        self.BotonesConCaracteres()

    def GetBoard(self):
        ############### INTERFAZ ############################
        archivo = ['&Nuevo', '&Guardar', '&Cargar', '&Salir']
        ayuda = ['&Ver reglas', '&Acerca de ScrabbleAR']
        botones_del_menu = [['&Archivo', archivo], ['A&yuda', ayuda]]

        ######### Armando una columna
        columna_1=[]
        for i in range(15):
            fila = []
            for j in range(15):
                color = BotonesEspeciales((i, j))
                fila.append(sg.Button( self.board , size=(2,1), key=(i,j), pad=(0,0), button_color=(None, color)))
                columna_1.append(fila)


        columna_2 = [   [sg.Text(' ' * 3),sg.Button('Bolsa')],
                        [sg.Text(' ' * 22)],
                        [sg.Text(' ' * 1),sg.Button('cronometro')]  ]

        #Armo el diseño de la interface
        layout=[[sg.Menu(botones_del_menu)],
                [sg.Text('Tablero Pc ')],
                [sg.Button('X', size=(4, 2), key=i) for i in letras_pc],
                [sg.Column(columna_1), sg.Column(columna_2)],
                [sg.Text('Tablero usuario ')],
                [sg.Button(w, size=(4, 2), key='w') for w in letras_usuario]]

        window = sg.Window('Juguemos', layout)
        return window

    def BotonesConCaracteres(self):
        ValeTriple = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        ValeDoble  = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        ValeMitad = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        BotonComienzo=((7,7))

        for coordinate in ValeTriple:
            self.board[coordinate[0]][coordinate[1]] = "x3"
        for coordinate in ValeDoble:
            self.board[coordinate[0]][coordinate[1]] = "x2"
        for coordinate in ValeMitad:
            self.board[coordinate[0]][coordinate[1]] = "%2"
        for coordinate in BotonComienzo:
            self.board[coordinate[0]][coordinate[1]] = "C"

    def BotonesColores(button):
        #funcion que da colores y valore especiales a algunos botonos
        (i, j) = button
        color = 'gray'
        if i in {7} and j in {7}:
            color = 'yellow'
        s = set((i, j))
        if s == {0, 3} or s == {0,11} or s == {3, 14} or s == {3, 14} or s == {11, 14}:
            color = 'red'
        if s == {2, 6} or s == {2, 8} or s == {3, 7} or s == {6, 12} or s == {7, 10} or s == {8, 12}:
            color = 'red'
        if i in {5, 9} and j in {5, 9}:
            color = 'blue'
        if s == {1, 5} or s == {1, 9} or s == {5, 13} or s == {9, 13}:
            color = 'green'
        return color
