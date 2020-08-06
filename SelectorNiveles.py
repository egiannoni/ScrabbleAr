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
            window3.close()
            GameEasy.main()
            break
        if event == 'Medio':
            window3.close()
            GameMedium.main()
            break
        if event == 'Difícil':
            window3.close()
            GameHard.main()
            break


if __name__ == '__main__':
    main()
