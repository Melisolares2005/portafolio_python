# modulos 
import os 
from lista_opciones import cargar_opciones
from calculadora import programa_calculadora

# INICIO DEL PROGRAMA
os.system("cls")

cargar_opciones()

# EJECUTO MI PTOGRAMA ESPERANDO UN POSIBLE ERROR
try:  # SI NO HAY ERRORES
    respuesta = input("[?] ")

    if respuesta == "1":
        programa_calculadora()
    
except:  # SI HAY ERROR
    print("valor nulo")