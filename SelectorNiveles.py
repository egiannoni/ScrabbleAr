import PySimpleGUI as sg
import GameEasy
import GameMedium
import GameHard

sg.theme('LightBrown3')

#Armo el diseño de la interface
layout = [[sg.Text('Seleccione el nivel que desea jugar',font=("Verdana", "11", "bold"),text_color='#d7191c')],
          [sg.T(' ' * 30)],
          [sg.T(' ' * 30)],
          [sg.Button('Fácil',button_color=('black','#fdae61')), sg.Button('Medio',button_color=('black','#fdae61')), sg.Button('Difícil',button_color=('black','#fdae61'))]
         ]


def main ():
    """ Principal loop """
    window3 = sg.Window('Scrabble AR', layout)
    event, values = window3.read()
    while True:
        if event == 'Fácil':
            GameEasy.main()
        if event == 'Medio':
            GameMedium.main()
        if event == 'Difícil':
            GameHard.main()

    window3.close()
if __name__ == '__main__':
    main()
