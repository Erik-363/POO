from modelo import ModeloGastos, Gasto
from vista import VistaGastos

class ControladorGastos:
    def __init__(self):
        self.modelo = ModeloGastos()
        self.vista = VistaGastos()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            op = self.vista.pedir_opcion()

            if op == "1":
                c, m, f = self.vista.pedir_datos()
                self.modelo.agregar(Gasto(c, m, f))

            elif op == "2":
                resumen = self.modelo.resumen_por_categoria()
                self.vista.mostrar_resumen(resumen)

            elif op == "3":
                break