import PySimpleGUI as sg
from MODULO_BASEDEDATOS import AbroBase
from MODULO_JUGADORES import ListaJugadores

def ventana(lista):
    diseño=[ [sg.Listbox(lista, size=(20, 12), key='ranking')],
             [sg.Button('ok')] ]
    window3 = sg.Window('Ranking General del ScrabbleAr', diseño)
    window3.finalize ()

def main():
    MostrarJugadores=ListaJugadores.jugadores
    while True :
        rank=ListaJugadores.mostrar_informacion(MostrarJugadores)
        ventana(rank)
        event, values = window3.read()
        if event == 'ok':
            window3.close()
        if event == sg.WIN_CLOSED:
            break

if __name__ == '__main__':
    main()


#### Todavia no muestra el ranking porque la funcion ranking no esta definida
#### quiero que me muestre aunque sea la lista de jugadores.
