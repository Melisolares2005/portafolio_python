#@sumar: función que requiere de dos parametros
#@return: retorna el resultado de la operación
# nm1 + num2


def sumar(num1, num2):
    return num1 + num2

# @resultado = 15
resultado = sumar(10,5) #return 10+5=15

print(resultado)


def restar(a, b):
    return a - b
resultado = restar(15,5) 
print(resultado)


def multiplicar(a, b):
    return a * b
resultado = multiplicar(5,5) 
print(resultado)


def dividir(a, b):
    return a / b
resultado = dividir(25,5) 
print(resultado)

# --------------------
# PROGRAMA CALCULADORA
# --------------------

def programa_calculadora():
    print("[1] ------------------------------")
    print(f"[1] Sumar           [2] Restar")
    print(f"[3] Multiplicar     [4] Dividir\n")

    opcion = input("[?]: ")
    
    num1 = int(input("[Num 1]: "))
    num2 = int(input("[Num 2]: "))

    if opcion == '1':
        print("[Res +]: ", sumar(num1,num2))
    elif opcion == '2':
        print("[Res -]: ", restar(num1,num2))
    elif opcion == '3':
        print("[Res *]: ", multiplicar(num1,num2))
    elif opcion == '4':
        print("[Res /]: ", dividir(num1,num2))
    
    print("----------------------------------")




