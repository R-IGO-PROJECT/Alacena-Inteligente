from paquete_imprimir.modulo_imprimir_menu import *
from utils import *
from paquete_productos.funciones_productos import registrar_producto

inventario = []
flag = True
while flag:
    imprimir_menu()
    opc = definir_rango_valido_numero_entero(0, 4)
        
    match opc:
        case 0:
            imprimir_despedida()
            flag = False
        case 1:
            inventario = registrar_producto(inventario)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            error_match_case()
            