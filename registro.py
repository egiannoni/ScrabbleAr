import PySimpleGUI as sg 
import json

############# ARMADO DE LA COLUMNA DE LA INTERFAZ #############
columna_1 =  [  [sg.Text('Nombre')],
                [sg.Text('Apellido')],
                [sg.Text('Nacionalidad')],
		            [sg.Text('Correo')] ]

columna_2 = [   [sg.InputText(key='nombre',size=(30, 1))],
                [sg.InputText(key='apellido',size=(30, 1))],
                [sg.InputText(key='nacionalidad',size=(30, 1))],
		    [sg.InputText(key='correo',size=(30, 1))]  ]

columna_3 =  [  [sg.Text('Nick Name')],
                [sg.Text('Pass')] ]

columna_4 = [   [sg.InputText(key='nick',size=(30, 1))],
                [sg.InputText(key='pas',size=(30, 1))]  ]

#Armo el diseño de la interface
dise = [      [sg.Text('Datos Personales')],
                [sg.Column(columna_1), sg.Column(columna_2)],
                [sg.Text('Datos de Juego ')],
                [sg.Column(columna_3), sg.Column(columna_4)],
                [ sg.Ok(), sg.Cancel()] ] 

############# GENERACION DE JUGADORES #############
class jugador: 
    
    def __init__(self, pas, nombre,apellido,nacionalidad,correo):
        
        self._pas = pas
        self._nombre = nombre
        self._apellido = apellido
        self._nacionalidad = nacionalidad
        self._correo = correo

#############  APERTURA DE BASE DE DATOS #############        
def abro_base():
    f=open('base_datos','a+')
    y=json.loads(f)
    return y

############# CARGA DE DATOS #############
def agrego_a_base(x,y):
    y=json.loads(str(x))
    y.close()
    
      
############# PRINCIPAL #############
def main():   
    window = sg.Window('Registro de ScrabbleAR').Layout(dise) 
    event, values = window.read()
    i = True
    while i == True:
        base=abro_base()
        if event == 'Ok' :
            if values['correo'] is not base:
                if values['nick'] is not base:
                    jug=values['nick']
                    jug= jugador(values['pas'],values['nombre'],values['apellido'],values['nacionalidad'],values['correo'])
                    agrego_a_base(jug)
                    window.close()
                else: 
                    sg.SystemTray.notify('Error', 'el nick ingresado ya existe')
                
            else:
               sg.SystemTray.notify('Error', 'el correo ingresado ya existe')  
        else:
            i == False        
            window.close()


if __name__ == '__main__':
    main()