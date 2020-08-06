import PySimpleGUI as sg
from Jugadores import Jugador, ListaJugadores
import Database

sg.theme('LightBrown3')
############# ARMADO DE LA INTERFAZ #############
column_1 =  [  [sg.Text('Nombre',font=("Verdana", "9"),text_color='black')],
               [sg.Text('Apellido',font=("Verdana", "9"),text_color='black')],
               [sg.Text('Nacionalidad',font=("Verdana", "9"),text_color='black')],
		       [sg.Text('Correo',font=("Verdana", "9"),text_color='black')]
            ]

column_2 = [   [sg.InputText(key='nombre',size=(30, 1))],
               [sg.InputText(key='apellido',size=(30, 1))],
               [sg.InputText(key='nacionalidad',size=(30, 1))],
		       [sg.InputText(key='correo',size=(30, 1))]
            ]

column_3 =  [  [sg.Text('Nick Name',font=("Verdana", "9"),text_color='black')],
                [sg.Text('Pasword',font=("Verdana", "9"),text_color='black')]
            ]

column_4 = [   [sg.InputText(key='nick',size=(30, 1))],
                [sg.InputText(key='pas',size=(30, 1))]
            ]

#Armo el diseño de la interface
layout = [      [sg.Text('Datos Personales',font=("Verdana", "11", "bold"),text_color='#d7191c')],
                [sg.Column(column_1), sg.Column(column_2)],
                [sg.Text('Datos de Juego',font=("Verdana", "11", "bold"),text_color='#d7191c')],
                [sg.Column(column_3), sg.Column(column_4)],
                [ sg.Ok(button_color=('black','#fdae61')), sg.Cancel(button_color=('black','#fdae61'))]
        ]

def main():
    """ Principal loop """
    window2 = sg.Window('Registro de ScrabbleAR', layout)
    event, values = window2.read()
    lista_jugadores=ListaJugadores()
    while True:
        if event == 'Ok':
            jug= Jugador(values['pas'],values['nick'] ,values['nombre'],values['apellido'],values['nacionalidad'],values['correo'])

            a = Database.abro_base()
            if a != None:
                lista_jugadores = Database.abro_base()
            else:
                lista_jugadores = ListaJugadores()

            lista_jugadores.agregar_jugador(jug)
            Database.guardo_base(lista_jugadores)
            break
        if event == None:
            break
        if event == 'Cancel':
            break
    window2.close()
if __name__ == '__main__':
    main()
