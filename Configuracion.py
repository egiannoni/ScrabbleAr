# ScrabbleAR: configuración del juego
# ScrabbleAR tendrá un módulo de configuración en donde se podrán especificar algunos
# parámetros del juego:
# ● Tiempo de juego: se configurará un máximo de tiempo para una partida de acuerdo a
# cada nivel.
# ● Nivel: se propondrá tres niveles de dificultad: fácil, medio y difícil. Esto podrá condicionar
# el tiempo y el conjunto de palabras disponibles. En el nivel fácil, se pueden jugar con
# cualquier tipo de palabra (adjetivos, sustantivos y verbos); en el nivel medio, se juega
# sólo con verbos y sustantivos y en el nivel difícil con una categoría al azar. En esta
# opción, se configurará el nivel del juego.
# ● El puntaje de cada ficha. Por ejemplo, se podría configurar de la siguiente manera:
# ○ 1 punto: A, E, O, S, I, U, N, L, R, T
# ○ 2 puntos: C, D, G
# ○ 3 puntos: M, B, P
# ○ 4 puntos: F, H, V, Y
# ○ 6 puntos: J
# ○ 8 puntos: K, LL, Ñ, Q, RR, W, X
# ○ 10 puntos: Z
# ● La cantidad total de fichas por letra. Por ejemplo se podría configurar de la siguiente
# manera y esta configuración será la misma para todos los niveles:
# ○ A ×11, E ×11, O ×8, S ×7, I ×6, U ×6, N ×5, L ×4, R ×4, T ×4
# ○ C ×4, D ×4, G ×2
# ○ M ×3, B ×3, P ×2
# ○ F ×2, H ×2, V ×2, Y ×1
# ○ J ×2
# ○ K ×1, LL ×1, Ñ ×1, Q ×1, RR ×1, W ×1, X ×1
# ○ Z ×1
# -----------------------------------------------------------------------------------------------
# Hola, en función de algunos inconvenientes con la librería Pattern les hacemos llegar algunas 
# modificaciones que hicimos sobre las consignas del trabajo:
# no tomar en cuenta las palabras con acentos, es decir, no se podrán  formar palabras que tengan 
# tildes.
# en el nivel fácil se podrá formar cualquier palabra que Pattern considere válida, sin tener en 
# cuenta una clasificación específica.
# en el nivel medio y difícil, sólo se podrán agregar adjetivos o verbos. Se saca las palabras 
# sustantivos como posibilidad.
# Saludos

# Sofía
# ------------------------------------------------------------------------------------------------
class Configuracion():
    def __init__(self, nivel):
        # ¿Hay una superclase implícita en Python como en Java?
        # super().__init__()
        self._tiempo_de_juego = self.setTiempoDeJuego(nivel)
        self._nivel = self.setNivel(nivel)
        self._conjunto_de_palabras = self.setConjuntoDePalabras(nivel)
        self._puntaje_de_cada_ficha = self.setPuntajeDeCadaFicha()
        self._cadena_de_letras = self.setCadenaDeLetras()
    
    def getTiempoDeJuego(self):
        return self._tiempo_de_juego
    # nivel fácil, medio, difícil --> 15, 10, 5 minutos
    def setTiempoDeJuego(self, nivel):
        if nivel == 'fácil':
            self._tiempo_de_juego = 15 * 60
        elif nivel == 'medio':
            self._tiempo_de_juego = 10 * 60
        elif nivel == 'difícil':
            self._tiempo_de_juego = 5 * 60
    
    def getNivel(self):
        return self._nivel
    def setNivel(self, nivel):
        self._nivel = nivel

    def getConjuntoDePalabras(self):
        return self._conjunto_de_palabras
    def setConjuntoDePalabras(self, nivel):
        if nivel == 'fácil':
            self._conjunto_de_palabras = {'todas'}
        elif nivel == 'medio' or nivel == 'difícil':
            self._conjunto_de_palabras = {'adjetivos', 'verbos'}

    def getPuntajeDeCadaFicha(self):
        return self._puntaje_de_cada_ficha
    def setPuntajeDeCadaFicha(self):
        puntajes = {
            'A': 1, 'B': 3, 'C': 2, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 6, 'K': 8,
            'L': 4, 'LL': 8, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'RR': 8, 'S': 1,
            'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8, 'Y': 4, 'Z': 10
        }
        self._puntaje_de_cada_ficha = puntajes

    def getCadenaDeLetras(self):
        return self._cadena_de_letras
    def setCadenaDeLetras(self):
        cantidades = {
            'A': 11, 'B': 3, 'C': 4, 'D': 4, 'E': 11, 'F': 2, 'G': 2, 'H': 2, 'I': 6, 'J': 2, 'K': 1,
            'L': 4, 'LL': 1, 'M': 3, 'N': 5, 'Ñ': 1, 'O': 8, 'P': 2, 'Q': 1, 'R': 4, 'RR': 1, 'S': 7,
            'T': 4, 'U': 6, 'V': 2, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1
        }
        cadena = ''
        for k, v in cantidades.items():
            for i in range(v):
                cadena += k
        print(cadena)
        self._cadena_de_letras = cadena

# SIGUIENTES DOS LÍNEAS SON DE PRUEBA: POR QUÉ RETORNA NONE???
c = Configuracion('fácil')
print(c.getCadenaDeLetras())
