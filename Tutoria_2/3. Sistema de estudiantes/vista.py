class VistaEstudiantes:

    def mostrar_menu(self):
        print("\n=== Estudiantes ===")
        print("1. Agregar estudiante")
        print("2. Ver estudiantes")
        print("3. Salir")

    def pedir_opcion(self):
        return input("Opción: ")

    def pedir_datos(self):
        nombre = input("Nombre: ")
        notas = list(map(float, input("Notas separadas por espacio: ").split()))
        return nombre, notas

    def mostrar_estudiantes(self, estudiantes):
        for e in estudiantes:
            print(f"{e.nombre} - Promedio: {e.promedio():.2f}")