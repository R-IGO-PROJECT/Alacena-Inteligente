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

def validar_string():
    flag = True
    while flag:
        respuesta_string = input("Ingrese su respuesta: ")
        validar_respuesta_vacia = respuesta_string.strip()
        if validar_respuesta_vacia == "":
            print("Ingrese de nuevo una respuesta valida y que no sea vacia")
        else:
            return validar_respuesta_vacia
            