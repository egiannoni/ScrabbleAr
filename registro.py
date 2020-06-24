import PySimpleGUI as sg
from MODULO_BASEDEDATOS import abro_base, agrego_a_base
from MODULO_JUGADORES import Jugador

############# ARMADO DE LA COLUMNA DE LA INTERFAZ #############
columna_1 =  [  [sg.Text('Nombre')],
                [sg.Text('Apellido')],
                [sg.Text('Nacionalidad')],
		            [sg.Text('Correo')] ]

columna_2 = [   [sg.InputText(key='nombre',size=(30, 1))],
                [sg.InputText(key='apellido',size=(30, 1))],
                [sg.InputText(key='nacionalidad',size=(30, 1))],
		    [sg.InputText(key='correo',size=(30, 1))]  ]

columna_3 =  [  [sg.Text('Nick Name')],
                [sg.Text('Pass')] ]

columna_4 = [   [sg.InputText(key='nick',size=(30, 1))],
                [sg.InputText(key='pas',size=(30, 1))]  ]

#Armo el diseño de la interface
dise = [      [sg.Text('Datos Personales')],
                [sg.Column(columna_1), sg.Column(columna_2)],
                [sg.Text('Datos de Juego ')],
                [sg.Column(columna_3), sg.Column(columna_4)],
                [ sg.Ok(), sg.Cancel()] ]


############# PRINCIPAL #############
def main():
    window = sg.Window('Registro de ScrabbleAR').Layout(dise)
    event, values = window.read()
    while True:
        base=abro_base('base_datos.pkl')
        if event == 'Ok' :
            if values['correo'] not in base:
                if values['nick'] not in base:
                    jug= Jugador(values['pas'],values['nick'] ,values['nombre'],values['apellido'],values['nacionalidad'],values['correo'])
                    agrego_a_base('base_datos.pkl',jug)
                    window.close()
                else:
                    sg.SystemTray.notify('Error', 'el nick ingresado ya existe')

            else:
               sg.SystemTray.notify('Error', 'el correo ingresado ya existe')
        if event == None:
            break
        if event == 'Cancel':
            break
    window.close()


if __name__ == '__main__':
    main()
