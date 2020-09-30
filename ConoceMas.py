import PySimpleGUI as sg

def readme():
    texto = ''
    with open('README.md','r', encoding='utf8') as f:
        texto=f.read()
        f.close()
    return texto


def main():
    var_texto = readme()
    layout = [[sg.Text(var_texto)]]
    windowConoceMas = sg.Window('Conocenos ', layout)
    while True:
        event, value = windowConoceMas.read()
        if event == None:
            break

if __name__ == '__main__':
    main()
