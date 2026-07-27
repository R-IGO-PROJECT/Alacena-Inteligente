class Producto:
    def __init__(self, id, nombre, categoria, paquetes, unidades):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.unidades = unidades
        self.paquetes = paquetes

    def mostrar_producto(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Categoria: {self.categoria}")
        print(f"Unidades: {self.unidades}")
        print(f"Paquetes: {self.paquetes}")

class ProductoSolidoGranel(Producto):
    def __init__(self, id, nombre, categoria, paquetes, unidades, peso_gramos):
        super().__init__(id, nombre, categoria, paquetes, unidades)
        self.peso_gramos = peso_gramos

    def mostrar_producto(self):
        super().mostrar_producto()
        print(f"Peso en gramos: {self.peso_gramos} | Peso en kilos: {round(self.peso_gramos / 1000, 2)}")

class ProductoLiquido(Producto):
    def __init__(self, id, nombre, categoria, paquetes, unidades, mililitros):
        super().__init__(id, nombre, categoria, paquetes, unidades)
        self.mililitros = mililitros

    def mostrar_producto(self):
        super().mostrar_producto()
        print(f"Volumen en mililitros: {self.mililitros} | Volumen en Litros: {round(self.mililitros / 1000, 2)}")
