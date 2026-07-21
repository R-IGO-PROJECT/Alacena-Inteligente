def validar_entero():
    flag = True
    while flag:
        numero = input("Ingrese un numero entero: ")
        try:
            numero_entero = int(numero)
            break
        except ValueError:
            print("El numero que ingreso no es un numero entero, intentelo de nuevo")
    return numero_entero

def validar_decimal():
    flag = True
    while flag:
        numero = input("Ingrese un numero entero: ")
        try:
            numero_decimal = float(numero)
            break
        except ValueError:
            print("El numero que ingreso no es un numero decimal o entero, intentelo de nuevo")
    return numero_decimal
