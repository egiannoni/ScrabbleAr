import pickle

#############  APERTURA DE BASE DE DATOS #############
def AbroBase(nombre_archivo):
    try:
        with open(nombre_archivo , 'rb') as f:
            y = pickle.load(f)
    except 'EOFError':
        with open(nombre_archivo , 'xb') as f:
            y = pickle.load(f)

    return y

############# CARGA DE DATOS #############
def CargoBase(nombre_archivo, datos):
    with open(nombre_archivo, 'ab+') as f:
        pickle.dump(datos, f)
    f.close()


#    except 'FileNotFoundError':
#        print('se levanto la excepcion')
#        with open(nombre_archivo, 'x') as f:
#           y= pickle.load(f, encoding="ASCII", errors="strict", buffers=None)
