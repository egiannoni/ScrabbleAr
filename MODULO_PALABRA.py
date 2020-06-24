# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:39:50 2020

@author: Victoria
"""

#recordar hacer los siguientes importar en el "código maestro"
#import pattern.es 
#from pattern.es import parse, split


class Palabra:
    def __init__(self, palabra, location, player, direction, board):
        self.palabra = palabra.upper()
        self.location = location
        self.player = player
        self.direction = direction.lower()
        self.board = board

#Este código logra verificar a partir de 7 letras dadas al azar qué palabras se pueden formar y que pertenezcan
# a una base de datos de palabras (en nuestro caso sust, adj o verbos de Pattern), a modo de verificación de funcionamiento/
#ejemplificación se pone un conjunto de 7 letras y un set de palabras predefinido 

def letra_cuenta(palabra): 
    """Cuenta las letras en la palabra"""
    dict = {} 
    for i in palabra: 
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def palabras_posibles(basepalabras, seleccion_letras): 
    #"basepalabras" son las palabras en pattern posibles según el nivel de complegidad
    #"seleccion_letras" son las 7 letras que se repartieron de froma random (tanto a pc como a usuario) 
    for palabra in basepalabras: 
        flag = 1
        cuenta = letra_cuenta(palabra) 
        lista_palabras_posibles=[]
        for key in cuenta: 
            if key not in seleccion_letras: 
                flag = 0
            else: 
                if seleccion_letras.count(key) != cuenta[key]: 
                    flag = 0
        if flag == 1: 
            lista_palabras_posibles.append(palabra)
    return lista_palabras_posibles

##############################################################################
##############################################################################

#El siguiente código programa trae de pattern los verbos, sustantivos y adjetivos. 
#Los organiza en listas separadas y calcula el puntaje de las palabras según el valor de 
#cada una de las letras que la conforman y arma un diccionario tal que es {'sustantivo1':valor,
#'sustantivo2':valor,..... } así para todos los sustantivos de pattern y así con adjetivos y con 
#verbos.

#considerar que para que el cálculo de puntaje y el armado de listas de "sustantivos", "adjetivos" 
#y "verbos" se utilizó "scores" como se comenta a continuación:
#scores = {"a": 1, "c": 2, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, 
#          "h": 4, "k": 8,"ñ": 8, "j": 6, "m": 3, "l": 1, "o": 1, 
#          "n": 1, "q": 8, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, 
#          "w": 8, "v": 4, "y": 4,"x": 8, "z": 10}
#tmb considerar que para que funcione este código necesito traer de pattern.es parse y split
#como se comenta a continuación:
#import pattern.es 
#from pattern.es import parse, split    

#si se quiere verificar la funcionalidad de el código en apartado basta realizar:
#a = dict_puntaje_verbos(verbos)
#print(a) 
#por dar un ejemplo.   

def calc_puntaje(palabra):
    """Calcula el puntaje a una palabra dada."""
    palab_puntaje = 0
    for letra in palabra:
        palab_puntaje += scores[letra]
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

def dict_puntaje_adjetivos(adjetivos):
    """Crear diccionarios de los adjetivos con los puntajes."""
    diccionario_puntajes_adj = {}
    for adjetivo in adjetivos:
        palabra_puntaje = calc_puntaje(adjetivo)
        diccionario_puntajes_adj[adjetivo] = palabra_puntaje
    return  diccionario_puntajes_adj

def dict_puntaje_sustantivos(sustantivos):
    """Crear diccionarios de los sustantivos con los puntajes."""
    diccionario_puntajes_sust = {}
    for sustantivo in sustantivos:
        palabra_puntaje = calc_puntaje(sustantivo)
        diccionario_puntajes_sust[sustantivo] = palabra_puntaje
    return  diccionario_puntajes_sust



******************************************************************************
    def revisa_palabra(self):
        #Revisa palabra para ver si existe en base de datos, y que la ubicación respeta ciertos aspectos
        
        
        global round_number, players
        palabra_score = 0
        global dictionary
        if "dictionary" not in globals():
            dictionary = open("dic.txt").read().splitlines()

        current_board_ltr = ""
        needed_tiles = ""
        blank_tile_val = ""

        #Assuming that the player is not skipping the turn:
        if self.palabra != "":         

            #Raises an error if the palabra being played is not in the official scrabble dictionary (dic.txt).
            if self.palabra not in dictionary:
                return "Please enter a valid dictionary palabra.\n"
            #Raises an error if the player does not have the correct tiles to play the palabra.
            for letter in needed_tiles:
                if letter not in self.player.get_rack_str() or self.player.get_rack_str().count(letter) < needed_tiles.count(letter):
                    return "You do not have the tiles for this palabra\n"
             #Ensures that first turn of the game will have the palabra placed at (7,7).
            if round_number == 1 and players[0] == self.player and self.location != [7,7]:
                return "The first turn must begin at location (7, 7).\n"
            return True

 
    def calculate_palabra_score(self):
        #Calculates the score of a palabra, allowing for the impact by premium squares.
        global LETTER_VALUES, premium_spots
        palabra_score = 0
        for letter in self.palabra:
            for spot in premium_spots:
                if letter == spot[0]:
                    if spot[1] == "TLS":
                        palabra_score += LETTER_VALUES[letter] * 2
                    elif spot[1] == "DLS":
                        palabra_score += LETTER_VALUES[letter]
            palabra_score += LETTER_VALUES[letter]
        for spot in premium_spots:
            if spot[1] == "TWS":
                palabra_score *= 3
            elif spot[1] == "DWS":
                palabra_score *= 2
        self.player.increase_score(palabra_score)

    def set_palabra(self, palabra):
        self.palabra = palabra.upper()

    def set_location(self, location):
        self.location = location

    def set_direction(self, direction):
        self.direction = direction

    def get_palabra(self):
        return self.palabra