import pickle

#############  APERTURA DE BASE DE DATOS #############
def AbroBase (nombre_archivo):
    # Lectura en modo binario
    fichero = open(nombre_archivo, "ab+")
    fichero.seek(0)  # Desplazamos cursor al principio
    try:
        y = pickle.load(fichero)  # Cargamos información
        return y
    except EOFError:
        print("El fichero está vacío.")  # Para la primera vez que abrimos
    finally:
        fichero.close()
        del fichero


############# CARGA DE DATOS #############
def CargoBase(nombre_archivo, datos):
    with open(nombre_archivo, 'ab+') as f:
        pickle.dump(datos, f)
    f.close()
