# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:23:57 2020

@author: Victoria
"""

#Este código logra verificar a partir de 7 letras dadas al azar qué palabras se pueden formar y que pertenezcan
# a una base de datos de palabras (en nuestro caso sust, adj o verbos de Pattern), a modo de verificación de funcionamiento/
#ejemplificación se pone un conjunto de 7 letras y un set de palabras predefinido 

def letra_cuenta(palabra): 
    dict = {} 
    for i in palabra: 
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def palabras_posibles(basepalabras, seleccion_letras): 
    for palabra in basepalabras: 
        flag = 1
        cuenta = letra_cuenta(palabra) 
        for key in cuenta: 
            if key not in seleccion_letras: 
                flag = 0
            else: 
                if seleccion_letras.count(key) != cuenta[key]: 
                    flag = 0
        if flag == 1: 
            print(palabra) 

    
#ejemplo (cuando lo implementemos el input es la lista/dict de palabras del  pattern y seleccion_letras son las 7 letras random que le toca a la pc)

if __name__ == "__main__": 
    input = ['gol', 'bata', 'me', 'mola', 'auto', 'chau', 'cumbia'] 
    seleccion_letras = ['e', 'o', 'b', 'a', 'm', 'g', 'l'] 
    palabras_posibles(input, seleccion_letras) 