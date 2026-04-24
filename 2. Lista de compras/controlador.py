from modelo import ModeloCompras, Producto
from vista import VistaCompras

class ControladorCompras:
    def __init__(self):
        self.modelo = ModeloCompras()
        self.vista = VistaCompras()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            op = self.vista.pedir_opcion()

            if op == "1":
                n, c = self.vista.pedir_producto()
                self.modelo.agregar(Producto(n, c))

            elif op == "2":
                nombre = self.vista.pedir_nombre()
                self.modelo.eliminar(nombre)

            elif op == "3":
                nombre = self.vista.pedir_nombre()
                self.modelo.marcar_comprado(nombre)

            elif op == "4":
                self.vista.mostrar_lista(self.modelo.listar())

            elif op == "5":
                break
