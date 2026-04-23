# controlador.py
from modelo import ModeloCalculadora
from vista import VistaCalculadora

class ControladorCalculadora:
    def __init__(self):
        self.modelo = ModeloCalculadora()
        self.vista = VistaCalculadora()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = self.vista.pedir_opcion()

            try:

                if opcion == "1":
                    numero1 = self.vista.pedir_n1()
                    numero2 = self.vista.pedir_n2()
                    resultado = self.modelo.sumar(numero1, numero2)
                    self.vista.mostrar_resultado(resultado)
                    self.vista.pausa()

                elif opcion == "2":
                    numero1 = self.vista.pedir_n1()
                    numero2 = self.vista.pedir_n2()
                    resultado = self.modelo.restar(numero1, numero2)
                    self.vista.mostrar_resultado(resultado)
                    self.vista.pausa()

                elif opcion == "3":
                    numero1 = self.vista.pedir_n1()
                    numero2 = self.vista.pedir_n2()
                    resultado = self.modelo.multiplicar(numero1, numero2)
                    self.vista.mostrar_resultado(resultado)
                    self.vista.pausa()

                elif opcion == "4":
                    numero1 = self.vista.pedir_n1()
                    numero2 = self.vista.pedir_n2()
                    resultado = self.modelo.dividir(numero1, numero2)
                    self.vista.mostrar_resultado(resultado)
                    self.vista.pausa()

                elif opcion == "5":
                    print("Saliendo del conversor...")
                    break
                else:
                    self.vista.mostrar_error("Opción no válida")
                    self.vista.pausa()

            except ValueError as e:
                    self.vista.mostrar_error(str(e))
                    self.vista.pausa()