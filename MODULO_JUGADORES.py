############ GENERACION DE JUGADORES #############
class Jugador:

    jugadores_todos={}
    #quiero crear un dic que sea clave nick valor puntaje para despues poder sacar el ranking.
    def todos_los_jugadores(cls):
            Jugador.jugadores_todos[Jugador.get_nick]=Jugador.get_puntaje
            return (Jugador.jugadores_todos)


    def __init__(self, pas,nick,nombre,apellido,nacionalidad,correo):

        self._pas = pas
        self._nick = nick
        self._nombre = nombre
        self._apellido = apellido
        self._nacionalidad = nacionalidad
        self._correo = correo
        self._puntaje = 0

    def get_nombre (self):
        return self._nombre

    def get_nick (self):
        return self._nick

    def get_pas (self):
        return self._pas

    def get_apellido (self):
        return self._apellido

    def get_nacionalidad (self):
        return self.get_nacionalidad

    def get_correo (self):
        return self.get_correo

    def agregar_puntos(self, cantidad_puntos):
        self._puntaje += cantidad_puntos


def ranking(self):
    for clave,valor in  Jugador.jugadores_todos.items():
        print("{} tiene {} puntos".format(clave,valor))

nico=Jugador('344','nico','nicolas','perez','argentino','nico@hotmail.com')
euge=Jugador('55535','euge','eugenia','giannoni','argentina','euge@hotmail.com')
coni=Jugador('er54','coni','constanza','gonzales','argentina','coni@gmail.com')

print(Jugador.jugadores_todos)



#        try:
#               puntos[key]= int(x[key][0])
#                rank = sorted(puntos.items(),key=lambda jugador: jugador[1],reverse=True)
#        except KeyError :
#            rank = "no hay jugadores que mostrar aun"
#        return rank
