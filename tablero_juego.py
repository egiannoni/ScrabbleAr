import PySimpleGUI as sg
import random
import MODULO_ATRIL
import MODULO_TABLERO


############### MODULOS ############################
#bolsa{ letra: [cantidad,valor]}  por ahora tenemos listas pero creemos que mejor seria un diccionario

bolsa=['A'*11,'B'*3,'C'*4,'D'*4,'E'*11,'F'*2,'G'*2,'H'*2,'I'*6,
       'J'*2,'K'*1,'L'*6,'M'*4,'N'*5,'Ñ'*1,'O'*8,'P'*3,'Q'*1,
       'R'*6,'S'*7,'T'*4,'U'*6,'V'*2,'W'*1,'X'*1,'Y'*1,'Z'*1]

def quien_empieza():
    if random.randint(0, 1) == 0:
        return 'pc'
    else:
        return 'usuario'



event,values = window.read()


##### PROGRAMA PRINCIPAL
letras_usuario,letras_pc=tableros(bolsa)
empieza= quien_empieza()
cantidad_fichas=len(bolsa)
puntaje_jugador=0
puntaje_pc=0
while cantidad_fichas !=0 or puntaje_jugador =< 300 or puntaje_pc =< 300 :   #Los 300son provisorios
    if empieza == pc:
        ....
    else:
        ....
