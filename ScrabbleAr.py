import PySimpleGUI as sg
import ConoceMas
import Ranking
import Registro
import SelectorNiveles
from Jugadores import ListaJugadores
import Database
import Config

sg.theme('LightBrown3')
column1=[  [sg.Text('Usuario:',font=("Verdana", "9"),text_color='black', key='-T1-')],
           [sg.InputText(size=(20, 1),text_color='black',key='nick'),sg.T(' ' * 10)],
           [sg.T('Contraseña:',font=("Verdana", "9"),text_color='black', key='-T2-')],
           [sg.InputText(size=(20, 1),text_color='black',key='password',password_char='*')],
           [sg.T(' ' * 30, key='-T3-')],
           [sg.Button('Iniciar Sesion', button_color=('black','#fdae61'), key='-LOGIN-')] ]

column2=[  [sg.Button('Registrarse',button_color=('black','#fdae61'), key='-SIGN_UP-')],
           [sg.T(' ' * 20, key='-T4-')],
           [sg.Button('Configuraciones Avanzadas',button_color=('black','#fdae61'), key='-ADVANCED_CONFIG-')],
           [sg.T(' ' * 20, key='-T5-')],
           [sg.Button('Conoce mas del juego',button_color=('black','#fdae61'), key='-README-')],
           [sg.T(' ' * 20, key='-T6-')],
           [sg.Button('Nuestro Ranking',button_color=('black','#fdae61'), key='-RANKING-')] ]


layout = [ [sg.Text('Scrabble Ar', size=(15, 1), justification='center', font=("Verdana", "30", "bold"),text_color='#d7191c', key= '-T7-')],
           [sg.Image(r'ScrabbleArBackGround.png',size=(400,350), key='-T8-')],
           [sg.Column(column1, key='-C1-'), sg.VSeparator(key='-VS-'),sg.Column(column2, key='-C2-')] ]

window1 = sg.Window('ScrabbleAr ',layout)

while True:
    event,value=window1.read()
    if event == None:
        break
    if event == '-ADVANCED_CONFIG-':
        Config.main()
    if event == '-README-':
        ConoceMas.main()
    if event == '-RANKING-':
        Ranking.main()
    if event == '-SIGN_UP-':
        Registro.main()
        window1['-SIGN_UP-'].Update(disabled=True)
    if event == '-LOGIN-':
        usuario= value['nick']
        password= value['password']
        lista_jugadores= ListaJugadores()

        a = Database.abro_base()
        try:
            if a != None:
                lista_jugadores_2 = Database.abro_base()
                usuario_valido = False
                for jugador in lista_jugadores_2.get_jugadores():
                    if jugador.get_nick() == usuario and jugador.get_password() == password:
                        usuario_valido = True
                        break
                if usuario_valido:
                    window1.close()
                    SelectorNiveles.main()
                else:
                    sg.SystemTray.notify('Error', 'Los datos ingresados no son correctos ')
            else:
                sg.SystemTray.notify('Error', 'No existen usuarios registrados, seleccionar la opción REGISTRARSE en el menú')
        except NameError:
            break
