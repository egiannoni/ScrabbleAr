import PySimpleGUI as sg
import random
import time
import pattern.es
import Config
from itertools import permutations

BOARD_WIDTH = 15
BOARD_HEIGHT = 15
ARRAY_LENGTH = 7
BUTTON_WIDTH = 2
BUTTON_HEIGHT = 1
BUTTON_PADDING = 1
BUTTON_SIZE = BUTTON_WIDTH, BUTTON_HEIGHT
LETTER_POINTS = {
            'A': 1, 'B': 3, 'C': 2, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 6, 'K': 8,
            'L': 4, 'M': 3, 'N': 1, 'Ñ': 8, 'O': 1, 'P': 3, 'Q': 8, 'R': 1, 'S': 1,
            'T': 1, 'U': 1, 'V': 4, 'W': 8, 'X': 8, 'Y': 4, 'Z': 10
        }
LETTERS_POOL = {
            'A': 11, 'B': 3, 'C': 4, 'D': 4, 'E': 11, 'F': 2, 'G': 2, 'H': 2, 'I': 6, 'J': 2, 'K': 1,
            'L': 4, 'M': 3, 'N': 5, 'Ñ': 1, 'O': 8, 'P': 2, 'Q': 1, 'R': 4, 'S': 7,
            'T': 4, 'U': 6, 'V': 2, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1
        }

def colorize_buttons(button):
    '''Colorizes buttons''' # Niveles de dificultad diferentes tendrían distinta distribución y densidad de los colores para multiplicar (Config.py)
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
    '''Returns True if param is in pattern.es and lexicon.es, disregarding case''' # Diferentes niveles aceptarían distinta validación (Config.py)
    word = word.lower()
    return len(word) >= 2 and len(word) <= 7 and word in pattern.es.lexicon.keys() and word in pattern.es.spelling.keys()

