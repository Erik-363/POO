from modelo import ModeloInventario, Producto
from vista import VistaInventario

class ControladorInventario:
    def __init__(self):
        self.modelo = ModeloInventario()
        self.vista = VistaInventario()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            op = self.vista.pedir_opcion()

            if op == "1":
                n, s, p = self.vista.pedir_producto()
                self.modelo.agregar(Producto(n, s, p))

            elif op == "2":
                n, c = self.vista.pedir_venta()
                self.modelo.vender(n, c)

            elif op == "3":
                self.vista.mostrar_inventario(self.modelo.listar())

            elif op == "4":
                break