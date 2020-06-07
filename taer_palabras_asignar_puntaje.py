# -*- coding: utf-8 -*-
"""
Created on Wed May 27 10:16:38 2020

@author: Victoria
"""
#Este programa trae de pattern los verbos, sustantivos y adjetivos. Los organiza en listas separadas.
#También se calcula el puntaje de las palabras según los puntos por letra y organiza pares palabra-puntaje en diccionarios por categoría

import pattern.es 
from pattern.es import parse, split

scores = {"a": 1, "c": 2, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, 
          "h": 4, "k": 8, "ll": 8, "ñ": 8, "j": 6, "m": 3, "l": 1, "o": 1, 
          "n": 1, "q": 8, "p": 3, "s": 1, "rr": 8, "r": 1, "u": 1, "t": 1, 
          "w": 8, "v": 4, "y": 4,"x": 8, "z": 10}


def calc_puntaje(palabra):
    """Calcula el puntaje a una palabra dada."""
    palab_puntaje = 0
    for letra in palabra:
        for x,y in scores.items():
            palab_puntaje += scores[x]
    return palab_puntaje

def list_verbos():
    """Armo lista de verbos."""
    lista_verbos = []
    for x in pattern.es.lexicon.keys():
        if x in pattern.es.spelling.keys():
            s = (pattern.es.parse(x)).split()
            for cada in s:
                for c in cada:
                    if c[1] == 'VB':
                        lista_verbos.append(c[0])                    
    return(lista_verbos)
    
def list_adjetivos():
    """Armo lista de adjetivos."""
    lista_adjetivos = []
    for x in pattern.es.lexicon.keys():
        if x in pattern.es.spelling.keys():
            s = (pattern.es.parse(x)).split()
            for cada in s:
                for c in cada:
                    if c[1] == 'JJ':
                        lista_adjetivos.append(c[0])                    
    return(lista_adjetivos)    
    
def list_sustantivos():
    """Armo lista de sustantivos."""
    lista_sustantivos = []
    for x in pattern.es.lexicon.keys():
        if x in pattern.es.spelling.keys():
            s = (pattern.es.parse(x)).split()
            for cada in s:
                for c in cada:
                    if c[1] == 'NNS'or c[1] ==  "NN":
                        lista_sustantivos.append(c[0])                    
    return(lista_sustantivos)        

verbos = list_verbos()  
adjetivos = list_adjetivos()      
sustantivos = list_sustantivos()
      
def dict_puntaje_verbos(verbos):
    """Crear diccionarios de los verbos con los puntajes."""
    diccionario_puntajes_verb = {}
    for verbo in verbos:
        palabra_puntaje = calc_puntaje(verbo)
        diccionario_puntajes_verb[verbo] = palabra_puntaje
    return  diccionario_puntajes_verb

#a = dict_puntaje_verbos(verbos)
#print(a)

def dict_puntaje_adjetivos(adjetivos):
    """Crear diccionarios de los adjetivos con los puntajes."""
    diccionario_puntajes_adj = {}
    for adjetivo in adjetivos:
        palabra_puntaje = calc_puntaje(adjetivo)
        diccionario_puntajes_adj[adjetivo] = palabra_puntaje
    return  diccionario_puntajes_adj

b = dict_puntaje_adjetivos(adjetivos)
print(b)

def dict_puntaje_sustantivos(sustantivos):
    """Crear diccionarios de los sustantivos con los puntajes."""
    diccionario_puntajes_sust = {}
    for sustantivo in sustantivos:
        palabra_puntaje = calc_puntaje(sustantivo)
        diccionario_puntajes_sust[sustantivo] = palabra_puntaje
    return  diccionario_puntajes_sust

#c = dict_puntaje_sustantivos(sustantivos)
#print(c)


