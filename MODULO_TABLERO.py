import PySimpleGUI as sg
from MODULO_ATRIL import Atril

class Board:
    """this function creates the scrabble board """
    def __init__(self):
        self.get_board()
        self.add_premium_squares()
        letras_pc=Atril.TableroPc()
        letras_usuario= Atril.TableroUsuario()

    def add_premium_squares(self):
          """ This function adds special scores and special prints to defined boxes """
        TripleScore = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
        DoubleScore  = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
        MiddleScore = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
        StartButton = ((7,7))

        for coordinate in TripleScore:
            self.board[coordinate[0]][coordinate[1]] = "x3"
        for coordinate in DoubleScore:
            self.board[coordinate[0]][coordinate[1]] = "x2"
        for coordinate in MiddleScore:
            self.board[coordinate[0]][coordinate[1]] = "%2"
        for coordinate in StartButton:
            self.board[coordinate[0]][coordinate[1]] = "C"

    def colorize_buttons(button):
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

    def get_board(self):
        ############### user interface creation ############################
        archive = ['&Nuevo', '&Guardar', '&Cargar', '&Salir']
        help = ['&Ver reglas', '&Acerca de ScrabbleAR']
        menu_buttons = [['&Archivo', archive], ['A&yuda', help]]

        ######### column creation
        column_1=[]
        for i in range(15):
            row = []
            for j in range(15):
                r,a,value = colorize_buttons((i, j))
                row.append(sg.Button( a , size=(2,1), key=(i,j), pad=(0,0), button_color=(None, r)))
            column_1.append(row)


        column_2 = [   [sg.Text(' ' * 3),sg.Button('Reponer')],
                        [sg.Text(' ' * 22)],
                        [sg.Text('Tiempo de Juego', key='-CLOCK_TEXT-')],
                        [sg.Text(key='-CLOCK-', size=(8, 2), font=('Helvetica', 11), justification='center')],
                        [sg.Text(' ' * 22)],
                        [sg.Text(' ' * 22)],
                        [sg.Button ('Pasar turno', key='pasarturno')]
                    ]
        #Armo el diseño de la interface
        layout=[[sg.Menu(menu_buttons)],
                [sg.Text('Tablero Pc '), sg.Text('Puntaje', key='puntajepc')],
                [sg.Button(key=i + 7, button_text='?', size=(2,1), pad=((1,1), (16, 1)), enable_events=True, disabled=True) for i in letras_pc],
                [sg.Column(column_1), sg.Column(column_2)],
                [sg.Text('Tablero Jugador '), sg.Text('Puntaje', key= 'puntajejugador')],
                [sg.Button(key=i, button_text=letras_usuario, size=(2,1), pad=((1,1), (16, 1)), enable_events=True) for i in letras_usuario]
                ]

        window = sg.Window('Juguemos', layout)
        return window

    def place_word(self, word, location, direction, player):
        #Allows you to play words, assuming that they have already been confirmed as valid.
        global premium_spots
        premium_spots = []
        direction = direction.lower()
        word = word.upper()

        #Places the word going rightwards
        if direction.lower() == "right":
            for i in range(len(word)):
                if self.board[location[0]][location[1]+i] != "   ":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                self.board[location[0]][location[1]+i] = " " + word[i] + " "

        #Places the word going downwards
        elif direction.lower() == "down":
            for i in range(len(word)):
                if self.board[location[0]][location[1]+i] != "   ":
                    premium_spots.append((word[i], self.board[location[0]][location[1]+i]))
                self.board[location[0]+i][location[1]] = " " + word[i] + " "

        #Removes tiles from player's rack and replaces them with tiles from the bag.
        for letter in word:
            for tile in player.get_rack_arr():
                if tile.get_letter() == letter:
                    player.rack.remove_from_rack(tile)
        player.rack.replenish_rack()

    def board_array(self):
        #Returns the 2-dimensional board array.
        return self.board
