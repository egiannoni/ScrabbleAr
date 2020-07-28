import PySimpleGUI as sg
from Jugadores import Jugador, ListaJugadores

############# ARMADO DE LA INTERFAZ #############
column_1 =  [  [sg.Text('Nombre')],
               [sg.Text('Apellido')],
               [sg.Text('Nacionalidad')],
		       [sg.Text('Correo')]
            ]

column_2 = [   [sg.InputText(key='nombre',size=(30, 1))],
               [sg.InputText(key='apellido',size=(30, 1))],
               [sg.InputText(key='nacionalidad',size=(30, 1))],
		       [sg.InputText(key='correo',size=(30, 1))]
            ]

column_3 =  [  [sg.Text('Nick Name')],
                [sg.Text('Pasword')]
            ]

column_4 = [   [sg.InputText(key='nick',size=(30, 1))],
                [sg.InputText(key='pas',size=(30, 1))]
            ]

#Armo el diseño de la interface
layout = [      [sg.Text('Datos Personales')],
                [sg.Column(column_1), sg.Column(column_2)],
                [sg.Text('Datos de Juego ')],
                [sg.Column(column_3), sg.Column(column_4)],
                [ sg.Ok(), sg.Cancel()]
        ]

def main():
    """ Principal loop """

    window2 = sg.Window('Registro de ScrabbleAR', layout)
    event, values = window2.read()
    lista_jugadores=ListaJugadores()
    while True:
        if event == 'Ok' :
                jug= Jugador(values['pas'],values['nick'] ,values['nombre'],values['apellido'],values['nacionalidad'],values['correo'])
                lista_jugadores.agregar_jugador(jug)
        if event == None:
            break
        if event == 'Cancel':
            break
    window2.close()


if __name__ == '__main__':
    main()
