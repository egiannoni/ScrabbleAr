import PySimpleGUI as sg 
import random 

############### MODULOS ############################
#bolsa{ letra: [cantidad,valor]}  por ahora tenemos listas pero creemos que mejor seria un diccionario

bolsa=['A'*11,'B'*3,'C'*4,'D'*4,'E'*11,'F'*2,'G'*2,'H'*2,'I'*6,
       'J'*2,'K'*1,'L'*6,'M'*4,'N'*5,'Ñ'*1,'O'*8,'P'*3,'Q'*1,
       'R'*6,'S'*7,'T'*4,'U'*6,'V'*2,'W'*1,'X'*1,'Y'*1,'Z'*1]

def quien_empieza():
    if random.randint(0, 1) == 0:
        return 'pc'
    else:
        return 'usuario'

def tableros(x):    
    letras_usuario=[]
    letras_pc=[]
    for i in range(7):
         letra=random.choice(x)
         letras_usuario.append(letra)
    return letras_usuario
    for i in range(7):
         letra=random.choice(x)
         letras_pc.append(letra)
    return letras_pc


def botones_especiales(button): #funcion que da colores y valore especiales a algunos botonos
    (i, j) = button
    a=' '
    valor='simple'
    color = 'gray'
    if i in {7} and j in {7}:
        color = 'yellow'
        a='C'
    s = set((i, j))
    if s == {0, 3} or s == {0,11} or s == {3, 14} or s == {3, 14} or s == {11, 14}:
        color = 'red'
        a='x2'
        valor='vale_doble'
    if s == {2, 6} or s == {2, 8} or s == {3, 7} or s == {6, 12} or s == {7, 10} or s == {8, 12}:
        color = 'red'
        a='x2'
        valor='vale_doble'
    if i in {5, 9} and j in {5, 9}:
        color = 'blue'
        a='x3'
        valor='vale_triple'
    if s == {1, 5} or s == {1, 9} or s == {5, 13} or s == {9, 13}:
        color = 'green'
        a='/2'
        valor='vale_mitad'
    return color, a, valor

############### INTERFAZ ############################
archivo = ['&Nuevo', '&Guardar', '&Cargar', '&Salir']
ayuda = ['&Ver reglas', '&Acerca de ScrabbleAR']
botones_del_menu = [['&Archivo', archivo], ['A&yuda', ayuda]]

######### Armando una columna
columna_1=[]
for i in range(15):
    fila = []
    for j in range(15):
        color,a,valor = botones_especiales((i, j))
        fila.append(sg.Button( a , size=(2,1), key=(i,j), pad=(0,0), button_color=(None, color)))
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

event,values = window.read()


##### PROGRAMA PRINCIPAL
letras_usuario,letras_pc=tableros(bolsa)
empieza= quien_empieza()
cantidad_fichas=len(bolsa)
puntaje_jugador=0
puntaje_pc=0
while cantidad_fichas !=0 or puntaje_jugador =< 300 or puntaje_pc =< 300 :   #Los 300son provisorios 
    if empieza == pc:
        ....
    else: 
        ....







