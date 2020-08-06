import PySimpleGUI as sg
import Database

def ventana(lista):
    diseño=[ [sg.Listbox(lista, size=(30,15), key='ranking')],
             [sg.Button('ok')] ]
    window = sg.Window('Ranking', diseño)
    return window

def main():
    try:
        lista_jugadores=Database.abro_base()
        rank=lista_jugadores.mostrar_ranking()
    except NameError:
        rank= 'No hay jugadores para mostrar'
    window3=ventana(rank)
    event, values = window3.read()
    if event == 'ok':
        window3.close()

if __name__ == '__main__':
    main()
