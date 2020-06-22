import PySimpleGUI as sg
import json

def abro_datos(nombre):
    with open(nombre,"r") as archdatos:
        base_datos=json.load(archdatos)
    return (base_datos)

def ranking(x):
    puntos={}
    try:
        for key in x:
            puntos[key]= int(x[key][0])
            rank = sorted(puntos.items(),key=lambda jugador: jugador[1],reverse=True)
    except KeyError :
        rank = "no hay jugadores que mostrar aun"
    return rank


def ventana(lista):
    diseño=[ [sg.Listbox(lista, size=(20, 12), key='ranking')],
             [sg.Button('ok')] ]
    window = sg.Window('Ranking General del ScrabbleAr', diseño)
    window.finalize ()

while True :
    datos=abro_datos('base_datos.json')
    rank=ranking(datos)
    ventana(rank)
    event, values = window.read()
    if event == 'ok':
        window.close()
    if event == sg.WIN_CLOSED:
        break




#def main():
#if __name__ == '__main__':
#    main()
