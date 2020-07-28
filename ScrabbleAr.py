import PySimpleGUI as sg
import ConoceMas
import Ranking
import Registro
import Game


layout = [  [sg.Text('Scrabble Ar', size=(15, 1), justification='center', font=("Times", "24", "bold italic"),text_color='black')],
            [sg.T(' ' * 7),sg.InputText('Nick',size=(30, 1),text_color='gray',key='nick')],
            [sg.T(' ' * 7),sg.InputText('Pass',size=(30, 1),text_color='gray',key='pass',password_char='*')],
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
        Game.main()
        #nickingresado= value['nick']
        #paswingresada= value['pasword']
        #base=AbroBase('base_datos.pkl')
        #try:
        #    if nickingresado in base:
        #        pasword= Jugador.get_pass()
        #        try:
        #            if paswingresada == pasword:
        #                window1.close()
        #                juego.main()
        #        except:
        #            sg.SystemTray.notify('Error', 'La contraseña ingresada no coincide ')
        #
        #except:
        #    sg.SystemTray.notify('Error', 'el nick ingresado NO existe.')
