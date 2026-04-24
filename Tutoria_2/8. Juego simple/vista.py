class VistaJuego:

    def mostrar_menu(self):
        print("\n=== Adivina el número (1-10) ===")

    def pedir_numero(self):
        return int(input("Tu intento: "))

    def mostrar_pista(self, mensaje):
        if mensaje == "bajo":
            print("Muy bajo")
        elif mensaje == "alto":
            print("Muy alto")
        else:
            print("¡Correcto!")