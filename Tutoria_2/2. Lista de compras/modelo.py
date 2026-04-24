class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.comprado = False


class ModeloCompras:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def eliminar(self, nombre):
        self.productos = [p for p in self.productos if p.nombre != nombre]

    def marcar_comprado(self, nombre):
        for p in self.productos:
            if p.nombre == nombre:
                p.comprado = True

    def listar(self):
        return self.productos