
from os import listdir, path
from os.path import isfile, join

def Listar_archivos(path: str)-> list[str]:
    """Retorna una lista con los nombres de los archivos que se encuentran en el directorio especificado.

    Args:
        path (str): Ruta del directorio.

    Returns:
        list[str]: Lista con los nombres de los archivos.
    """
    return [f for f in listdir(path) if isfile(join(path, f))]

def Listar_archivos_completos(path: str)-> list[str]:
    """Retorna una lista con los nombres de los archivos que se encuentran en el directorio especificado.

    Args:
        path (str): Ruta del directorio.

    Returns:
        list[str]: Lista con los nombres de los archivos.
    """
    return [join(path, f) for f in listdir(path) if isfile(join(path, f))]

def Fecha_creacion_archivo(file: str)-> str:
    import time
    """Retorna la fecha de creacion del archivo.

    Args:
        file (str): Ruta del archivo.

    Returns:
        str: Fecha de creacion del archivo.
    """
    return time.ctime(path.getctime(file))

def Fecha_modificacion_archivo(file: str)-> str:
    import time
    """Retorna la fecha de modificacion del archivo.

    Args:
        file (str): Ruta del archivo.

    Returns:
        str: Fecha de modificacion del archivo.
    """
    return time.ctime(path.getmtime(file))

def listar_archivos_antiguos(url, dias=1):
    import time
    import os
    """Retorna una lista con los nombres de los archivos que se encuentran en el directorio especificado.

    Args:
        url (str): Ruta del directorio.

    Returns:
        list[str]: Lista con los nombres de los archivos.
    """

    return [join(url, f) for f in listdir(url) if isfile(join(url, f)) and (time.time() - os.path.getmtime(join(url, f))) / 86400 > dias]

def Remover_archivo(file: str)-> None:
    """Remueve el archivo especificado.

    Args:
        file (str): Ruta del archivo.
    """
    import os
    os.remove(file)

def Remover_archivos(files: list[str])-> None:
    import os
    """Remueve los archivos especificados.

    Args:
        files (list[str]): Lista con las rutas de los archivos.
    """
    for file in files:
        if os.path.isfile(file):
            print(f"Archivo {file} removido. ultima modificacion: {Fecha_modificacion_archivo(file)}")
            Remover_archivo(file)

def Remover_archivos_antiguos(url, dias=1):
    import time
    import os
    """Remueve los archivos especificados.

    Args:
        files (list[str]): Lista con las rutas de los archivos.
    """
    for file in listar_archivos_antiguos(url, dias):
        if os.path.isfile(file):
            print(f"Archivo {file} removido. ultima modificacion: {Fecha_modificacion_archivo(file)}")
            Remover_archivo(file)

def Enviar_a_papelera(file: str)-> None:
    import send2trash
    """Envia el archivo especificado a la papelera de reciclaje.

    Args:
        file (str): Ruta del archivo.
    """
    send2trash.send2trash(file)

def Enviar_a_papelera_archivos(files: list[str])-> None:
    import send2trash
    import os
    """Envia los archivos especificados a la papelera de reciclaje.

    Args:
        files (list[str]): Lista con las rutas de los archivos.
    """
    for file in files:
        if os.path.isfile(file):
            print(f"Archivo {file} enviado a la papelera de reciclaje. ultima modificacion: {Fecha_modificacion_archivo(file)}")
            Enviar_a_papelera(file)

def Enviar_a_papelera_archivos_antiguos(url, dias=1):
    import time
    import os
    import send2trash
    """Envia los archivos especificados a la papelera de reciclaje.

    Args:
        files (list[str]): Lista con las rutas de los archivos.
    """
    for file in listar_archivos_antiguos(url, dias):
        if os.path.isfile(file):
            print(f"Archivo {file} enviado a la papelera de reciclaje. ultima modificacion: {Fecha_modificacion_archivo(file)}")
            Enviar_a_papelera(file)
