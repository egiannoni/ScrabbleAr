import pickle

class Jugador:
    """  Creates the gamers from information input on the registration """

    def __init__(self, pas,nick,nombre,apellido,nacionalidad,correo):

        self._password = pas
        self._nick = nick
        self._nombre = nombre
        self._apellido = apellido
        self._nacionalidad = nacionalidad
        self._correo = correo
        self._puntaje = 0

    def get_nombre (self):
        return self._nombre

    def get_puntos(self):
        return self._puntaje

    def get_nick (self):
        return self._nick

    def get_password (self):
        return self._password

    def get_apellido (self):
        return self._apellido

    def get_nacionalidad (self):
        return self.get_nacionalidad

    def get_correo (self):
        return self.get_correo

    def agregar_puntos(self, cantidad_puntos):
        self._puntaje += cantidad_puntos

    def __str__(self):
        return " + {} {} usa el nick {} y tiene {} puntos.".format(self._nombre, self._apellido, self._nick, self._puntaje)


class ListaJugadores:
    def __init__(self):
        self._jugadores=[]
    
    def cargar_fichero(self):
        try:
            with open("DatabaseGamers.pkl", "ab+") as arhivo:
                lista_jugadores_2 = pickle.load(arhivo)
        except EOFError:
            print("El fichero está vacío.")
    
    def get_jugadores(self):
        return self._jugadores
    
    def agregar_jugador(self, jugador):
        self._jugadores.append(jugador)
        self.guardar_jugadores()

    def mostrar_jugador(self):
        for jugador in self._jugadores:
            print(jugador.__str__())

    def guardar_jugadores(self):
        fichero = open("DatabaseGamers.pkl", "ab+")
        pickle.dump(self._jugadores, fichero)
        fichero.close()
        del fichero
    
    
    def mostrar_informacion(self):
        print("La información del fichero externo es la siguiente:")
        for jugador in self.jugadores:
            print( jugador.__str__() )

    def mostrar_ranking(self):
        lista={}
        for jugador in self.jugadores:
            nick=jugador.get_nick()
            puntos=jugador.get_puntos()
            lista[nick]=puntos        
        rank = sorted(lista.items(),key=lambda jugador: jugador[1],reverse=True)
        for i in rank :
            print( " +  el nick {} tiene {} puntos.".format(i[0], i[1]))


