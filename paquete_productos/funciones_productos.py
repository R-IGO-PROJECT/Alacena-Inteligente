from paquete_productos.clases_de_productos import *
from utils import *
from paquete_productos.funciones_imprimir_menus import *

def registrar_producto(inventario):
    flag = True
    while True:
        imprimir_continuar_registro()
        opc = validar_entero()
        match opc:
            case 0:
                break
            case 1:
                print("Cuantos productos quiere registrar?: ")
                cantidad_productos = validar_entero()
                for i in range(cantidad_productos):
                    imprimir_tipos_de_producto()
                    opc_categoria = validar_entero()
                    match opc_categoria:
                        case 1:
                            categoria, nombre, numero_paquetes, unidades = registro_general_de_producto()
                            inventario = guardar_producto_general(categoria, nombre, numero_paquetes, unidades, inventario)
                        case 2:
                            categoria, nombre, numero_paquetes, unidades = registro_general_de_producto()
                            peso = registrar_producto_a_granel()
                            inventario = guardar_producto_a_granel(categoria, nombre, numero_paquetes, unidades, peso, inventario)
                        case 3:
                            categoria, nombre, numero_paquetes, unidades = registro_general_de_producto()
                            liquido = registrar_producto_liquido()
                            inventario = guardar_producto_liquido(categoria, nombre, numero_paquetes, unidades, liquido, inventario)
                        case 0:
                            cancelando()
                            return inventario
                        case _:
                            error_match_case()
            case _:
                error_match_case()

def registro_general_de_producto():
    imprimir_categorias_de_productos()
    categoria_producto = validar_entero()
    imprime_pregunta_del_nombre()
    nombre_producto = validar_string()
    imprime_pregunta_si_compro_paquetes()
    pregunta_paquetes = validar_entero()
    match pregunta_paquetes:
        case 1:
            imprime_pregunta_de_paquetes()
            numero_paquetes = validar_entero()
            imprime_pregunta_de_unidades_por_paquete()
            unidades_por_paquete = validar_entero()
            return categoria_producto, nombre_producto, numero_paquetes, unidades_por_paquete
        case 2:
            numero_paquetes = 1
            imprime_pregunta_numero_de_unidades_solas()
            unidades = validar_entero()
            return categoria_producto, nombre_producto, numero_paquetes, unidades
        case _:
            error_match_case() 

def registrar_producto_a_granel():
    imprime_pregunta_cantidad_si_en_gr_o_kg()
    opc = validar_entero()
    match opc:
        case 1:
            imprime_pregunta_cantidad_gr()
            gramos = validar_decimal()
            return gramos
        case 2:
            imprime_pregunta_cantidad_kg()
            kilos = validar_decimal()
            gramos = kilos * 1000
            return gramos
        case _:
            error_match_case()

def registrar_producto_liquido():
    imprime_pregunta_si_ml_o_L()
    opc = validar_entero()
    match opc:
        case 1:
            imprime_pregunta_cantidad_ml()
            mililitros = validar_decimal
            return mililitros
        case 2:
            imprime_pregunta_cantidad_L()
            litros = validar_decimal()
            mililitros = litros * 1000
            return mililitros
        case _:
            error_match_case()

def guardar_producto_general(categoria, nombre, numero_paquetes, unidades, inventario):
    indice = len(inventario) + 1
    nuevo_producto = Producto(indice, nombre, categoria, numero_paquetes, unidades)
    inventario.append(nuevo_producto)
    confirmacion_producto_registrado()
    return inventario

def guardar_producto_a_granel(categoria, nombre, numero_paquetes, unidades, peso, inventario):
    indice = len(inventario) + 1
    nuevo_producto = ProductoSolidoGranel(indice, nombre, categoria, numero_paquetes, unidades, peso)
    inventario.append(nuevo_producto)
    confirmacion_producto_registrado()
    return inventario

def guardar_producto_liquido(categoria, nombre, numero_paquetes, unidades, liquido, inventario):
    indice = len(inventario) + 1
    nuevo_producto = ProductoLiquido(indice, nombre, categoria, numero_paquetes, unidades, liquido)
    inventario.append(nuevo_producto)
    confirmacion_producto_registrado()
    return inventario
