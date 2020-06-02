import PySimpleGUI as sg  
  
def main():
    diseño= [[sg.Text('''Aca va la pantalla principal''')],
             [sg.Text('Seleccione el nivel:')],
             [sg.Radio('Facil', "nivel", default=True),sg.Radio('medio', "nivel"),sg.Radio('dicifil', "nivel")]]
    window = sg.Window(' ').layout(diseño)
    window.read()


if __name__ == '__main__':
    main()


