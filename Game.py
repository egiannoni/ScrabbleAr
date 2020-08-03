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
import Config

BOARD_HEIGHT = 15
BOARD_WIDTH = 15
ARRAY_LENGTH = 7
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
        points = 0
        points += LETTER_POINTS[letter.upper()]
        if letter_matrix[letter_matrix_positions_used[0][0]][letter_matrix_positions_used[0][1]][1] == 'yellow':
            points *= 3
        if letter_matrix[letter_matrix_positions_used[0][0]][letter_matrix_positions_used[0][1]][1] == 'green':
            points *= 2
        if letter_matrix[letter_matrix_positions_used[0][0]][letter_matrix_positions_used[0][1]][1] == 'blue':
            points -= 1
        if letter_matrix[letter_matrix_positions_used[0][0]][letter_matrix_positions_used[0][1]][1] == 'red':
            points -= 3
        letter_matrix_positions_used.pop(0)
        total += points
    return total

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
    # Assign letters
    for i in range(ARRAY_LENGTH):
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
    letter_changes_available = 3
    # Theme
    sg.theme('Dark Teal 12')
    # Layout
    # AI letter array column layout
    top_column_layout_1 = [
        [sg.Button(key=i + ARRAY_LENGTH, button_text='?', size=BUTTON_SIZE, pad=((BUTTON_PADDING, BUTTON_PADDING), (8, BUTTON_PADDING)), enable_events=True, disabled=True) for i in range(ARRAY_LENGTH)]
    ]
    # Clock column layout
    top_column_layout_2 = [
        [sg.Text('Tiempo restante de juego:', key='-CLOCK_TEXT-')],
        [sg.Text(key='-CLOCK-', size=(8, 2), font=('Helvetica', 10), justification='center')]
    ]
    # AI letter array and clock layout
    layout = [
        [sg.Column(top_column_layout_1), sg.VerticalSeparator(), sg.Column(top_column_layout_2)],
        [sg.Text('_' * ((BUTTON_WIDTH + BUTTON_PADDING) * BOARD_WIDTH + 4))]
    ]
    # AI score layout
    layout += [
        [sg.Text('Puntaje del ordenador:', key='-AI_TOTAL_SCORE_TEXT-', size=(16, 1), font=('Helvetica', 10)), 
        sg.Text(key='-AI_TOTAL_SCORE-', size=(8, 1), font=('Helvetica', 11))]
    ]
    # Board layout
    layout += [
        [sg.Button(key=(i, j), button_text='{}'.format(letter_matrix[i][j][0]), button_color=(None, letter_matrix[i][j][1]), size=BUTTON_SIZE, pad=(BUTTON_PADDING, BUTTON_PADDING), enable_events=True) for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)
    ]
    # User score layout
    layout += [
        [sg.Text('Puntaje del usuario:', key='-USER_TOTAL_SCORE_TEXT-', size=(14, 1), font=('Helvetica', 10)), 
        sg.Text(key='-USER_TOTAL_SCORE-', size=(8, 1), font=('Helvetica', 11))]
    ]
    # User letter array column layout
    bottom_column_layout_1 = [
        [sg.Button(key=i, button_text=user_letter_array[i], size=BUTTON_SIZE, pad=((BUTTON_PADDING, BUTTON_PADDING), (8, BUTTON_PADDING)), enable_events=True) for i in range(ARRAY_LENGTH)],
        [sg.Button(f'Cambiar letras ({letter_changes_available})', key='-CHANGE_LETTERS-', pad=((28, BUTTON_PADDING), (8, BUTTON_PADDING)))]
    ]
    # Score and Exit column layout
    bottom_column_layout_2 = [
        [sg.Button('Regresar letras', key='-RETURN_LETTERS-', pad=((28, BUTTON_PADDING), (4, BUTTON_PADDING)))],
        [sg.Button('Puntuar', key='-SCORE-', pad=((0, BUTTON_PADDING), (8, BUTTON_PADDING))),
            sg.Button('Terminar', key='-FINISH-', pad=((50, BUTTON_PADDING), (8, BUTTON_PADDING)))]
    ]
    # User and exit layout
    layout += [
        [sg.Text('_' * ((BUTTON_WIDTH + BUTTON_PADDING) * BOARD_WIDTH + 4))],
        [sg.Column(bottom_column_layout_1), sg.VerticalSeparator(), sg.Column(bottom_column_layout_2)]
    ]
    # Window and auxiliary variables
    window = sg.Window('ScrabbleAR', layout, grab_anywhere=True)
    letter_grabbed = ''
    user_word = ''
    user_word_score = 0
    ai_word_score = 0
    first_letter_placement_ever = True # Si juega la máquina primero, se iniciaría en False
    first_letter_placement = True
    moves_horizontally = True
    moves_vertically = True
    pos = ()
    changing_letters = False
    user_chose_letter_to_change = False
    # These three variables are for when the user inputs an invalid word
    letter_matrix_positions_updated = []
    user_letter_array_positions_updated = []
    letters_in_use = []
    # Time variables
    game_duration = 120 # Se obtiene de la configuracion
    start_time = time.time()
    finish_time = start_time + game_duration
    
    endgame = False
    # Loop
    while True:
        event, values = window.read(timeout=10)
        if event == None:
            break
        if endgame:
            break
        # Updating time
        current_time = time.time()
        remaining_time = finish_time - current_time
        hours, rem = divmod(remaining_time, 3600)
        minutes, seconds = divmod(rem, 60)
        window['-CLOCK-'].Update('{:0>2}:{:0>2}:{:02d}'.format(int(hours),int(minutes),int(seconds)))
        # Checks for endtime
        if remaining_time <= 0:
            endgame = True
        # Checks for exit button
        if event == '-FINISH-':
            endgame = True
        # Updates score in the display
        window['-USER_TOTAL_SCORE-'].Update(user_total_score)
        window['-AI_TOTAL_SCORE-'].Update(ai_total_score)
        # Interaction with user's set of letters
        if type(event) == int and not changing_letters:
            # Grabs the letter from the array
            if user_letter_array[event] != '' and letter_grabbed == '':
                letter_grabbed = user_letter_array[event]
                letters_in_use.append(letter_grabbed)
                user_letter_array[event] = ''
                window[event].Update('')
                user_letter_array_positions_updated.append(event)
            # Puts the letter back in the array 
            elif user_letter_array[event] == '' and letter_grabbed != '':
                user_letter_array[event] = letter_grabbed
                letters_in_use.remove(letter_grabbed)
                letter_grabbed = ''
                window[event].Update('{}'.format(user_letter_array[event]))
                user_letter_array_positions_updated.remove(event)
        # Interaction with game board
        if type(event) == tuple and letter_matrix[event[0]][event[1]][0] == '' and letter_grabbed != '' and not changing_letters:
            # The first ever letter placement goes in the center
            if first_letter_placement_ever:
                pos = (BOARD_HEIGHT // 2, BOARD_WIDTH // 2)
                # Checks whether the first letter is positioned correctly
                if event[0] == pos[0] and event[1] == pos[1]:
                    first_letter_placement_ever = False
                    first_letter_placement = False
                    letter_matrix[event[0]][event[1]][0] = letter_grabbed
                    window[event].Update('{}'.format(letter_matrix[event[0]][event[1]][0]))
                    user_word += letter_grabbed
                    letter_grabbed = ''
                    pos = event[0], event[1]
                    letter_matrix_positions_updated.append(event)
                # Gives a hint to where should the letter go
                else:
                    window[(pos[0], pos[1])].Update('{}'.format(letter_grabbed))
                    window.Refresh()
                    time.sleep(0.1)
                    window[(pos[0], pos[1])].Update('')
            else:
                # The subsequent first letter placement are free
                if first_letter_placement:
                    # Updates board
                    letter_matrix[event[0]][event[1]][0] = letter_grabbed
                    window[event].Update('{}'.format(letter_matrix[event[0]][event[1]][0]))
                    user_word += letter_grabbed
                    letter_grabbed = ''
                    pos = event[0], event[1]
                    letter_matrix_positions_updated.append(event)
                    first_letter_placement = False
                # If it's not the first letter placement, restrains the placements to exclusively rightwards or downwards 
                elif (event[0] - 1 == pos[0] and event[1] == pos[1]) or (event[0] == pos[0] and event[1] - 1 == pos[1]):
                    if moves_horizontally and event[0] - 1 == pos[0] and event[1] == pos[1]:
                        moves_vertically = False
                        # Updates board
                        letter_matrix[event[0]][event[1]][0] = letter_grabbed
                        window[event].Update('{}'.format(letter_matrix[event[0]][event[1]][0]))
                        user_word += letter_grabbed
                        letter_grabbed = ''
                        pos = event[0], event[1]
                        letter_matrix_positions_updated.append(event)
                    # Gives a hint to where should the letter go (the exception could raise if the movement would be illegal)
                    elif moves_horizontally and not moves_vertically:
                        try:
                            window[(pos[0] + 1, pos[1])].Update('{}'.format(letter_grabbed))
                            window.Refresh()                
                            time.sleep(0.1)
                            window[(pos[0] + 1, pos[1])].Update('')
                        except AttributeError:
                            pass
                    elif moves_vertically and event[0] == pos[0] and event[1] - 1 == pos[1]:
                        moves_horizontally = False
                        # Updates board
                        letter_matrix[event[0]][event[1]][0] = letter_grabbed
                        window[event].Update('{}'.format(letter_matrix[event[0]][event[1]][0]))
                        user_word += letter_grabbed
                        letter_grabbed = ''
                        pos = event[0], event[1]
                        letter_matrix_positions_updated.append(event)
                    # Gives a hint to where should the letter go (the exception could raise if the movement would be illegal)
                    elif moves_vertically and not moves_horizontally:
                        try:
                            window[(pos[0], pos[1] + 1)].Update('{}'.format(letter_grabbed))
                            window.Refresh()
                            time.sleep(0.1)
                            window[(pos[0], pos[1] + 1)].Update('')
                        except AttributeError:
                            pass
                # Gives a hint to where should the letter go (the exception could raise if the movement would be illegal)
                elif moves_horizontally and not moves_vertically:
                    try:
                        window[(pos[0] + 1, pos[1])].Update('{}'.format(letter_grabbed))
                        window.Refresh()
                        time.sleep(0.1)
                        window[(pos[0] + 1, pos[1])].Update('')
                    except AttributeError:
                        pass
                # Gives a hint to where should the letter go (the exception could raise if the movement would be illegal)
                elif moves_vertically and not moves_horizontally:
                    try:
                        window[(pos[0], pos[1] + 1)].Update('{}'.format(letter_grabbed))
                        window.Refresh()
                        time.sleep(0.1)
                        window[(pos[0], pos[1] + 1)].Update('')
                    except AttributeError:
                        pass

        # Resetting current word
        if event == '-RETURN_LETTERS-':
            letter_grabbed = ''
            # Reverses current play
            # Clears movement flags
            first_letter_placement = True
            moves_horizontally = True
            moves_vertically = True
            pos = ()
            for t in letter_matrix_positions_updated:
                letter_matrix[t[0]][t[1]][0] = ''
                window[t].Update('{}'.format(letter_matrix[t[0]][t[1]][0]))
            while user_letter_array_positions_updated:
                i = user_letter_array_positions_updated.pop()
                user_letter_array[i] = letters_in_use.pop()
                window[i].Update('{}'.format(user_letter_array[i]))
            # Checks if the first word has been placed
            if user_total_score == 0:
                first_letter_placement_ever = True

        # User starts changing letters
        if event == '-CHANGE_LETTERS-' and not changing_letters:
            changing_letters = True
            window['-CHANGE_LETTERS-'].Update('Selecciónalas')
        # User chooses letters to change
        if type(event) == int and changing_letters:
            user_chose_letter_to_change = True
            window['-CHANGE_LETTERS-'].Update('Hacer el cambio')
            # Grabs the letter from the array
            if user_letter_array[event] != '':
                letter_grabbed = user_letter_array[event]
                letters_in_use.append(letter_grabbed)
                user_letter_array[event] = ''
                window[event].Update('')
                user_letter_array_positions_updated.append(event)
            # Puts the letter back in the array 
            elif user_letter_array[event] == '' and letter_grabbed != '':
                user_letter_array[event] = letter_grabbed
                letters_in_use.remove(letter_grabbed)
                letter_grabbed = ''
                window[event].Update('{}'.format(user_letter_array[event]))
                user_letter_array_positions_updated.remove(event)
        # User finishes changing letters
        if event == '-CHANGE_LETTERS-' and changing_letters and user_chose_letter_to_change:
            letter_changes_available -= 1
            letter_grabbed = ''
            # Resetting the flags
            user_chose_letter_to_change = False
            changing_letters = False
            # Putting back the chosen letters
            quantity_chosen = len(letters_in_use)
            for i in range(quantity_chosen):
                all_letters.append(letters_in_use.pop())
            # Assign new letters
            new_letters = []
            for i in range(quantity_chosen):
                letter = random.choice(all_letters).upper()
                new_letters.append(letter)
                all_letters.remove(letter)
            # Update the user letter array
            for i in user_letter_array_positions_updated:
                user_letter_array[i] = new_letters.pop()
            # Update the display of the user letter array
            while user_letter_array_positions_updated:
                i = user_letter_array_positions_updated.pop()
                window[i].Update('{}'.format(user_letter_array[i]))
            window['-CHANGE_LETTERS-'].Update(f'Cambiar letras ({letter_changes_available})')
            if letter_changes_available == 0:
                window['-CHANGE_LETTERS-'].Update(disabled=True)

        # Score the created word
        if event == '-SCORE-':
            user_word = user_word.lower()
            if valid(user_word):
                user_word_score = score(user_word, letter_matrix, letter_matrix_positions_updated)
                user_total_score += user_word_score
                sg.PopupOK('Tu palabra acumula {} puntos'.format(user_word_score))
                user_word_score = 0
                # Check if there are enough letters in the pool to replace the last used
                if len(user_word) > len(all_letters):
                    endgame = True # Should I add a break statement?
                # Assign more letters for the user
                for i in range(len(user_word)):
                    letter = random.choice(all_letters).upper()
                    user_letter_array[user_letter_array.index('')] = letter
                    all_letters.remove(letter)
                # Updates user letter array display with the new and the remaining letters
                for i in range(len(user_letter_array)):
                    window[i].Update('{}'.format(user_letter_array[i]))
                # Resets variables for next invalid word
                letter_matrix_positions_updated = []
                user_letter_array_positions_updated = []
                letters_in_use = []
            else:
                # Reverses current play
                for t in letter_matrix_positions_updated:
                    letter_matrix[t[0]][t[1]][0] = ''
                    window[t].Update('{}'.format(letter_matrix[t[0]][t[1]][0]))
                while user_letter_array_positions_updated:
                    i = user_letter_array_positions_updated.pop()
                    user_letter_array[i] = letters_in_use.pop()
                    window[i].Update('{}'.format(user_letter_array[i]))
                sg.PopupOK('Tu palabra era inválida')
                # Checks if the first word has been placed
                if user_total_score == 0:
                    first_letter_placement_ever = True
            # Clears movement flags
            first_letter_placement = True
            moves_horizontally = True
            moves_vertically = True
            pos = ()
            user_word = ''

if __name__ == '__main__':
    main()
