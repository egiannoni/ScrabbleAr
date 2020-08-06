##################
### ScrabbleAr ###
##################

----------------------------------------------------------------------------------------------------
ScrabbleAR es un juego basado en el popular juego Scrabble, en el que se intenta ganar puntos mediante la construcción de palabras sobre un tablero.

Desarrollado por Eugenia Giannoni, Norberto Ariel Chaar y Victoria Hipatia Olivera Craig. 

En todos los casos se han utilizado imágenes o sonidos, libres o propios, que puedan ser publicados con licencias libres.

Esta versión de Scrabble cuenta con tres niveles de dificultad, cada nivel de dificultad tiene un tablero distinto asociado siendo 
las acciones de los casilleros especiales distinta en cada uno de ellos. 

La paleta de colores presente en los tablero fue especialmente seleccionada para que los puedan disfrutar usuarios con insuficiencia 
en la visión del color (contemplando variantes). Los colores fueron seleccionados y evaluados utilizando herramientas de dominio público 
(CVSimulator, https://asada.website/webCVS/; Color Advice for Cartography, https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3) 

----------------------------------------------------------------------------------------------------

Requisitos del Sistema:

+ Python 3.6
    + Paquete Pattern Version 3.6
    + Paquete PySimpleGUI Version 4.21.0
    
----------------------------------------------------------------------------------------------------
Ejecución del programa - Guía para el usuario 

Para iniciar el juego deberás ejecutar el archivo "ScrabbleAR.py" el cual te llevará directamente a la plataforma de inicio de sesión. 

Si nunca jugaste con nuestros tableros te invitamos a que registres y comiences a disfrutar de nuestro juego para demostrarle a la pc que tu 
eres más inteligente. 

Una vez iniciada la sesión deberás elegir entre niveles Fácil, Medio o Difícil según tu preferencia.

La primer letra deberá ubicarse siempre en el casillero central del tablero. Se pueden armar palabras de arriba hacia abajo y de izquierda a 
derecha. El turno se elige al azar entre el usuario y la computadora.

Colores (código hex adjunto para facilitar interpretación) y acciones de casilleros especiales por nivel:

*Fácil: los casilleros naranjas (#fdae61) multiplican x3 los puntos de la palabra a partir de sumar los puntos de las letras de forma individual 
y los casilleros rojos (#d7191c) multiplican x2 los puntos de la palabra a partir de sumar los puntos de las letras de forma individual.
 
*Medio: los casilleros naranjas (#fdae61) multiplican x3 los puntos de la palabra a partir de sumar los puntos de las letras de forma individual, 
los casilleros rojos (#d7191c) multiplican x2 los puntos de la palabra a partir de sumar los puntos de las letras de forma individual,  los casilleros 
azules (#2c7bb6) restan 1 punto de los puntos de la palabra a partir de sumar los puntos de las letras de forma individual y  los casilleros celestes
 (#abd9e9) restan 3 puntos de  los puntos de la palabra a partir de sumar los puntos de las letras de forma individual.

*Difícil: los casilleros salmón (#f46d43) restan 5 puntos de los puntos de la palabra a partir de sumar los puntos de las letras de forma individual,
 los casilleros celestes (#abd9e9) multiplican x2 los puntos de la palabra a partir de sumar los puntos de las letras de forma individual,  los 
 casilleros azules (#2c7bb6) restan 1 punto de los puntos de la palabra a partir de sumar los puntos de las letras de forma individual y  los casilleros
  granate (#a50026) restan 3 puntos de  los puntos de la palabra a partir de sumar los puntos de las letras de forma individual.

El juego finalizará una vez que se pulse el botón “Terminar” o que se acabe el tiempo (nivel “Fácil” = 900 seg, nivel “Medio” = 600 seg y nivel 
“Difícil” = 300 seg)


Los desarrolladores te deseamos mucha suerte!! 

----------------------------------------------------------------------------------------------------
Estructura del programa - Guía para programadores

ScrabbleAr es un juego desarrollado en lenguaje Python, con librerías bajo licencia libre. 
A su vez, se ha dejado una carpeta "ModulosPOO" con partes del código que no se llegaron a utilizar en el desarrollo final pero que fueron creados con la 
intención de que ScrabbleAR estuviera desarrollado con lenguaje orientado a objetos en su integridad.
La mayor parte del código, como así también la mayor parte de los comentarios realizados en el mismo, fue desarrollado en inglés con la intención de facilitar
 su accesibilidad y edición sin importar desde qué parte del mundo se haga y por quién. 



###########################
### ScrabbleAr - English###
###########################

----------------------------------------------------------------------------------------------------
ScrabbleAR is a game based on the popular game Scrabble, in which you try to get points
by placing words on a board.

This game was developed by Eugenia Giannoni, Norberto Ariel Chaar and Victoria Hipatia Olivera Craig.

In all cases, images or sounds, free or own, that can be published with free licenses have been used.

This version of Scrabble has three levels of difficulty, each level of difficulty has a different board associated, the actions of the special squares are 
different in each one of them.

The color palette present on the boards was specially selected so it can be enjoyed by users with insufficient color vision (variants being considered). 
Colors were selected and evaluated using public domain tools (CVSimulator, https://asada.website/webCVS/; Color Advice for Cartography, 
https://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3)

----------------------------------------------------------------------------------------------------

System Requirements:

+ Python 3.6
    + Pattern Version 3.6 Package
    + PySimpleGUI Version 4.21.0 Package
    
----------------------------------------------------------------------------------------------------
Program Execution - User Guide

To start the game you must run the file "ScrabbleAR.py" which will take you directly to the login platform.

If you never played with our boards we invite you to register and start enjoying our game so you can demonstrate that you are smarter than the computer.

Once the session starts, you must choose between Easy (“Fácil”), Medium (“Medio”) or Hard (“Difícil”) levels according to your preference.

The first letter must always be located in the central box of the board. Words can be assembled from top to bottom and from left to right. The shift is
 chosen randomly between the user and the computer.

Colors (hex code attached for easy interpretation) and actions of special lockers by level:

* Easy: the orange boxes (# fdae61) multiply the word points x3 by adding the letter points individually and the red boxes (# d7191c) multiply the word 
points x2 by adding the points of the letters individually.
 
* Medium: the orange boxes (# fdae61) multiply the word points x3 by adding the letter points individually, the red boxes (# d7191c) multiply the word 
points x2 by adding the points of the letters individually, the blue boxes (# 2c7bb6) subtract 1 point from the points of the word from adding the points
 of the letters individually and the light blue boxes (# abd9e9) subtract 3 points from the points of the word from adding the points of the letters individually.

* Difficult: the salmon squares (# f46d43) subtract 5 points from the word points from adding the letter points individually, the light blue boxes (# abd9e9)
 multiply x2 the word points from adding the letter points individually, the blue boxes (# 2c7bb6) subtract 1 point from the word points from adding the letter
 points individually and the maroon boxes (# a50026) subtract 3 points from the word points from adding the letter points individually.

The game will end once the "Finish" button is pressed or the time is up (level "Easy" = 900 sec, level "Medium" = 600 sec and level "Hard" = 300 sec)


We, the developers, wish you the best of luck !!

----------------------------------------------------------------------------------------------------
Program Structure - Programmer's Guide

ScrabbleAr is a game developed in Python, free licensed libraries had been used.
A "ModulosPOO" folder has been left with parts of the code that were not used in the final script but that were created with the intention that ScrabbleAR were 
entirely developed as object-oriented.
Most of the code, as well as most of the comments made on it, are in English with the intention of facilitating the access and edition no matter where in the world 
it is made and by whom.
