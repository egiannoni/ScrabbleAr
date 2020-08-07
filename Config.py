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

import PySimpleGUI as sg   


sg.theme('LightBrown3')

     
diccionario= ['A','B','C','D','E','F','G','H','I','J','K',
              'L','M','N','O','P','Q','R','S','T','U','V',
              'W','X','Y','Z']

layout = [          
    [sg.Text('Configuración Avanzada', key='-T1-', size=(30, 1), justification='center', font=("Helvetica", 25,"bold"),text_color='#d7191c', relief=sg.RELIEF_RIDGE)],         
    [sg.Text(' '  * 80, key='-T2-')],
    [sg.Frame(key='-F-', layout=[          
    [sg.Radio('Facil', "nivel", key='-R1-', default=True, size=(5,1)), sg.Radio('Medio', "nivel", key='-R2-',size=(5,1)),sg.Radio('Dificil', "nivel", key='-R3-',size=(5,1))]], title='Seleccione el nivel que desea configurar',title_color='black', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],         
    [sg.Text('Duración del turno en segundos:', key='-T3-'),sg.Slider(range=(1, 100),key='duration', orientation='h', size=(34, 20), default_value=60)],      
    [sg.Text('Cantidad de letras', key='-T4-', justification='center', size=(15, 1))],      
    [sg.Text('{}-'.format(letra), key='-TT{}-'.format(letra),size=(3, 1), justification='center', font=("Helvetica",9), relief=sg.RELIEF_RIDGE)for letra in diccionario],
    [sg.Spin(values=[i for i in range(1, 10)], initial_value=4, size=(2,2),key='-S1_{}-'.format(letra))for letra in diccionario ],     
    [sg.Text('_'  * 80, key='-T5-')],          
    [sg.Text('Valores', justification='center', size=(15, 1), key='-T6-')],      
    [sg.Text('{}-'.format(letra), key='-TTT{}-'.format(letra),size=(3, 1), justification='center', font=("Helvetica",9), relief=sg.RELIEF_RIDGE)for letra in diccionario],
    [sg.Spin(values=[i for i in range(1, 10)], initial_value=3, size=(2,2),key='-S2_{}-'.format(letra))for letra in diccionario ],     
    [sg.Text('_'  * 80, key='-T7-')],   
    [sg.Text(' '  * 80, key='-T8-')],         
    [sg.Button('Guardar', key='-SAVE-',button_color=('black','#fdae61')), sg.Button('Cancelar', key='-CANCEL-', button_color=('black','#fdae61'))]    
]      


window7 = sg.Window('ScrabbleAr', layout, default_element_size=(40, 1), grab_anywhere=False)      

def main():
    while True: 
        event,value = window7.read()    
        if event == '-CANCEL-':
            window7.close()
        if event  == '-SAVE-':
            sg.popup('Error',
                     'Lamentablemente la configuración de niveles no está disponible en esta versión', 
                     'Compruebe en su proxima actualización.')
            window7.close()   
#        if value[0] == True:
#            nivel='Facil'
#        if value[1] == True:
#            nivel='Medio'
#        if value[2] == True:
#            nivel='Dificil'
#        duration=value['duration']
#        for letra in diccionario:
#            LETTERS_POOL={}
#            LETTERS_POOL[letra]= value[letra]
#        
#        for letra in diccionario:
#            LETTER_POINTS={}
#            LETTER_POINTS[letra]= value[letra]
        
if __name__ == '__main__':
    main()

#############################################################################
# class Config():
#     def __init__(self, level):
#         self._game_duration = self.setGameDuration(level)
#         self._level = self.setlevel(level)
#         self._group_of_words = self.setGroupOfWords(level)
#         self._points_per_chip = self.setPointsPerChip()
#         self._string_of_letters = self.setStringOfLetters()
    
#     def getGameDuration(self):
#         return self._game_time
#     # Level easy, medium, hard --> 15, 10, 5 minutes
#     def setGameDuration(self, level):
#         if level == 'easy':
#             self._game_duration = 15 * 60
#         elif level == 'medium':
#             self._game_duration = 10 * 60
#         elif level == 'hard':
#             self._game_duration = 5 * 60
    
#     def getlevel(self):
#         return self._level
#     def setlevel(self, level):
#         self._level = level

#     def getGroupOfWords(self):
#         return self._group_of_words
#     def setGroupOfWords(self, level):
#         if level == 'easy':
#             self._group_of_words = {'all'}
#         elif level == 'medium' or level == 'hard':
#             self._group_of_words = {'adjectives', 'verbs'}

#     def getPointsPerChip(self):
#         return self._points_per_chip
#     def setPointsPerChip(self):
#         points = {
#             'A': 1, 'B': 3, 'C': 2, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 6, 'K': 8,
#             '1': 4, 'LL': 8, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'RR': 8, 'S': 1,
#             'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8, 'Y': 4, 'Z': 10
#         }
#         self._points_per_chip = points

#     def getStringOfLetters(self):
#         return self._string_of_letters
#     def setStringOfLetters(self):
#         quantities = {
#             'A': 11, 'B': 3, 'C': 4, 'D': 4, 'E': 11, 'F': 2, 'G': 2, 'H': 2, 'I': 6, 'J': 2, 'K': 1,
#             'L': 4, 'LL': 1, 'M': 3, 'N': 5, 'Ñ': 1, 'O': 8, 'P': 2, 'Q': 1, 'R': 4, 'RR': 1, 'S': 7,
#             'T': 4, 'U': 6, 'V': 2, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1
#         }
#         string = ''
#         for k, v in quantities.items():
#             for i in range(v):
#                 string += k
#         print(string)
#         self._string_of_letters = string

# SIGUIENTES DOS LÍNEAS SON DE PRUEBA: POR QUÉ RETORNA NONE???
# c = Configuracion('easy')
# print(c.getStringOfLetters())