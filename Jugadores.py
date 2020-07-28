import pickle
import operator

class Jugador:
    """  Creates the gamers from information input on the registration """

    def __init__(self, pas,nick,nombre,apellido,nacionalidad,correo):

        self._pasword = pas
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

    def get_pas (self):
        return self._pasword

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
    jugadores = []

    def __init__(self):
        fichero = open("prueba.pkl", "ab+")
        fichero.seek(0)  # Desplazamos cursor al principio

        try:
            self.jugadores = pickle.load(fichero)  # Cargamos información
            print("Se cargaron {} personas.".format(len(self.jugadores)))
        except EOFError:
            print("El fichero está vacío.")
        finally:
            fichero.close()
            del fichero

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        self.guardar_jugadores()

    def mostrar_jugador(self):
        for jugador in self.jugadores:
            print(jugador.__str__())

    def guardar_jugadores(self):
        fichero = open("base_datos.pkl", "wb")
        pickle.dump(self.jugadores, fichero)
        fichero.close()
        del fichero

    def mostrar_informacion(self):
        lista={}
        listaordenada=[]
        for jugador in self.jugadores:
            nick=jugador.get_nick()
            puntos=jugador.get_puntos()
            lista[nick]=puntos
        jugadores_sort = sorted(lista.items(), key=operator.itemgetter(1), reverse= True)
        for nick in enumerate(jugadores_sort):
            listaordenada.append(nick[1][0], ':', lista[nick[1][0]])
        return listaordenada
