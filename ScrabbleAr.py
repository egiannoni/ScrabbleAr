import PySimpleGUI as sg
import ConoceMas
import Ranking
import Registro
import Game
from Jugadores import ListaJugadores

layout = [  [sg.Text('Scrabble Ar', size=(15, 1), justification='center', font=("Times", "24", "bold italic"),text_color='black')],
            [sg.Text(' Usuario: '),sg.InputText(size=(30, 1),text_color='gray',key='nick')],
            [sg.T('Contraseña:'),sg.InputText(size=(30, 1),text_color='gray',key='password',password_char='*')],
            [sg.T(' ' * 20),sg.Button(' Iniciar Sesion  ')],
            [sg.T(' ' * 22),sg.Button('Registrarse')],
            [sg.T(' ' * 30)],
            [sg.Button('Conoce mas del juego'),sg.T(' ' * 5), sg.Button('Nuestro Ranking')] ]

window1 = sg.Window('ScrabbleAr ',layout)


while True:
    event,value=window1.read()
    if event == None:
        break
    if event == 'Conoce mas del juego':
        ConoceMas.main()
    if event == 'Nuestro Ranking':
        Ranking.main()
    if event == 'Registrarse':
        Registro.main()
    if event == ' Iniciar Sesion  ':
        usuario= value['nick']
        password= value['password']
        lista_jugadores=ListaJugadores()
        try:
            usuario_valido = False
            for jugador in lista_jugadores.get_jugadores():
                if jugador.get_nick() == usuario and jugador.get_password() == password:
                    usuario_valido = True
                    print ('validacion con exito')
                    window1.close()
                    Game.main()
                else:
                    sg.SystemTray.notify('Error', 'La contraseña ingresada no coincide ')
        except:
            sg.SystemTray.notify('Error', 'el nick ingresado NO existe.')
