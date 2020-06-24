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
        super().__init__()
        self._tiempo_de_juego = setTiempoDeJuego(nivel)
        self._nivel = setNivel(nivel)
        self._conjunto_de_palabras = setConjuntoDePalabras(nivel)
        self._puntaje_de_cada_ficha = setPuntajeDeCadaFicha()
        self._cantidad_de_fichas_por_letra = setCantidadDeFichasPorLetra()
    
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
            1: ['A', 'E', 'O', 'S', 'I', 'U', 'N', 'L', 'R', 'T'],
            2: ['C', 'D', 'G'],
            3: ['M', 'B', 'P'],
            4: ['F', 'H', 'V', 'Y'],
            6: ['J'],
            8: ['K', 'LL', 'Ñ', 'Q', 'RR', 'W', 'X'],
            10: ['Z']
        }
        self._puntaje_de_cada_ficha = puntajes

    def getCantidadDeFichasPorLetra(self):
        return self._cantidad_de_fichas_por_letra
    def setCantidadDeFichasPorLetra(self):
        cantidades = {
            1: ['Y', 'K', 'LL', 'Ñ', 'Q', 'RR', 'W', 'X', 'Z'],
            2: ['G', 'P', 'F', 'H', 'V', 'J'],
            3: ['M', 'B'],
            4: ['R', 'L', 'T', 'C', 'D'],
            5: ['N'],
            6: ['I', 'U'],
            7: ['S'],
            8: ['O'],
            11: ['A', 'E']
        }
        self._cantidad_de_fichas_por_letra = cantidades
