# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:05:28 2020

@author: Victoria
"""

import pickle


def  abro_base():
    lista_jugadores_2 = None
    try:
        with open('DatabaseGamers.pkl', 'rb') as archivo:
            lista_jugadores_2 = pickle.load(archivo)
    except FileNotFoundError:
        print('no se encontró el archivo')
        pass
    return lista_jugadores_2

def guardo_base(lista_jugadores):    
    archivo = open('DatabaseGamers.pkl', 'wb')
    # archivo.seek(0)
    pickle.dump(lista_jugadores, archivo)
        