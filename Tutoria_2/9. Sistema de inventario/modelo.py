class Producto:
    def __init__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio


class ModeloInventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def vender(self, nombre, cantidad):
        for p in self.productos:
            if p.nombre == nombre:
                p.stock -= cantidad

    def listar(self):
        return self.productos