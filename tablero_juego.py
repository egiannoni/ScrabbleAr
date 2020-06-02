import PySimpleGUI as sg 
import random

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

#Armando una columna
columna_1 = [[sg.Button(' ', size=(2,1), key='(i,j)', pad=(0,0)) for j in range(15)] for i in range(15)]

columna_2 = [   [sg.Text(' ' * 3),sg.Button('Bolsa')],
                [sg.Text(' ' * 22)],
                [sg.Text(' ' * 1),sg.Button('cronometro')]  ]
#Armo el diseño de la interface
dise=[  [sg.Text('Tablero Pc ')],
        [sg.Button('X', size=(4, 2), key=i) for i in letras_pc],
        [sg.Column(columna_1), sg.Column(columna_2)],
        [sg.Text('Tablero usuario ')],
        [sg.Button(w, size=(4, 2), key='w') for w in letras_usuario]] 


window = sg.Window('Juguemos').Layout(dise) 
event,values = window.read()









