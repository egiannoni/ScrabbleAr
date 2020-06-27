import PySimpleGUI as sg
from MODULO_BASEDEDATOS import AbroBase
import MODULO_JUGADORES


def ventana(lista):
    diseño=[ [sg.Listbox(lista, size=(20, 12), key='ranking')],
             [sg.Button('ok')] ]
    window3 = sg.Window('Ranking General del ScrabbleAr', diseño)
    window3.finalize ()

def main():
    while True :
        base=AbroBase('base_datos.pkl')
        rank=ListaJugadores.ranking()
        ventana(rank)
        event, values = window3.read()
        if event == 'ok':
            window3.close()
        if event == sg.WIN_CLOSED:
            break

if __name__ == '__main__':
    main()
