import PySimpleGUI as sg
from Jugadores import ListaJugadores

def ventana(lista):
    diseño=[ [sg.Listbox(lista, size=(30,15), key='ranking')],
             [sg.Button('ok')] ]
    window = sg.Window('Ranking', diseño)
    return window

def main():
    lista_jugadores=ListaJugadores()
    rank=lista_jugadores.mostrar_informacion()
    window3=ventana(rank)
    event, values = window3.read()
    if event == 'ok':
        window3.close()

if __name__ == '__main__':
    main()
