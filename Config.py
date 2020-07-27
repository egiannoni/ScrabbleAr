# ScrabbleAR: configuración del juego
# ScrabbleAR tendrá un módulo de configuración en donde se podrán especificar algunos
# parámetros del juego:
# ● Tiempo de juego: se configurará un máximo de tiempo para una partida de acuerdo a
# cada level.
# ● level: se propondrá tres leveles de dificultad: easy, medium y hard. Esto podrá condicionar
# el tiempo y el conjunto de palabras disponibles. En el level easy, se pueden jugar con
# cualquier tipo de palabra (adjectives, sustantivos y verbs); en el level medium, se juega
# sólo con verbs y sustantivos y en el level hard con una categoría al azar. En esta
# opción, se configurará el level del juego.
# ● El puntaje de cada ficha. Por ejemplo, se podría configurar de la siguiente manera:
# ○ 1 punto: A, E, O, S, I, U, N, L, R, T
# ○ 2 puntos: C, D, G
# ○ 3 puntos: M, B, P
# ○ 4 puntos: F, H, V, Y
# ○ 6 puntos: J
# ○ 8 puntos: K, LL, Ñ, Q, RR, W, X
# ○ 10 puntos: Z
# ● La cantidad total de fichas por letra. Por ejemplo se podría configurar de la siguiente
# manera y esta configuración será la misma para todos los leveles:
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
# en el level easy se podrá formar cualquier palabra que Pattern considere válida, sin tener en 
# cuenta una clasificación específica.
# en el level medium y hard, sólo se podrán agregar adjectives o verbs. Se saca las palabras 
# sustantivos como posibilidad.
# Saludos

# Sofía
# ------------------------------------------------------------------------------------------------
class Config():
    def __init__(self, level):
        self._game_duration = self.setGameDuration(level)
        self._level = self.setlevel(level)
        self._group_of_words = self.setGroupOfWords(level)
        self._points_per_chip = self.setPointsPerChip()
        self._string_of_letters = self.setStringOfLetters()
    
    def getGameDuration(self):
        return self._game_time
    # Level easy, medium, hard --> 15, 10, 5 minutes
    def setGameDuration(self, level):
        if level == 'easy':
            self._game_duration = 15 * 60
        elif level == 'medium':
            self._game_duration = 10 * 60
        elif level == 'hard':
            self._game_duration = 5 * 60
    
    def getlevel(self):
        return self._level
    def setlevel(self, level):
        self._level = level

    def getGroupOfWords(self):
        return self._group_of_words
    def setGroupOfWords(self, level):
        if level == 'easy':
            self._group_of_words = {'all'}
        elif level == 'medium' or level == 'hard':
            self._group_of_words = {'adjectives', 'verbs'}

    def getPointsPerChip(self):
        return self._points_per_chip
    def setPointsPerChip(self):
        points = {
            'A': 1, 'B': 3, 'C': 2, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 6, 'K': 8,
            '1': 4, 'LL': 8, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'RR': 8, 'S': 1,
            'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8, 'Y': 4, 'Z': 10
        }
        self._points_per_chip = points

    def getStringOfLetters(self):
        return self._string_of_letters
    def setStringOfLetters(self):
        quantities = {
            'A': 11, 'B': 3, 'C': 4, 'D': 4, 'E': 11, 'F': 2, 'G': 2, 'H': 2, 'I': 6, 'J': 2, 'K': 1,
            'L': 4, 'LL': 1, 'M': 3, 'N': 5, 'Ñ': 1, 'O': 8, 'P': 2, 'Q': 1, 'R': 4, 'RR': 1, 'S': 7,
            'T': 4, 'U': 6, 'V': 2, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1
        }
        string = ''
        for k, v in quantities.items():
            for i in range(v):
                string += k
        print(string)
        self._string_of_letters = string

# SIGUIENTES DOS LÍNEAS SON DE PRUEBA: POR QUÉ RETORNA NONE???
# c = Configuracion('easy')
# print(c.getStringOfLetters())