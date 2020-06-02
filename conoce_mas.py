import PySimpleGUI as sg  
  
def main():
    diseño= [[sg.Text('''Somos un grupo de alumnes
    que está desarrollando
    un juego mientras aprendemos y nos divertimos
    ojala te guste a vos tambien''')]]
    window = sg.Window('Conocenos  ').layout(diseño)
    window.read()


if __name__ == '__main__':
    main()


