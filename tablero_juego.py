import PySimpleGUI as sg 
import random
 
################ CONTENIDO #####################
bolsa =['A','B','C','D','E','F','G','H','I',
          'J','K','L','M','N','Ñ','O','P','Q',
          'R','S','T','U','V','W','X','Y','Z']

letras_usuario=[]
letras_pc=[]
for i in range(7):
     letra=random.choice(bolsa)
     letras_usuario.append(letra)
for i in range(7):
     letra=random.choice(bolsa)
     letras_pc.append(letra)

print(letras_usuario)
print(letras_pc)

############### INTERFAZ ############################

archivo = ['&Nuevo', '&Guardar', '&Cargar', '&Salir']
ayuda = ['&Ver reglas', '&Acerca de ScrabbleAR']
botones_del_menu = [['&Archivo', archivo], ['A&yuda', ayuda]]

def botones_especiales(button):
    (i, j) = button
    a=' '
    key=' '
    color = 'gray'
    if i == j or i + j == 14:
        color = 'red'
        a='x2'
        key='Valedoble'
    s = set((i, j))
    if s == {0, 3} or s == {0,11} or s == {3, 14} or s == {3, 14} or s == {11, 14}:
        color = 'green'
    if s == {2, 6} or s == {2, 8} or s == {3, 7} or s == {6, 12} or s == {7, 11} or s == {8, 12}:
        color = 'green'
    if i in {6, 8} and j in {6, 8}:
        color = 'blue'
    if s == {1, 5} or s == {1, 9} or s == {5, 13} or s == {9, 13}:
        color = 'blue'
    return color,a,key

######### Armando una columna
    
columna_1=[]
for i in range(15):
    fila = []
    for j in range(15):
        color,a = botones_especiales((i, j))
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









