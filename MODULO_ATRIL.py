# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:59:29 2020

@author: Victoria
"""

class Atril:
    
#formato bolsa utilizado para selccionar fichas

# bolsa=['A'*11,'B'*3,'C'*4,'D'*4,'E'*11,'F'*2,'G'*2,'H'*2,'I'*6,
#        'J'*2,'K'*1,'L'*6,'M'*4,'N'*5,'Ñ'*1,'O'*8,'P'*3,'Q'*1,
#        'R'*6,'S'*7,'T'*4,'U'*6,'V'*2,'W'*1,'X'*1,'Y'*1,'Z'*1]

#tener en consideración que para que este código funcione necesito en el código que 
#llame a esta clase importar random    

    def __init__(self, bolsa):
        self.bolsa = bolsa
        
    def tableros(self):
        """Reparte 7 letras a usuario y 7 a pc, quita esas letras de bolsa"""
        letras_usuario=[]
        letras_pc=[]
        for i in range(7):
             letra=random.choice(self.bolsa)
             letras_usuario.append(letra)
             #método válido si bolsa es lista, modificar pertinentemente si bolsa es diccionario
             a = self.bolsa.index(letra)
             del(self.bolsa[a])
        return letras_usuario
        for i in range(7):
             letra=random.choice(self.bolsa)
             letras_pc.append(letra)
              #método válido si bolsa es lista, modificar pertinentemente si bolsa es diccionario
             a = self.bolsa.index(letra)
             del(self.bolsa[a])
        return letras_pc
              
    def num_letras_quedan_enbolsa(self):
        """me dice cuantas letras quedan todavía en la bolsa"""
        """recordar que estamos asumiendo bolsa=lista, cambiar pertinentemente de hacer falta"""
        return len(self.bag)            
            
            
    
