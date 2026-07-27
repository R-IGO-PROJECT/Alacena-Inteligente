from paquete_productos.clases_de_productos import *
from utils import *
from paquete_productos.funciones_imprimir_menus import *

def registrar_producto(inventario: list):
    flag = True
    while True:
        imprimir_continuar_registro()
        opc = definir_rango_valido_numero_entero(0, 1)
        match opc:
            case 0:
                return inventario
            case 1:
                flag = True
                while flag:    
                    print("Cuantos productos quiere registrar?: ")
                    cantidad_productos = validar_entero()
                    if cantidad_productos <= 0:
                        print("Ingrese un numero mayor a 0")
                    else:
                        break
                for i in range(cantidad_productos):
                    imprimir_tipos_de_producto()
                    opc_categoria = definir_rango_valido_numero_entero(0, 3)
                    match opc_categoria:
                        case 0:
                            cancelando()
                            return inventario
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
                        case _:
                            error_match_case()
            case _:
                error_match_case()

def registro_general_de_producto():
    imprimir_categorias_de_productos()
    categoria_producto = definir_rango_valido_numero_entero(1, 8)
    imprime_pregunta_del_nombre()
    nombre_producto = validar_string()
    imprime_pregunta_si_compro_paquetes()
    pregunta_paquetes = definir_rango_valido_numero_entero(1, 2)
    match pregunta_paquetes:
        case 1:
            flag = True
            while flag:
                imprime_pregunta_de_paquetes()
                numero_paquetes = validar_entero()
                if numero_paquetes <= 0:
                    print("Ingrese un numero mayor a 0")
                else:
                    break
            while flag:
                imprime_pregunta_de_unidades_por_paquete()
                unidades_por_paquete = validar_entero()
                if unidades_por_paquete <= 0:
                    print("Ingrese un numero mayor a 0")
                else:
                    break
            return categoria_producto, nombre_producto, numero_paquetes, unidades_por_paquete
        case 2:
            numero_paquetes = 1
            flag = True
            while flag:
                imprime_pregunta_numero_de_unidades_solas()
                unidades = validar_entero()
                if unidades <= 0:
                    print("Ingrese un numero mayor a 0")
                else:
                    break
            return categoria_producto, nombre_producto, numero_paquetes, unidades
        case _:
            error_match_case() 

def registrar_producto_a_granel():
    imprime_pregunta_cantidad_si_en_gr_o_kg()
    opc = definir_rango_valido_numero_entero(1, 2)
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
    opc = definir_rango_valido_numero_entero(1, 2)
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

def mostrar_productos(inventario):
    for producto in inventario:
        producto.mostrar_producto()
        