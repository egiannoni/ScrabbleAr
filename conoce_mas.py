import PySimpleGUI as sg  

def readme():
    f=open('README.md','r')
    texto=f.read()
    f.close()
    return texto


def main():
    var_texto=readme()
    diseño= [[sg.Text(var_texto)]]
    window = sg.Window('Conocenos  ').layout(diseño)
    window.read()


if __name__ == '__main__':
    main()


