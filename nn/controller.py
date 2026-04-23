from model import Persona
from view import Vista

class Controlador:
    def __init__(self):
        self.modelo = []
        self.vista = Vista()

    def agregar_persona(self):
        nombre = self.vista.pedir_nombre()
        edad = self.vista.pedir_edad()
        persona = Persona(nombre, edad)
        self.modelo.append(persona)
        self.vista.mostrar_mensaje(f"Persona {nombre} agregada.")

    def mostrar_personas(self):
        self.vista.mostrar_personas(self.modelo)

    def ejecutar(self):
        while True:
            print("\nOpciones:")
            print("1. Agregar persona")
            print("2. Mostrar personas")
            print("3. Salir")
            opcion = input("Ingrese una opción: ")

            if opcion == '1':
                self.agregar_persona()
            elif opcion == '2':
                self.mostrar_personas()
            elif opcion == '3':
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida.")

if __name__ == "__main__":
    controlador = Controlador()
    controlador.ejecutar()
    