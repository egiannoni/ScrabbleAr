import random
from configuracion import Configuracion


class Atril():
    
#hay que llamar de configuracion a getCantidadDeFichasPorLetra (diccionario al 
#que llamo "bolsa") donde
#self._cantidad_de_fichas_por_letra = cantidades y cantidades es de tipo: 
  # cantidades = {1: ['Y', 'K', 'LL', 'Ñ', 'Q', 'RR', 'W', 'X', 'Z'],
  #           2: ['G', 'P', 'F', 'H', 'V', 'J'], 3: ['M', 'B'],
  #           4: ['R', 'L', 'T', 'C', 'D'], 5: ['N'], 6: ['I', 'U'],
  #           7: ['S'], 8: ['O'], 11: ['A', 'E']}
  
#es conveniente pasarlo de formato, para eso:  
    cantidades_formato_amigo = {value: key for key in cantidades for value in cantidades[key]}
    temporal_cantidades=[]
    for key, value in cantidades_formato_amigo.items():
        for i in range(value):
            temporal_cantidades.append(key)    
    #temporal_cantidades es una lista de tipo ['Y','K','G','G',...] donde cada elemento es una letra
    #temporal_cantidades es mi bolsa a partir de donde voy a elegir siete fichas y sacarlas en la repartida  
    
 #######Ahora si la clase#########   

    def __init__(self, bolsa):
        self.bolsa = temporal_cantidades        
        #verificar si esto esta bien, ver comentarios de abajo a modo guia para interpretar 
        #que se busca con este código
        
    def TableroUsuario(self):
        """Reparte 7 letras a usuario y 7 a pc, quita esas letras de bolsa"""
        letras_usuario=[]
        for i in range(7):
             letra=random.choice(self.bolsa)
             letras_usuario.append(letra)
             a = self.bolsa.index(letra)
             del(self.bolsa[a])
        return letras_usuario
    
    def TableroPc (self):
        letras_pc=[]
        for i in range(7):
             letra=random.choice(self.bolsa)
             letras_pc.append(letra)
             a = self.bolsa.index(letra)
             del(self.bolsa[a])
        return letras_pc
              
    def num_letras_quedan_enbolsa(self):
        """me dice cuantas letras quedan todavía en la bolsa"""
        """recordar que estamos asumiendo bolsa=lista, cambiar pertinentemente de hacer falta"""
        return len(self.bag)            
            
#BORRAR UNA VEZ QUE SE CONECTÓ EL CODIGO DE ARRIBA CON LOS OTROS MODULOS DE FORMA
#CORRECTA    
#código de prueba de lo que está arriba para verificar que anda: 
# import random

# cantidades = {
#             1: ['Y', 'K', 'LL', 'Ñ', 'Q', 'RR', 'W', 'X', 'Z'],
#             2: ['G', 'P', 'F', 'H', 'V', 'J'],
#             3: ['M', 'B'],
#             4: ['R', 'L', 'T', 'C', 'D'],
#             5: ['N'],
#             6: ['I', 'U'],
#             7: ['S'],
#             8: ['O'],
#             11: ['A', 'E']
#         }


# cantidades_formato_amigo = {value: key for key in cantidades for value in cantidades[key]}
# temporal_cantidades=[]
# for key, value in cantidades_formato_amigo.items():
#     for i in range(value):
#         temporal_cantidades.append(key)
# def TableroUsuario():
#         """Reparte 7 letras a usuario y 7 a pc, quita esas letras de bolsa"""
#         letras_usuario=[]
#         for i in range(7):
#               letra=random.choice(temporal_cantidades)
#               letras_usuario.append(letra)
#               #método válido si bolsa es lista, modificar pertinentemente si bolsa es diccionario
#               a = temporal_cantidades.index(letra)
#               del(temporal_cantidades[a])
#         return letras_usuario

# list_letras = TableroUsuario()
# print(list_letras) #letras usuarios
# print(temporal_cantidades) #letras restantes en la bolsa menos las siete de la mano      
            
    
