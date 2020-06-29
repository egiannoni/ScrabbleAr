# ##########################################################################################
# El presente código sería mejorable y compactable con clases y métodos que lo factoricen, #
# sin embargo por el momento es un primer prototipo que muestra elementos que al           #
# momento se están considerando para la versión final de la iterfaz de juego, así como la  #
# puntuación de una palabra insertada por el usuario de acuerdo a las pautas               #
# que corresponden a la 1era entrega del trabajo.                                          #
# En cuanto a funcionalidad, la muestra actual pretende contemplar el ingreso de la        # 
# 1era palabra por el usuario y su puntuación.                                             #
# ##########################################################################################
# Fecha de la primera entrega: semana del 16 de junio. En esta entrega se evaluará:
# ● un primer prototipo: donde se visualice el tablero y las demás componentes del
# juego. No es necesario que estén funcionando todos los componentes,
# simplemente para visualizar la interfaz de usuario propuesta;
# ● el ingreso de una palabra al tablero y su puntuación.
# Fecha de la segunda entrega: semana del 13 de julio. En esta entrega se evaluará el
# trabajo completo.
# ----------------------------------------------------------------------------------------
import PySimpleGUI as sg
import random
import time
import pattern.es

BOARD_HEIGHT = 15
BOARD_WIDTH = 15
ARRAY = 7
BUTTON_WIDTH = 2
BUTTON_HEIGHT = 1
BUTTON_PADDING = 1
BUTTON_SIZE = BUTTON_WIDTH, BUTTON_HEIGHT
LETTER_POINTS = {
            'A': 1, 'B': 3, 'C': 2, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 6, 'K': 8,
            'L': 4, 'LL': 8, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'RR': 8, 'S': 1,
            'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8, 'Y': 4, 'Z': 10
        }
LETTERS_POOL = {
            'A': 11, 'B': 3, 'C': 4, 'D': 4, 'E': 11, 'F': 2, 'G': 2, 'H': 2, 'I': 6, 'J': 2, 'K': 1,
            'L': 4, 'LL': 1, 'M': 3, 'N': 5, 'Ñ': 1, 'O': 8, 'P': 2, 'Q': 1, 'R': 4, 'RR': 1, 'S': 7,
            'T': 4, 'U': 6, 'V': 2, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1
        }

def colorize_buttons(button):
    (i, j) = button
    color = 'gray'
    if i == j or i + j == 14:
        color = 'red'
    if i in {0, 7, 14} and j in {0, 7, 14}:
        color = 'yellow'
    s = set((i, j))
    if s == {0, 3} or s == {0,11} or s == {3, 14} or s == {3, 14} or s == {11, 14}:
        color = 'green'
    if s == {2, 6} or s == {2, 8} or s == {3, 7} or s == {6, 12} or s == {7, 11} or s == {8, 12}:
        color = 'green'
    if i in {6, 8} and j in {6, 8}:
        color = 'blue'
    if s == {1, 5} or s == {1, 9} or s == {5, 13} or s == {9, 13}:
        color = 'blue'
    return color

def valid(word):
    return len(word) >= 2 and len(word) <= 7 and word in pattern.es.lexicon.keys() and word in pattern.es.spelling.keys()

def score(word, letter_matrix, letter_matrix_positions_used):
    total = 0
    for letter in word:
        add = 0
        add += LETTER_POINTS[letter.upper()]
        if letter_matrix[letter_matrix_positions_used[0][0]][letter_matrix_positions_used[0][1]][1] == 'yellow':
            add *= 10
        if letter_matrix[letter_matrix_positions_used[0][0]][letter_matrix_positions_used[0][1]][1] == 'green':
            add *= 2
        if letter_matrix[letter_matrix_positions_used[0][0]][letter_matrix_positions_used[0][1]][1] == 'blue':
            add /= 2
        if letter_matrix[letter_matrix_positions_used[0][0]][letter_matrix_positions_used[0][1]][1] == 'red':
            add *= 0
        letter_matrix_positions_used.pop(0)
        total += add
    return total

# ¿Cómo factorizar varias lineas repetidas con una función de una manera simple? Usaría clases...
def update_board():
    pass
def hint():
    pass

