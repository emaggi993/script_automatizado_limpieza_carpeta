import os
from utils.funciones import  Remover_archivos_antiguos, listar_archivos_antiguos, Enviar_a_papelera_archivos_antiguos


def main(carpeta, dias, enviar_papelera):

    path = carpeta
    print(f"Archivos en el directorio {path}")

    # print(listar_archivos_antiguos(path, dias=dias))
    if enviar_papelera:
        Enviar_a_papelera_archivos_antiguos(path, dias=dias)
    else:
        Remover_archivos_antiguos(path, dias=dias)
        

        

    # print(f"Archivos antiguos en el directorio {path}")


if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) > 1:
        carpeta = sys.argv[1]
        carpeta = os.path.join(os.environ['USERPROFILE'],carpeta)
        if not os.path.isdir(carpeta):
            print(f"La carpeta {sys.argv[1]} no existe")
            exit()
        if len(sys.argv) > 2:
            dias = int(sys.argv[2])
        else:
            r = input("Cuantos dias desea que pasen para que un archivo sea considerado antiguo?: ")
            dias = int(r)

        if len(sys.argv) > 3:
            if sys.argv[3] == "y":
                enviar_papelera = True
            else:
                enviar_papelera = False
        else:
            r = input("Desea enviar a la papelera los archivos antiguos? (y/n): ")
            if r.lower() == "y":
                enviar_papelera = True
            else:
                enviar_papelera = False

    else:
        print("No se especifico la carpeta")
        print("Uso correcto del programa:")
        print("* python app.py <carpeta> <dias>")
        print("* python app.py <carpeta>")

        exit()



    main(carpeta, dias, enviar_papelera)