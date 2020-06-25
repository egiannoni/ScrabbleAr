# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:39:50 2020

@author: Victoria
"""
import pattern.es
import Configuracion 


#AYUDA PLEASE!acá tengo dudas de como vincular las variables, dsp uso "puntajes", ver que 
#programé para puntajes en diccionario tal que puntajes = {'letra':'puntos'}
#hay que cambiar...también dudo de si estas variables tienen que ir adentro de l clase
puntaje = Configuracion()
puntajes = puntaje.getPuntajeDeCadaFicha

#recordar hacer los siguientes importar en el "código maestro"
#import pattern.es 
#from pattern.es import parse, split


class Palabra():
    def __init__(self, palabra, basepalabras, seleccion_letras):
        self.palabra = palabra.upper()
        self.basepalabras = basepalabras
        self.seleccion_letras = seleccion_letras
       
#Este código logra verificar a partir de 7 letras dadas al azar qué palabras se pueden formar y que pertenezcan
# a una base de datos de palabras (en nuestro caso sust, adj o verbos de Pattern), a modo de verificación de funcionamiento/
#ejemplificación se pone un conjunto de 7 letras y un set de palabras predefinido 

    def letra_cuenta(self): 
        """Cuenta las letras en las palabras de la base de datos tal que si encuentra "cumbia", 
        por ejemplo, arma: {'c':1,'u':1,'m':1,'b':1,'i':1,'a':1} """
        dict = {} 
        for i in self.palabra: 
            dict[i] = dict.get(i, 0) + 1
        return dict 
  
    def palabras_posibles(self): 
        """Función que llama a la función letra_cuenta y arma a partir de letras dadas arbitrariamente,
        en nuestro caso 7 letras entregadas al azar de la bolsa de letras del scrabble, palabras que
        existan en la base de datos (que es sust, adj y/o verb de pattern.es según el nivel)"""
        #"basepalabras" son las palabras en pattern posibles según el nivel de complegidad
        #"seleccion_letras" son las 7 letras que se repartieron de froma random (tanto a pc como a usuario) 
        for palabra in self.basepalabras: 
            flag = 1
            cuenta = letra_cuenta(palabra) 
            lista_palabras_posibles=[]
            for key in cuenta: 
                if key not in self.seleccion_letras: 
                    flag = 0
                else: 
                    if self.seleccion_letras.count(key) != cuenta[key]: 
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
#puntaje = {"a": 1, "c": 2, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, 
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

    def calc_puntaje(self):
        """Calcula el puntaje a una palabra dada a partir de diccionario de puntos por letra."""
        palab_puntaje = 0
        for letra in self.palabra:
            palab_puntaje += puntajes[letra]
        return palab_puntaje

    def list_verbos():
        """Armo lista de verbos a partir de pattern.es."""
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
        """Armo lista de adjetivos a partir de pattern.es."""
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
        """Armo lista de sustantivos a partir de pattern.es."""
        lista_sustantivos = []
        for x in pattern.es.lexicon.keys():
            if x in pattern.es.spelling.keys():
                s = (pattern.es.parse(x)).split()
                for cada in s:
                    for c in cada:
                        if c[1] == 'NNS'or c[1] ==  "NN":
                            lista_sustantivos.append(c[0])                    
        return(lista_sustantivos)        

#RESOLVER DUDA!tal vez no corresponda definir estas variables internas dentro de una clase?
    verbos = list_verbos()  
    adjetivos = list_adjetivos()      
    sustantivos = list_sustantivos()
#FIN DUDA!as siguientes tres funciones utilizan estas variables...    
    
      
    def dict_puntaje_verbos(verbos):
        """Crear diccionarios de los verbos con los puntajes según puntaje de cada letra."""
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

##############################################################################
##############################################################################