def main():
    # Data structures for the interface to be updated with
    all_letters = []
    for k, v in LETTERS_POOL.items():
        for i in range(v):
            all_letters.append(k)
    user_letter_array = []
    ai_letter_array = []
    for i in range(ARRAY):
        # For the user
        letter = random.choice(all_letters).upper()
        user_letter_array.append(letter)
        all_letters.remove(letter)
        # For the AI
        letter = random.choice(all_letters).upper()
        ai_letter_array.append(letter)
        all_letters.remove(letter)

    letter_matrix = [[['', colorize_buttons((i, j))] for i in range(BOARD_HEIGHT)] for j in range(BOARD_WIDTH)]
    user_total_score = 0
    ai_total_score = 0
    # Theme
    sg.theme('Dark Teal 12')
    # Layout
    # AI letter array column layout
    top_column_layout_1 = [
        [sg.Button(key=i + ARRAY, button_text='?', size=BUTTON_SIZE, pad=((BUTTON_PADDING, BUTTON_PADDING), (16, BUTTON_PADDING)), enable_events=True, disabled=True) for i in range(ARRAY)]
    ]
    # Clock column layout
    top_column_layout_2 = [
        [sg.Text('Tiempo de Juego', key='-CLOCK_TEXT-')],
        [sg.Text(key='-CLOCK-', size=(8, 2), font=('Helvetica', 11), justification='center')]
    ]
    # AI letter array and clock layout
    layout = [
        [sg.Column(top_column_layout_1), sg.VerticalSeparator(key='-TOP_V_SEPARATOR-'), sg.Column(top_column_layout_2)],
        [sg.Text('_' * ((BUTTON_WIDTH + BUTTON_PADDING) * BOARD_WIDTH + 4), key='-TOP_H_SEPARATOR-')]
    ]
    # Board layout
    layout += [
        [sg.Button(key=(i, j), button_text='{}'.format(letter_matrix[i][j][0]), button_color=(None, letter_matrix[i][j][1]), size=BUTTON_SIZE, pad=(BUTTON_PADDING, BUTTON_PADDING), enable_events=True) for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)
    ]
    # User letter array column layout
    bottom_column_layout_1 = [
        [sg.Button(key=i, button_text=user_letter_array[i], size=BUTTON_SIZE, pad=((BUTTON_PADDING, BUTTON_PADDING), (16, BUTTON_PADDING)), enable_events=True) for i in range(ARRAY)]
    ]
    # Score and Exit column layout
    bottom_column_layout_2 = [
        [sg.Button('Puntuar', key='-SCORE-', pad=((0, BUTTON_PADDING), (30, BUTTON_PADDING))),
            sg.Exit('Salir', pad=((70, BUTTON_PADDING), (30, BUTTON_PADDING)))]
    ]
    # User and exit layout
    layout += [
        [sg.Text('_' * ((BUTTON_WIDTH + BUTTON_PADDING) * BOARD_WIDTH + 4), key='-BOTTOM_H_SEPARATOR-')],
        [sg.Column(bottom_column_layout_1), sg.VerticalSeparator(key='-BOTTOM_V_SEPARATOR-'), sg.Column(bottom_column_layout_2)]
    ]
    # Window and auxiliary variables
    window = sg.Window('ScrabbleAR', layout, grab_anywhere=True)
    letter_aux = ''
    user_word = ''
    user_word_score = 0
    ai_word_score = 0
    first_pick = True
    moves_horizontally = True
    moves_vertically = True
    # These three variables are for when the user inputs an invalid word, so the state can reverse
    letter_matrix_positions_updated = []
    user_letter_array_positions_updated = []
    letters_in_use = []
    # Time variables
    current_time = 0
    start_time = int(round(time.time() * 100))
    while True:
        event, values = window.read(timeout=10)
        if event in (None, 'Salir'):
            break
        # Updating time
        current_time = int(round(time.time() * 100)) - start_time
        window['-CLOCK-'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100))
        # Interaction with user's set of letters
        if type(event) == int:
            # Grabs the letter from the array
            if user_letter_array[event] != '' and letter_aux == '':
                letter_aux = user_letter_array[event]
                letters_in_use.append(letter_aux)
                user_letter_array[event] = ''
                window[event].Update('')
                user_letter_array_positions_updated.append(event)
            # Puts the letter back in the array 
            elif user_letter_array[event] == '' and letter_aux != '':
                user_letter_array[event] = letter_aux
                letters_in_use.remove(letter_aux)
                letter_aux = ''
                window[event].Update('{}'.format(user_letter_array[event]))
                user_letter_array_positions_updated.remove(event)
        # Interaction with game board
        if type(event) == tuple and letter_matrix[event[0]][event[1]][0] == '' and letter_aux != '':
            # In first pick, the letter placement is free
            if first_pick:
                # Updates board
                letter_matrix[event[0]][event[1]][0] = letter_aux
                window[event].Update('{}'.format(letter_matrix[event[0]][event[1]][0]))
                user_word += letter_aux
                letter_aux = ''
                pos = event[0], event[1]
                letter_matrix_positions_updated.append(event)
                first_pick = False
            # If it's not the first pick, restrains the placements to exclusively rightwards or downwards 
            elif (event[0] - 1 == pos[0] and event[1] == pos[1]) or (event[0] == pos[0] and event[1] - 1 == pos[1]):
                if moves_horizontally and event[0] - 1 == pos[0] and event[1] == pos[1]:
                    moves_vertically = False
                    # Updates board
                    letter_matrix[event[0]][event[1]][0] = letter_aux
                    window[event].Update('{}'.format(letter_matrix[event[0]][event[1]][0]))
                    user_word += letter_aux
                    letter_aux = ''
                    pos = event[0], event[1]
                    letter_matrix_positions_updated.append(event)
                # Gives a hint to where should the letter go (the exception could raise if the movement would be illegal)
                elif moves_horizontally and not moves_vertically:
                    try:
                        window[(pos[0] + 1, pos[1])].Update('{}'.format(letter_aux))
                        window.Refresh()                
                        time.sleep(0.1)
                        window[(pos[0] + 1, pos[1])].Update('')
                    except AttributeError:
                        pass
                elif moves_vertically and event[0] == pos[0] and event[1] - 1 == pos[1]:
                    moves_horizontally = False
                    # Updates board
                    letter_matrix[event[0]][event[1]][0] = letter_aux
                    window[event].Update('{}'.format(letter_matrix[event[0]][event[1]][0]))
                    user_word += letter_aux
                    letter_aux = ''
                    pos = event[0], event[1]
                    letter_matrix_positions_updated.append(event)
                # Gives a hint to where should the letter go (the exception could raise if the movement would be illegal)
                elif moves_vertically and not moves_horizontally:
                    try:
                        window[(pos[0], pos[1] + 1)].Update('{}'.format(letter_aux))
                        window.Refresh()
                        time.sleep(0.1)
                        window[(pos[0], pos[1] + 1)].Update('')
                    except AttributeError:
                        pass
            # Gives a hint to where should the letter go (the exception could raise if the movement would be illegal)
            elif moves_horizontally and not moves_vertically:
                try:
                    window[(pos[0] + 1, pos[1])].Update('{}'.format(letter_aux))
                    window.Refresh()                
                    time.sleep(0.1)
                    window[(pos[0] + 1, pos[1])].Update('')
                except AttributeError:
                    pass
            # Gives a hint to where should the letter go (the exception could raise if the movement would be illegal)
            elif moves_vertically and not moves_horizontally:
                try:
                    window[(pos[0], pos[1] + 1)].Update('{}'.format(letter_aux))
                    window.Refresh()
                    time.sleep(0.1)
                    window[(pos[0], pos[1] + 1)].Update('')
                except AttributeError:
                    pass
        if event == '-SCORE-':
            user_word = user_word.lower()
            if valid(user_word):
                user_word_score = score(user_word, letter_matrix, letter_matrix_positions_updated)
                sg.PopupOK('Tu palabra acumula {} puntos'.format(user_word_score))
            else:
                # Reverses state
                for t in letter_matrix_positions_updated:
                    letter_matrix[t[0]][t[1]][0] = ''
                    window[t].Update('{}'.format(letter_matrix[t[0]][t[1]][0]))
                for i in user_letter_array_positions_updated:
                    user_letter_array[i] = letters_in_use.pop()
                    window[i].Update('{}'.format(user_letter_array[i]))
                sg.PopupOK('Tu palabra era inválida'.format(user_word_score))
            user_word = ''
            user_total_score += user_word_score
            user_word_score = 0

if __name__ == '__main__':
    main()