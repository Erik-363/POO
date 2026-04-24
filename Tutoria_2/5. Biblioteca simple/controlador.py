from modelo import ModeloBiblioteca, Libro
from vista import VistaBiblioteca

class ControladorBiblioteca:
    def __init__(self):
        self.modelo = ModeloBiblioteca()
        self.vista = VistaBiblioteca()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            op = self.vista.pedir_opcion()

            if op == "1":
                t, a = self.vista.pedir_libro()
                self.modelo.agregar(Libro(t, a))

            elif op == "2":
                t = self.vista.pedir_titulo()
                self.modelo.prestar(t)

            elif op == "3":
                t = self.vista.pedir_titulo()
                self.modelo.devolver(t)

            elif op == "4":
                self.vista.mostrar_libros(self.modelo.listar())

            elif op == "5":
                break