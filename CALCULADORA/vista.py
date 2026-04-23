# vista.py
import os
class VistaCalculadora:

    def limpiar_consola(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_menu(self):
        print("\n=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

    def pedir_opcion(self):
        return input("Seleccione una opción: ")

    def pedir_n1(self):
        return float(input("\nIngrese el primer número: "))

    def pedir_n2(self):
        return float(input("Ingrese el segundo número: "))
    
    def mostrar_resultado(self, resultado):
        print(f"\nResultado: {resultado:.1f}")

    def pausa(self):
        input("\nPresione Enter para continuar...")
        self.limpiar_consola()

    def mostrar_error(self, mensaje):
        print(f"Error: {mensaje}")
