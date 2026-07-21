from paquete_imprimir.modulo_imprimir_menu import *
from utils import *

flag = True
while flag:
    imprimir_menu()
    opc = validar_entero()
        
    match opc:
        case 0:
            imprimir_despedida()
            flag = False
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

    