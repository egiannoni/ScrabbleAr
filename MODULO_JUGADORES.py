import pickle
############ GENERACION DE JUGADORES #############
class Jugador():
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

    def __str__(self):
        return " + {} {} usa el nick {} y tiene {} puntos.".format(self._nombre, self._apellido, self._nick, self._puntaje)


class ListaJugadores():
    jugadores = []

    def __init__(self):
        fichero = open("prueba.pkl", "ab+")
        fichero.seek(0)  # Desplazamos cursor al principio

        try:
            self.jugadores = pickle.load(fichero)  # Cargamos información
            print("Se cargaron {} personas.".format(len(self.jugadores)))
        except EOFError:
            print("El fichero está vacío.")  # Para la primera vez que abrimos
        finally:
            fichero.close()
            del fichero
            return self.jugadores

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)
        self.guardar_jugadores()

    def mostrar_jugador(self):
        for jugador in self.jugadores:
            print(jugador.__str__())

    def guardar_jugadores(self):
        fichero = open("prueba.pkl", "wb")
        pickle.dump(self.jugadores, fichero)
        fichero.close()
        del fichero

    def mostrar_informacion(self):
        lista=[]
        for jugador in self.jugadores:
            lista.append(jugador.__str__())
        return lista

    # Esta funcion tdv no anda #
    def ranking(self):
        lista=[]
        for clave,valor in  self.jugadores.items():
            lista.append("{} tiene {} puntos".format(clave,valor))
        return lista
