from modelo import ModeloAgenda, Contacto
from vista import VistaAgenda

class ControladorAgenda:
    def __init__(self):
        self.modelo = ModeloAgenda()
        self.vista = VistaAgenda()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            op = self.vista.pedir_opcion()

            if op == "1":
                n, t, e = self.vista.pedir_datos()
                self.modelo.agregar(Contacto(n, t, e))

            elif op == "2":
                nombre = self.vista.pedir_nombre()
                self.modelo.eliminar(nombre)

            elif op == "3":
                contactos = self.modelo.listar()
                self.vista.mostrar_contactos(contactos)

            elif op == "4":
                break
