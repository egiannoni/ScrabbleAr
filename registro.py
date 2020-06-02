import PySimpleGUI as sg 

#Armando una columna
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

class Jugador: 
    
    def __init__(self, pas, nombre,apellido,nacionalidad,correo):
        
        self.pas = pas
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.correo = correo
        
    def jugar(self):
           print ("se llama {} {},tiene la contraseña {}".format( self.nombre, self.apellido, self.pas))
           

def main():   
    window = sg.Window('Registro de ScrabbleAR').Layout(dise) 
    event, values = window.read()
    i = True
    while i == True:
        if event == 'Ok' :
            if values['correo'] is not base_datos:
                if values['nick'] is not base_datos:
                    values['nick'] = Jugador(values['pas'],values['nombre'],values['apellido'],values['nacionalidad'],values['correo'])
                    values['nick'].jugar()
                    window.close()
                else: 
                    sg.SystemTray.notify('Error', 'el nick ingresado ya existe')
                
            else:
               sg.SystemTray.notify('Error', 'el correo ingresado ya existe')  
        else:
            i == False        
            window.close()
    values['nick'].jugar()


if __name__ == '__main__':
    main()