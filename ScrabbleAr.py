import PySimpleGUI as sg
import ConoceMas
import Ranking
import Registro
import Game
from Jugadores import ListaJugadores
 
sg.theme('Material2')
column1 = [  [sg.Text('Scrabble Ar', size=(15, 1), justification='center', font=("Comic", "30", "bold italic"),text_color='black')],
            [sg.Text(' Usuario: ',font=("Comic", "15"),text_color='black'),sg.InputText(size=(30, 1),text_color='gray',key='nick')],
            [sg.T('Contraseña:',font=("Comic", "15"),text_color='black'),sg.InputText(size=(30, 1),text_color='gray',key='password',password_char='*')],
            [sg.T(' ' * 20),sg.Button(' Iniciar Sesion  ')],
            [sg.T(' ' * 22),sg.Button('Registrarse')],
            [sg.T(' ' * 30)],
            [sg.Button('Conoce mas del juego'),sg.T(' ' * 5), sg.Button('Nuestro Ranking')] ]


layout = [[sg.Image(r'ScrabbleArBackGround.png',size=(400,400)),sg.VerticalSeparator( ),sg.Column(column1)] ]

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
        lista_jugadores2= ListaJugadores.cargar_fichero()
        usuario_valido = False
        for jugador in lista_jugadores2.get_jugadores():
            if jugador.get_nick() == usuario and jugador.get_password() == password:
                usuario_valido = True
                break
        if usuario_valido:
            print ('validacion con exito')
            window1.close()
            Game.main()
        else:
            sg.SystemTray.notify('Error', 'Los datos ingresados no son correctos ')
