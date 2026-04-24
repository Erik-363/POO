from modelo import ModeloJuego
from vista import VistaJuego

class ControladorJuego:
    def __init__(self):
        self.modelo = ModeloJuego()
        self.vista = VistaJuego()

    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            intento = self.vista.pedir_numero()
            resultado = self.modelo.verificar(intento)
            self.vista.mostrar_pista(resultado)

            if resultado == "correcto":
                break