def score(word, letter_matrix, letter_matrix_positions_used):
    '''Returns score for a given word'''
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
    
    # Association between letter positions and colors for scoring in a matrix
    letter_matrix = [[['', colorize_buttons((i, j))] for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]

    # Positions for the AI to choose from
    board_positions = [(i, j) for i in range(BOARD_WIDTH) for j in range(BOARD_HEIGHT)]

    # Random initial turn
    user_turn = random.choice([True, False])

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
        [sg.Column(top_column_layout_1), sg.VerticalSeparator(key='-TOP_V_SEPARATOR-'), sg.Column(top_column_layout_2)],
        [sg.Text('_' * ((BUTTON_WIDTH + BUTTON_PADDING) * BOARD_WIDTH + 4), key='-TOP_H_SEPARATOR-')]
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
        [sg.Text('_' * ((BUTTON_WIDTH + BUTTON_PADDING) * BOARD_WIDTH + 4), key='-BOTTOM_H_SEPARATOR-')],
        [sg.Column(bottom_column_layout_1), sg.VerticalSeparator(key='-BOTTOM_V_SEPARATOR-'), sg.Column(bottom_column_layout_2)]
    ]
    # Window and auxiliary variables
    window = sg.Window('ScrabbleAR', layout, grab_anywhere=True, no_titlebar=True)
    letter_grabbed = ''
    user_word = ''
    user_word_score = 0
    ai_word_score = 0
    first_letter_placement_ever = True
    first_letter_placement = True
    moves_horizontally = True
    moves_vertically = True
    pos = ()
    changing_letters = False
    user_chose_letter_to_change = False
    # These three variables are for keeping track of letters and positions in play
    letter_matrix_positions_updated = []
    user_letter_array_positions_updated = []
    letters_in_use = []
    # Time variables
    game_duration = 600 # Se obtiene de la configuracion, de acuerdo al nivel elegido (Config.py)
    start_time = time.time()
    finish_time = start_time + game_duration
    
    endgame = False
    # Loop
    while True:
        event, values = window.read(timeout=10)
        if event == None:
            break
        if endgame:
            sg.PopupOK(f'Juego finalizado. Tus puntos: {user_total_score}. Puntos del ordenador: {ai_total_score}', no_titlebar=True, grab_anywhere=True)
            break
        # Updating time
        current_time = time.time()
        remaining_time = finish_time - current_time
        hours, rem = divmod(remaining_time, 3600)
        minutes, seconds = divmod(rem, 60)
        window['-CLOCK-'].Update('{:0>2}:{:0>2}:{:02d}'.format(int(hours),int(minutes),int(seconds)))
        # Checks for endtime
        if remaining_time <= 0:
            sg.PopupOK('Se acabó el tiempo', no_titlebar=True, grab_anywhere=True)
            endgame = True
        # Checks for exit button
        if event == '-FINISH-':
            endgame = True
        # Updates score in the display
        window['-USER_TOTAL_SCORE-'].Update(user_total_score)
        window['-AI_TOTAL_SCORE-'].Update(ai_total_score)
        
        # AI play
        if not user_turn:
            # Lists valid words
            ai_word = ''
            ai_words = []
            for i in range(len(ai_letter_array)):
                ai_words += [ai_word.join(ai_letter) for ai_letter in permutations(ai_letter_array, i + 1)]
            ai_unique_words = set(ai_words)
            ai_valid_words = [word for word in filter(valid, ai_unique_words)]
            # Tries to make a word
            try:
                # Chooses a valid word
                # Sorts them by length
                ai_valid_words.sort(key=lambda x: len(x))
                # Picks the longest
                ai_word_choice = ai_valid_words.pop() # En dificultad fácil elegiría la más corta (pop(index=0)), en media la del medio (Config.py)
                # Finds place to put the word
                positions_needed = len(ai_word_choice)
                while positions_needed:
                    if first_letter_placement_ever:
                        first_letter_placement_ever = False
                        first_letter_placement = False
                        # First letter ever to the center of the board
                        pos = (BOARD_WIDTH // 2, BOARD_HEIGHT // 2)
                        direction = random.choice(['downwards', 'rightwards'])
                        positions_needed -= 1
                        letter_matrix_positions_updated.append(pos)
                    elif first_letter_placement:
                        first_letter_placement = False
                        # First letter of a word is random
                        pos = random.choice(board_positions)
                        direction = random.choice(['downwards', 'rightwards'])
                        positions_needed -= 1
                        letter_matrix_positions_updated.append(pos)
                    else:
                        if direction == 'downwards':
                            for i in range(positions_needed):
                                pos = list(pos)
                                pos[1] += 1
                                pos = tuple(pos)
                                letter_matrix_positions_updated.append(pos)
                                positions_needed -= 1
                        else:
                            # direction is rightwards
                            for i in range(positions_needed):
                                pos = list(pos)
                                pos[0] += 1
                                pos = tuple(pos)
                                letter_matrix_positions_updated.append(pos)
                                positions_needed -= 1
                    if positions_needed == 0:
                        # Checks if it's all available spots
                        for p in letter_matrix_positions_updated:
                            if p[0] >= BOARD_WIDTH or p[1] >= BOARD_HEIGHT or letter_matrix[p[0]][p[1]][0] != '':
                                # Preparing for the next search
                                positions_needed = len(ai_word_choice)
                                first_letter_placement = True
                                letter_matrix_positions_updated = []
                                break
                # Places the letters in the board
                for i in range(len(ai_word_choice)):
                    # Grabs a letter
                    ai_letter = ai_word_choice[i]
                    # Erases it from the ai letter array
                    ai_letter_array[ai_letter_array.index(ai_letter)] = ''
                    # Gets the corresponding position
                    pos = letter_matrix_positions_updated[i]
                    # Updates association matrix
                    letter_matrix[pos[0]][pos[1]][0] = ai_letter
                    # Reflects it on the display
                    window[pos].Update('{}'.format(letter_matrix[pos[0]][pos[1]][0]))
                # Scores the AI word
                ai_word_score = score(ai_word_choice, letter_matrix, letter_matrix_positions_updated)
                ai_total_score += ai_word_score
                # Checks for endgame if there aren't enough letters in the pool to replace the last used
                if len(ai_word_choice) > len(all_letters):
                    sg.PopupOK('No hay más letras en la bolsa', no_titlebar=True, grab_anywhere=True)
                    endgame = True
                else:
                    # Assign more letters for the ai
                    for i in range(len(ai_word_choice)):
                        letter = random.choice(all_letters).upper()
                        ai_letter_array[ai_letter_array.index('')] = letter
                        all_letters.remove(letter)
                    # The turn goes back to the user
                    user_turn = not user_turn
                    # Resets for the user
                    first_letter_placement = True
                    letter_matrix_positions_updated = []
            # Handles .pop() at line 208 if no valid words were found
            except IndexError:
                sg.PopupOK('El ordenador no ha encontrado palabra', no_titlebar=True, grab_anywhere=True)
                endgame = True

        # Interaction with user's set of letters
        if type(event) == int and not changing_letters and user_turn:
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
        if type(event) == tuple and letter_matrix[event[0]][event[1]][0] == '' and letter_grabbed != '' and not changing_letters and user_turn:
            # The first ever letter placement goes in the center
            if first_letter_placement_ever:
                pos = (BOARD_WIDTH // 2, BOARD_HEIGHT // 2)
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
        if event == '-RETURN_LETTERS-' and user_turn:
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
            if user_total_score == 0 and ai_total_score == 0:
                first_letter_placement_ever = True

        # User starts changing letters
        if event == '-CHANGE_LETTERS-' and not changing_letters and user_turn:
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
            # When the user changes their letters, their turn finishes
            user_turn = not user_turn

        # Score the created word
        if event == '-SCORE-' and user_turn:
            if valid(user_word):
                user_word_score = score(user_word, letter_matrix, letter_matrix_positions_updated)
                user_total_score += user_word_score
                user_word_score = 0
                # Check if there are enough letters in the pool to replace the last used
                if len(user_word) > len(all_letters):
                    sg.PopupOK('No hay más letras en la bolsa', no_titlebar=True, grab_anywhere=True)
                    endgame = True
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
                # When the user scores a valid word, their turn finishes
                user_turn = not user_turn
            else:
                # Reverses current play
                for t in letter_matrix_positions_updated:
                    letter_matrix[t[0]][t[1]][0] = ''
                    window[t].Update('{}'.format(letter_matrix[t[0]][t[1]][0]))
                while user_letter_array_positions_updated:
                    i = user_letter_array_positions_updated.pop()
                    user_letter_array[i] = letters_in_use.pop()
                    window[i].Update('{}'.format(user_letter_array[i]))
                sg.PopupOK('Tu palabra era inválida', no_titlebar=True, grab_anywhere=True)
                # Checks if the first word has been placed
                if user_total_score == 0 and ai_total_score == 0:
                    first_letter_placement_ever = True
            # Clears movement flags
            first_letter_placement = True
            moves_horizontally = True
            moves_vertically = True
            pos = ()
            user_word = ''

if __name__ == '__main__':
    main()