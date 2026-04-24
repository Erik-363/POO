from modelo import ModeloTareas, Tarea
from vista import VistaTareas

class ControladorTareas:
    def __init__(self):
        self.modelo = ModeloTareas()
        self.vista = VistaTareas()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            op = self.vista.pedir_opcion()

            if op == "1":
                d = self.vista.pedir_descripcion()
                self.modelo.agregar(Tarea(d))

            elif op == "2":
                d = self.vista.pedir_descripcion()
                self.modelo.completar(d)

            elif op == "3":
                d = self.vista.pedir_descripcion()
                self.modelo.eliminar(d)

            elif op == "4":
                self.vista.mostrar_tareas(self.modelo.listar())

            elif op == "5":
                break