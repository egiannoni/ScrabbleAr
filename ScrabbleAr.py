import PySimpleGUI as sg 
import json 
import conoce_mas
import ranking 
import registro
import pantalla_principal


diseño = [  [sg.Text('Scrabble Ar', size=(15, 1), justification='center', font=("Times", "24", "bold italic"),text_color='black')],
            [sg.T(' ' * 7),sg.InputText('Nick',size=(30, 1),text_color='gray',key='nick')],
            [sg.T(' ' * 7),sg.InputText('Pass',size=(30, 1),text_color='gray',key='pass',password_char='*')],
            [sg.T(' ' * 20),sg.Button(' Iniciar Sesion  ')],
            [sg.T(' ' * 22),sg.Button('Registrarse')],
            [sg.T(' ' * 30)],
            [sg.Button('Conoce mas del juego'),sg.T(' ' * 5), sg.Button('Nuestro Ranking')] ]

window = sg.Window(' ').layout(diseño)

while True:
    # archivo = open("base_datos", "a+")       ## ABRO EL ARCHIVO de la base de datos
    # datos = json.load(archivo)
    event,value=window.read()
    if event == None:
        break
    if event == 'Conoce mas del juego':
        conoce_mas.main()
    if event == 'Nuestro Ranking':
        ranking.main()
    if event == 'Registrarse':
        registro.main()
    if event == ' Iniciar Sesion  ':
        break
    #     ## este es un loop que tiene que evaluar si existe el nick ver si la contraseña es igual
    #     ## a la que tiene el usuario y recien ahi cerrar la ventana de inicio y abrir el menu principal        
        # if value['nick'] in base_datos:  
        #     if value['pass'] == nick_pass:
        #         window.close()
        #         pantalla_principal.main()

        
        
        
        
        
        
        
