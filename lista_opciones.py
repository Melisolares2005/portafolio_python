# Función
def cargar_opciones(lista):
    imprimirLinea()

    for opcion in lista: 

        indice = lista.index(opcion)+1

        if indice%2 == 0:
            print(f"[{indice}]{opcion}")
        else:
            mensaje = f"[{indice}]{opcion} "
            print(mensaje," "*(15-len(mensaje)),end="")


def imprimirLinea():
    print("-"*30)

