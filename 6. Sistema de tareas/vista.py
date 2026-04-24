class VistaTareas:

    def mostrar_menu(self):
        print("\n=== Tareas ===")
        print("1. Agregar")
        print("2. Completar")
        print("3. Eliminar")
        print("4. Ver tareas")
        print("5. Salir")

    def pedir_opcion(self):
        return input("Opción: ")

    def pedir_descripcion(self):
        return input("Descripción: ")

    def mostrar_tareas(self, tareas):
        for t in tareas:
            estado = "hecha" if t.completada else "sin completar"
            print(f"{t.descripcion} - {estado}")