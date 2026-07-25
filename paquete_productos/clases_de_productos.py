class Producto:
    def __init__(self, id, nombre, categoria, paquetes, unidades):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.unidades = unidades
        self.paquetes = paquetes

class ProductoSolidoGranel(Producto):
    def __init__(self, id, nombre, categoria, paquetes, unidades, peso_gramos):
        super().__init__(id, nombre, categoria, paquetes, unidades)
        self.peso_gramos = peso_gramos

class ProductoLiquido(Producto):
    def __init__(self, id, nombre, categoria, paquetes, unidades, mililitros):
        super().__init__(id, nombre, categoria, paquetes, unidades)
        self.mililitros = mililitros
