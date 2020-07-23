import pickle

#############  APERTURA DE BASE DE DATOS #############
def AbroBase (nombre_archivo):
    """ Opens the database, if it doesn't exist is creates """

    fichero = open(nombre_archivo, "ab+")
    fichero.seek(0)  # Desplazamos cursor al principio
    try:
        y = pickle.load(fichero)  # Cargamos información
        return y
    except EOFError:
        fichero = open(nombre_archivo, "x") # Para la primera vez que abrimos
        y = pickle.load(fichero)  # Cargamos información
    finally:
        fichero.close()
        del fichero


############# CARGA DE DATOS #############
def CargoBase(nombre_archivo, datos):
    """ Uploads information gamer's to database """

    with open(nombre_archivo, 'ab+') as f:
        pickle.dump(datos, f)
    f.close()
