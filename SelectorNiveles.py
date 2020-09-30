import PySimpleGUI as sg
import Game

sg.theme('LightBrown3')

#Armo el diseño de la interface
layout = [[sg.Text('Seleccione el nivel que desea jugar',font=("Verdana", "11", "bold"),text_color='#d7191c')],
          [sg.T(' ' * 30)],
          [sg.T(' ' * 30)],
          [sg.Button('Fácil',button_color=('black','#fdae61')), sg.Button('Medio',button_color=('black','#fdae61')), sg.Button('Difícil',button_color=('black','#fdae61'))]
         ]


def main (players_list, player, username, easy_config, medium_config, hard_config):
    """ Principal loop """
    window3 = sg.Window('Scrabble AR', layout)
    event, values = window3.read()
    while True:
        if event == 'Fácil':
            window3.close()
            Game.main(players_list, player, username, easy_config)
            break
        if event == 'Medio':
            window3.close()
            Game.main(players_list, player, username, medium_config)
            break
        if event == 'Difícil':
            window3.close()
            Game.main(players_list, player, username, hard_config)
            break


if __name__ == '__main__':
    main()
