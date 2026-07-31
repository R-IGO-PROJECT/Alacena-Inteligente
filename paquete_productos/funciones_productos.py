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

def borrar_producto(inventario: list):
    while True:
        imprimir_continuar_borrando_producto()
        opc = definir_rango_valido_numero_entero(0, 1)
        match opc:
            case 0:
                return inventario
            case 1:
                while True:
                    imprime_pregunta_mostrar_todo_el_inventario_o_ir_a_borrar_por_busqueda()
                    opc = definir_rango_valido_numero_entero(0, 4)
                    match opc:
                        case 0:
                            cancelando()
                            return inventario
                        case 1:
                            mostrar_productos(inventario)
                        case 2:
                            while True:
                                imprime_pregunta_ID_a_borrar()
                                ID_borrar = validar_entero()
                                ID_borrar_str = str(ID_borrar)
                                coincidencias = []
                                for producto in inventario:
                                    id_producto_inventario = str(producto.id)
                                    if ID_borrar_str in id_producto_inventario:
                                        coincidencias.append(producto)
                                if len(coincidencias) == 0:
                                    imprime_no_encontro_el_producto()
                                    pregunta_continuar_o_salir_ID_no_encontrado()
                                    opc = definir_rango_valido_numero_entero(1, 2)
                                    match opc:
                                        case 1:
                                            pass
                                        case 2:
                                            cancelando()
                                            return inventario
                                else:
                                    imprime_mensaje_coincidencias_encontradas()
                                    for coincidencia in coincidencias:
                                        coincidencia.mostrar_producto()
                                    while True:
                                        imprime_pregunta_ID_a_borrar_confirmacion()
                                        ID_borrar_confirmar = validar_entero()
                                        lista_coincidencia_final = []
                                        for coincidencia in coincidencias:
                                            if coincidencia.id == ID_borrar_confirmar:
                                                lista_coincidencia_final.append(coincidencia)
                                        if len(lista_coincidencia_final) == 0:
                                            imprime_mensaje_ID_no_valido()
                                        else:
                                            break
                                    imprime_mensaje_producto_seleccionado()
                                    lista_coincidencia_final[0].mostrar_producto()
                                    pregunta_continuar_con_eliminar_el_producto()
                                    opc = definir_rango_valido_numero_entero(1, 2)
                                    match opc:
                                        case 1:
                                            for indice_producto, producto in enumerate(inventario):
                                                if lista_coincidencia_final[0].id == producto.id:
                                                    indice_borrar = indice_producto
                                            inventario.pop(indice_borrar)
                                            imprime_producto_eliminado()
                                            return inventario
                                        case 2:
                                            pregunta_continuar_o_salir_ID_no_encontrado()
                                            opc = definir_rango_valido_numero_entero(1, 2)
                                            match opc:
                                                case 1:
                                                    pass
                                                case 2:
                                                    cancelando()
                                                    return inventario
                        case 3:
                            while True:
                                imprime_pregunta_nombre_a_borrar()
                                nombre_borrar = validar_string()
                                nombre_borrar = nombre_borrar.strip().lower()
                                coincidencias = []
                                for producto in inventario:
                                    nombre_producto = producto.nombre
                                    nombre_producto = nombre_producto.strip().lower()
                                    if nombre_borrar in nombre_producto:
                                        coincidencias.append(producto)
                                if len(coincidencias) == 0:
                                    imprime_no_encontro_el_producto()
                                    pregunta_continuar_o_salir_nombre_no_encontrado()
                                    opc = definir_rango_valido_numero_entero(1, 2)
                                    match opc:
                                        case 1:
                                            pass
                                        case 2:
                                            cancelando()
                                            return inventario
                                else:
                                    imprime_mensaje_coincidencias_encontradas()
                                    for coincidencia in coincidencias:
                                        coincidencia.mostrar_producto()
                                    while True:
                                        imprime_pregunta_ID_a_borrar_confirmacion()
                                        ID_borrar_confirmar = validar_entero()
                                        lista_coincidencia_final = []
                                        for coincidencia in coincidencias:
                                            if coincidencia.id == ID_borrar_confirmar:
                                                lista_coincidencia_final.append(coincidencia)
                                        if len(lista_coincidencia_final) == 0:
                                            imprime_mensaje_nombre_no_valido()
                                        else:
                                            break
                                    imprime_mensaje_producto_seleccionado()
                                    lista_coincidencia_final[0].mostrar_producto()
                                    pregunta_continuar_con_eliminar_el_producto()
                                    opc = definir_rango_valido_numero_entero(1, 2)
                                    match opc:
                                        case 1:
                                            for indice_producto, producto in enumerate(inventario):
                                                if lista_coincidencia_final[0].id == producto.id:
                                                    indice_borrar = indice_producto
                                            inventario.pop(indice_borrar)
                                            imprime_producto_eliminado()
                                            return inventario
                                        case 2:
                                            pregunta_continuar_o_salir_nombre_no_encontrado()
                                            opc = definir_rango_valido_numero_entero(1, 2)
                                            match opc:
                                                case 1:
                                                    pass
                                                case 2:
                                                    cancelando()
                                                    return inventario
                        case 4:
                            while True:
                                imprime_pregunta_categoria_a_borrar()
                                categoria_borrar = definir_rango_valido_numero_entero(1, 8)
                                coincidencias = []
                                for producto in inventario:
                                    categoria_producto = producto.categoria
                                    if categoria_borrar == categoria_producto:
                                        coincidencias.append(producto)
                                if len(coincidencias) == 0:
                                    imprime_no_encontro_el_producto()
                                    pregunta_continuar_o_salir_categoria_no_encontrada()
                                    opc = definir_rango_valido_numero_entero(1, 2)
                                    match opc:
                                        case 1:
                                            pass
                                        case 2:
                                            cancelando()
                                            return inventario
                                else:
                                    imprime_mensaje_coincidencias_encontradas()
                                    for coincidencia in coincidencias:
                                        coincidencia.mostrar_producto()
                                    while True:
                                        imprime_pregunta_ID_a_borrar_confirmacion()
                                        ID_borrar_confirmar = validar_entero()
                                        lista_coincidencia_final = []
                                        for coincidencia in coincidencias:
                                            if coincidencia.id == ID_borrar_confirmar:
                                                lista_coincidencia_final.append(coincidencia)
                                        if len(lista_coincidencia_final) == 0:
                                            imprime_mensaje_ID_no_valido()
                                        else:
                                            break
                                    imprime_mensaje_producto_seleccionado()
                                    lista_coincidencia_final[0].mostrar_producto()
                                    pregunta_continuar_con_eliminar_el_producto()
                                    opc = definir_rango_valido_numero_entero(1, 2)
                                    match opc:
                                        case 1:
                                            for indice_producto, producto in enumerate(inventario):
                                                if lista_coincidencia_final[0].id == producto.id:
                                                    indice_borrar = indice_producto
                                            inventario.pop(indice_borrar)
                                            imprime_producto_eliminado()
                                            return inventario
                                        case 2:
                                            pregunta_continuar_o_salir_nombre_no_encontrado()
                                            opc = definir_rango_valido_numero_entero(1, 2)
                                            match opc:
                                                case 1:
                                                    pass
                                                case 2:
                                                    cancelando()
                                                    return inventario
                        case _:
                            error_match_case()
            case _:
                error_match_case()