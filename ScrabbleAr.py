import PySimpleGUI as sg
import ConoceMas
import Ranking
import Registro
import Game
from Jugadores import ListaJugadores
 
sg.theme('LightBrown3')
# sg.theme_button(('#fdae61'))
# sg.theme_button(('black','#fdae61'))
column1=[  [sg.Text('Usuario:',font=("Verdana", "9"),text_color='black')],
           [sg.InputText(size=(20, 1),text_color='black',key='nick'),sg.T(' ' * 10)],
           [sg.T('Contraseña:',font=("Verdana", "9"),text_color='black')],
           [sg.InputText(size=(20, 1),text_color='black',key='password',password_char='*')],
           [sg.T(' ' * 30)],
           [sg.Button('Iniciar Sesion', button_color=('black','#fdae61'))] ]

column2=[  [sg.Button('Registrarse',button_color=('black','#fdae61'))],
           [sg.T(' ' * 20)],
           [sg.Button('Conoce mas del juego',button_color=('black','#fdae61'))],
           [sg.T(' ' * 20)],
           [sg.Button('Nuestro Ranking',button_color=('black','#fdae61'))] ]


layout = [ [sg.Text('Scrabble Ar', size=(15, 1), justification='center', font=("Verdana", "30", "bold"),text_color='#d7191c')], 
           [sg.Image(r'ScrabbleArBackGround.png',size=(400,350))], 
           [sg.Column(column1), sg.VSeperator(),sg.Column(column2)] ]
           
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
    if event == 'Iniciar Sesion':
        window1.close()
        Game.main()
        # usuario= value['nick']
        # password= value['password']
        # lista_jugadores= ListaJugadores()
        # lista_jugadores2= lista_jugadores.cargar_fichero()
        # usuario_valido = False
        # for jugador in lista_jugadores2.get_jugadores():
        #     if jugador.get_nick() == usuario and jugador.get_password() == password:
        #         usuario_valido = True
        # if usuario_valido:
        #     print ('validacion con exito')
        #     window1.close()
        #     Game.main()
        # else:
        #     sg.SystemTray.notify('Error', 'Los datos ingresados no son correctos ')
