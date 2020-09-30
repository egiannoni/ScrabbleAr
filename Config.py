import PySimpleGUI as sg

ALPHABET= ['A','B','C','D','E','F','G','H','I','J','K',
              'L','M','N','O','P','Q','R','S','T','U','V',
              'W','X','Y','Z']
LETTER_POOL = { 'A': 11, 'B': 3, 'C': 4, 'D': 4, 'E': 11, 'F': 2, 'G': 2, 'H': 2, 'I': 6, 'J': 2, 'K': 1,
                  'L': 4, 'M': 3, 'N': 5, 'O': 8, 'P': 2, 'Q': 1, 'R': 4, 'S': 7,
                  'T': 4, 'U': 6, 'V': 2, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1 }
LETTER_POINTS = {'A': 1, 'B': 3, 'C': 2, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 6, 'K': 8,
                  'L': 4, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1,
                  'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8, 'Y': 4, 'Z': 10 }
GAME_DURATION_EASY = 900
GAME_DURATION_MEDIUM = 600
GAME_DURATION_HARD = 300

class Settings():

    def __init__(self, level: str, game_duration_choice=0, letter_pool=LETTER_POOL, letter_points=LETTER_POINTS):
        self._game_duration = self.setGameDuration(level, game_duration_choice)
        self._level = level
        self._letter_pool = letter_pool
        self._letter_points = letter_points

    def getGameDuration(self):
        return self._game_duration
    def setGameDuration(self, level: str, game_duration_choice: int):
        if game_duration_choice:
            self._game_duration = game_duration_choice
            return self._game_duration
        elif level == 'easy':
            self._game_duration = GAME_DURATION_EASY
            return self._game_duration
        elif level == 'medium':
            self._game_duration = GAME_DURATION_MEDIUM
            return self._game_duration
        elif level == 'hard':
            self._game_duration = GAME_DURATION_HARD
            return self._game_duration
        
    def getLevel(self):
        return self._level
    def setLevel(self, level: str):
        self._level = level
    
    def getLetterPool(self):
        return self._letter_pool
    def setLetterPool(self, letter_pool: dict):
        self._letter_pool = letter_pool

    def getLetterPoints(self):
        return self._letter_points
    def setLetterPoints(self, letter_points: dict):
        self._letter_points = letter_points

def main(easy_config, medium_config, hard_config):

    sg.theme('LightBrown3')

    layout = [          
        [sg.Text('Configuración Avanzada', key='-T1-', size=(30, 1), justification='center', font=("Helvetica", 25,"bold"),text_color='#d7191c', relief=sg.RELIEF_RIDGE)],         
        [sg.Text(' '  * 80, key='-T2-')],
        [sg.Frame(key='-F-', layout=[          
        [sg.Radio('Facil', 'level_choice', key='-RADIO_EASY-', size=(5,1), enable_events=True), sg.Radio('Medio', 'level_choice', key='-RADIO_MEDIUM-', size=(5,1), enable_events=True), sg.Radio('Dificil', 'level_choice', key='-RADIO_HARD-', size=(5,1), enable_events=True)]], title='Seleccione el nivel que desea configurar', title_color='black', relief=sg.RELIEF_SUNKEN)],
        [sg.Text('Duración del juego en segundos:', key='-T3-'), sg.Slider(range=(60, 3600), key='-GAME_DURATION-', orientation='h', size=(34, 20), default_value=600, enable_events=True)],      
        [sg.Text('Cantidad de letras', key='-T4-', justification='center', size=(15, 1))],      
        [sg.Text('{}-'.format(letra), key='-TT{}-'.format(letra),size=(3, 1), pad=(7,7), justification='center', font=("Helvetica",9), relief=sg.RELIEF_RIDGE) for letra in ALPHABET],
        [sg.Spin(values=[i for i in range(1, 21)], enable_events= True, initial_value=LETTER_POOL[letra], size=(2,2), key='-SPIN1_{}-'.format(letra)) for letra in ALPHABET ],
        [sg.Text('_'  * 80, key='-T5-')],          
        [sg.Text('Valores de letras', justification='center', size=(15, 1), key='-T6-')],      
        [sg.Text('{}-'.format(letra), key='-TTT{}-'.format(letra),size=(3, 1), pad=(7,7), justification='center', font=("Helvetica",9), relief=sg.RELIEF_RIDGE) for letra in ALPHABET],
        [sg.Spin(values=[i for i in range(1, 21)], enable_events= True, initial_value=LETTER_POINTS[letra], size=(2,2), key='-SPIN2_{}-'.format(letra)) for letra in ALPHABET],
        [sg.Text('_'  * 80, key='-T7-')],   
        [sg.Text(' '  * 80, key='-T8-')],         
        [sg.Button('Guardar', key='-SAVE-', button_color=('black','#fdae61')), sg.Button('Cancelar', key='-CANCEL-', button_color=('black','#fdae61'))]
    ]      
    window7 = sg.Window('ScrabbleAr', layout, default_element_size=(40, 1), grab_anywhere=False)

    letter_pool_choice = LETTER_POOL
    letter_points_choice = LETTER_POINTS
    game_duration_choice = 0
    level_customizing = ''
    while True: 
        event, value = window7.read()
        if event == None:
            break
        if event == '-RADIO_EASY-':
            level_customizing = 'easy'
        elif event == '-RADIO_MEDIUM-':
            level_customizing = 'medium'
        elif event == '-RADIO_HARD-':
            level_customizing = 'hard'

        if event == '-GAME_DURATION-':
            game_duration_choice = value['-GAME_DURATION-']

        for event_id in ALPHABET:
            if event == '-SPIN1_{}-'.format(event_id):
                letter_pool_choice[event_id] = value['-SPIN1_{}-'.format(event_id)]

        for event_id in ALPHABET:
            if event == '-SPIN2_{}-'.format(event_id):
                letter_points_choice[event_id] = value['-SPIN2_{}-'.format(event_id)]

        if event == '-CANCEL-':
            window7.close()
            break

        if event  == '-SAVE-':
            if not level_customizing:
                sg.PopupOK(f'Debes elegir un nivel de dificultad para aplicar los cambios.', no_titlebar=True, grab_anywhere=True)
                continue
            elif level_customizing == 'easy':
                easy_config.setLetterPool(letter_pool_choice)
                easy_config.setLetterPoints(letter_points_choice)
                easy_config.setGameDuration(level_customizing, game_duration_choice)
            elif level_customizing == 'medium':
                medium_config.setLetterPool(letter_pool_choice)
                medium_config.setLetterPoints(letter_points_choice)
                medium_config.setGameDuration(level_customizing, game_duration_choice)
            elif level_customizing == 'hard':
                hard_config.setLetterPool(letter_pool_choice)
                hard_config.setLetterPoints(letter_points_choice)
                hard_config.setGameDuration(level_customizing, game_duration_choice)
            window7.close()
            break
        
if __name__ == '__main__':
    main()