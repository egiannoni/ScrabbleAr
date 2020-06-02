import PySimpleGUI as sg  
  
def main():
    diseño= [[sg.Text('''Aca va el ranking''')]]
    window = sg.Window('Ranking').layout(diseño)
    window.read()


if __name__ == '__main__':
    main()


