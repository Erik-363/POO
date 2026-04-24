from modelo import ModeloEstudiantes, Estudiante
from vista import VistaEstudiantes

class ControladorEstudiantes:
    def __init__(self):
        self.modelo = ModeloEstudiantes()
        self.vista = VistaEstudiantes()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            op = self.vista.pedir_opcion()

            if op == "1":
                n, notas = self.vista.pedir_datos()
                self.modelo.agregar(Estudiante(n, notas))

            elif op == "2":
                self.vista.mostrar_estudiantes(self.modelo.listar())

            elif op == "3":
                break