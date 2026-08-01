def validar_entero():
    while True:
        numero = input("Ingrese un numero entero: ")
        try:
            numero_entero = int(numero)
            break
        except ValueError:
            print("El numero que ingreso no es un numero entero, intentelo de nuevo")
    return numero_entero

def validar_decimal():
    while True:
        numero = input("Ingrese un numero entero: ")
        try:
            numero_decimal = float(numero)
            break
        except ValueError:
            print("El numero que ingreso no es un numero decimal o entero, intentelo de nuevo")
    return numero_decimal

def validar_string():
    while True:
        respuesta_string = input("Ingrese su respuesta: ")
        validar_respuesta_vacia = respuesta_string.strip()
        if validar_respuesta_vacia == "":
            print("Ingrese de nuevo una respuesta valida y que no sea vacia")
        else:
            return validar_respuesta_vacia
            
def error_match_case():
    print("ERROR: Opcion no valida, seleccione una de las opciones aceptables")

def definir_rango_valido_numero_entero(min, max):
    while True:
        numero_entero = validar_entero()
        if min <= numero_entero <= max:
            return numero_entero
        else:
            print("El numero ingresado no esta entre el rango de valores permitidos, ingrese uno valido")
