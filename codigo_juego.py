import random 
import pattern

bolsa=['A'*11,'B'*3,'C'*4,'D'*4,'E'*11,'F'*2,'G'*2,'H'*2,'I'*6,
       'J'*2,'K'*1,'L'*6,'M'*4,'N'*5,'Ñ'*1,'O'*8,'P'*3,'Q'*1,
       'R'*6,'S'*7,'T'*4,'U'*6,'V'*2,'W'*1,'X'*1,'Y'*1,'Z'*1]

def quien_empieza():
    if random.randint(0, 1) == 0:
        return pc
    else:
        return usuario


def tableros():    
    letras_usuario=[]
    letras_pc=[]
    for i in range(7):
         letra=random.choice(bolsa)
         letras_usuario.append(letra)
    return letras_usuario
    for i in range(7):
         letra=random.choice(bolsa)
         letras_pc.append(letra)
    return letras_pc


def variables_inicio(bolsa):
    cantidad_fichas=len(bolsa)
    puntaje_jugador=0
    puntaje_pc=0


##### PROGRAMA PRINCIPAL
tableros()
empieza= quien_empieza()
while cantidad_fichas !=0 or puntaje_jugador =< 300 or puntaje_pc =< 300 :
    if empieza == pc:
        ....
    else: 
        ....
